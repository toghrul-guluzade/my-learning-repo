# Password Strength Checker

This repository contains two implementations of a **Password Strength Checker** that evaluates the strength of a password based on specific criteria and provides feedback. The purpose of these implementations is to help users create stronger and more secure passwords.

The GUI was designed in **Figma** and converted into **Tkinter code** using **Tkinter Designer**. The password strength logic was then integrated into the GUI with the help of **ChatGPT**.

---

## Features

### 1. GUI Version

- **File:** `password_strength_checker_GUI.py`
- **Framework:** Tkinter
- Provides real-time feedback and validates password criteria:
  - Minimum length (8 characters)
  - Mix of letters, digits, and special characters
  - Avoidance of common passwords.

### 2. Command-Line Version

- **File:** `PasswordStrengthChecker.py`
- Command-line tool to check password strength.
- Validates length, diversity, and common passwords.
- Outputs a score (0–8) with feedback.

---

## Requirements

- Python 3.x
- Tkinter (for GUI)

---

## Usage

### GUI Version

1. Install Python and Tkinter.
2. Place `common_passwords.txt` in a `files` folder.
3. Run:
   ```bash
   python password_strength_checker_GUI.py
   ```

### Command-Line Version

1. Install Python.
2. Ensure `common_passwords.txt` is in the script directory.
3. Run:
   ```bash
   python PasswordStrengthChecker.py
   ```

---

## Password Strength Criteria

- **Length:** Longer passwords score higher.
- **Character Diversity:** Uppercase, lowercase, digits, and special characters.
- **Avoidance of Common Passwords:** Verified against a predefined list.

---

## Sources

- [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer)
- [YouTube Tutorial](https://www.youtube.com/watch?v=NVPibVfFVtM)
- [Common Passwords List](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)
- Background image: *The Seine at Vétheuil (La Seine à Vétheuil)* by Claude Monet

---

## License

This project is licensed under the MIT License. See LICENSE for details.

