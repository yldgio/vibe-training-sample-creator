/**
 * Password Generator Test Template
 * Use this template as a starting point for password generator tests
 */

describe('Password Generator', () => {
  describe('generatePassword', () => {
    test('generates password with specified length', () => {
      const options = { length: 16, uppercase: true, lowercase: true, numbers: true, symbols: false };
      const password = generatePassword(options);
      expect(password.length).toBe(16);
    });

    test('includes uppercase letters when enabled', () => {
      const options = { length: 20, uppercase: true, lowercase: false, numbers: false, symbols: false };
      const password = generatePassword(options);
      expect(password).toMatch(/[A-Z]/);
    });

    test('includes lowercase letters when enabled', () => {
      const options = { length: 20, uppercase: false, lowercase: true, numbers: false, symbols: false };
      const password = generatePassword(options);
      expect(password).toMatch(/[a-z]/);
    });

    test('includes numbers when enabled', () => {
      const options = { length: 20, uppercase: false, lowercase: false, numbers: true, symbols: false };
      const password = generatePassword(options);
      expect(password).toMatch(/[0-9]/);
    });

    test('includes symbols when enabled', () => {
      const options = { length: 20, uppercase: false, lowercase: false, numbers: false, symbols: true };
      const password = generatePassword(options);
      expect(password).toMatch(/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/);
    });

    test('generates unique passwords on each call', () => {
      const options = { length: 16, uppercase: true, lowercase: true, numbers: true, symbols: true };
      const password1 = generatePassword(options);
      const password2 = generatePassword(options);
      expect(password1).not.toBe(password2);
    });
  });

  describe('calculateStrength', () => {
    test('returns "weak" for short passwords', () => {
      expect(calculateStrength('abc')).toBe('weak');
    });

    test('returns "medium" for moderate passwords', () => {
      expect(calculateStrength('Abc12345')).toBe('medium');
    });

    test('returns "strong" for complex passwords', () => {
      expect(calculateStrength('Abc123!@#XyZ')).toBe('strong');
    });
  });
});
