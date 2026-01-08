"""
Password Generator Tools

Defines tools that the agent can call to generate and validate passwords.
Uses Pydantic for schema validation and automatic JSON schema generation.
"""

import secrets
import string
from pydantic import BaseModel, Field


# Tool input schemas (Pydantic models)
class GeneratePasswordInput(BaseModel):
    """Input schema for password generation."""
    length: int = Field(default=16, ge=8, le=128, description="Password length (8-128)")
    include_uppercase: bool = Field(default=True, description="Include uppercase letters")
    include_lowercase: bool = Field(default=True, description="Include lowercase letters")
    include_numbers: bool = Field(default=True, description="Include numbers")
    include_symbols: bool = Field(default=True, description="Include special symbols")


class CheckPasswordStrengthInput(BaseModel):
    """Input schema for password strength checking."""
    password: str = Field(description="The password to check")


class GenerateMultiplePasswordsInput(BaseModel):
    """Input schema for generating multiple passwords."""
    count: int = Field(default=3, ge=1, le=10, description="Number of passwords to generate")
    length: int = Field(default=16, ge=8, le=128, description="Password length")


# Tool implementations
def generate_password(params: GeneratePasswordInput) -> str:
    """Generate a cryptographically secure password."""
    charset = ""
    if params.include_uppercase:
        charset += string.ascii_uppercase
    if params.include_lowercase:
        charset += string.ascii_lowercase
    if params.include_numbers:
        charset += string.digits
    if params.include_symbols:
        charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not charset:
        return "Error: At least one character type must be selected"
    
    password = ''.join(secrets.choice(charset) for _ in range(params.length))
    return password


def check_password_strength(params: CheckPasswordStrengthInput) -> dict:
    """Check password strength and return detailed analysis."""
    password = params.password
    
    checks = {
        "length": len(password) >= 12,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "numbers": any(c.isdigit() for c in password),
        "symbols": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
    }
    
    score = sum(checks.values())
    
    if score <= 2:
        strength = "weak"
    elif score <= 3:
        strength = "medium"
    elif score <= 4:
        strength = "strong"
    else:
        strength = "very_strong"
    
    return {
        "password_length": len(password),
        "strength": strength,
        "score": f"{score}/5",
        "checks": checks,
        "recommendations": [
            f"Add {check}" for check, passed in checks.items() if not passed
        ]
    }


def generate_multiple_passwords(params: GenerateMultiplePasswordsInput) -> list[str]:
    """Generate multiple unique passwords."""
    passwords = []
    for _ in range(params.count):
        password = generate_password(GeneratePasswordInput(length=params.length))
        passwords.append(password)
    return passwords


# Tool registry for the agent
TOOLS = {
    "generate_password": {
        "function": generate_password,
        "schema": GeneratePasswordInput,
        "description": "Generate a cryptographically secure password with specified options"
    },
    "check_password_strength": {
        "function": check_password_strength,
        "schema": CheckPasswordStrengthInput,
        "description": "Check the strength of a password and get improvement recommendations"
    },
    "generate_multiple_passwords": {
        "function": generate_multiple_passwords,
        "schema": GenerateMultiplePasswordsInput,
        "description": "Generate multiple unique passwords at once"
    }
}


def get_tool_schemas() -> list[dict]:
    """Generate OpenAI-compatible tool schemas from Pydantic models."""
    schemas = []
    for name, tool in TOOLS.items():
        schemas.append({
            "type": "function",
            "function": {
                "name": name,
                "description": tool["description"],
                "parameters": tool["schema"].model_json_schema()
            }
        })
    return schemas


def execute_tool(name: str, arguments: dict) -> str:
    """Execute a tool by name with the given arguments."""
    if name not in TOOLS:
        return f"Error: Unknown tool '{name}'"
    
    tool = TOOLS[name]
    try:
        # Validate arguments with Pydantic
        params = tool["schema"](**arguments)
        result = tool["function"](params)
        return str(result)
    except Exception as e:
        return f"Error executing {name}: {str(e)}"
