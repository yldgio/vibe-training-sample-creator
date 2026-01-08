"""
Shared Tools for Multi-Agent System

Tools that can be used by any agent in the orchestration.
"""

import secrets
import string
from pydantic import BaseModel, Field


class GeneratePasswordInput(BaseModel):
    """Input schema for password generation."""
    length: int = Field(default=16, ge=8, le=128, description="Password length")
    include_uppercase: bool = Field(default=True, description="Include uppercase letters")
    include_lowercase: bool = Field(default=True, description="Include lowercase letters")
    include_numbers: bool = Field(default=True, description="Include numbers")
    include_symbols: bool = Field(default=True, description="Include special symbols")


class CheckPasswordStrengthInput(BaseModel):
    """Input schema for password strength checking."""
    password: str = Field(description="The password to check")


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
        "length_ok": len(password) >= 12,
        "has_uppercase": any(c.isupper() for c in password),
        "has_lowercase": any(c.islower() for c in password),
        "has_numbers": any(c.isdigit() for c in password),
        "has_symbols": any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password),
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
    
    recommendations = []
    if not checks["length_ok"]:
        recommendations.append("Increase length to at least 12 characters")
    if not checks["has_uppercase"]:
        recommendations.append("Add uppercase letters")
    if not checks["has_lowercase"]:
        recommendations.append("Add lowercase letters")
    if not checks["has_numbers"]:
        recommendations.append("Add numbers")
    if not checks["has_symbols"]:
        recommendations.append("Add special symbols")
    
    return {
        "password_length": len(password),
        "strength": strength,
        "score": f"{score}/5",
        "checks": checks,
        "recommendations": recommendations
    }
