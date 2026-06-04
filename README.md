# Custom Password Generator

A secure, command-line password generator tool written in Python. It allows users to fully customize the length and character sets of their passwords to ensure strong account security.

## 🚀 Features

* **Adjustable Length:** Generate passwords of any chosen length (minimum length of 4 enforced for basic security).
* **Granular Complexity Settings:** Toggle different character sets on or off depending on your requirements:
  * Lowercase letters (enabled by default)
  * Uppercase letters
  * Numeric digits (`0-9`)
  * Special characters and symbols (e.g., `!@#$%^&*`)
* **Input Protection:** Gracefully handles invalid inputs like accidental letters in the length selector.

---

## 🛠️ Requirements

* **Python 3.x** installed on your operating system.
* No external packages or third-party library installations required (uses native Python modules: `random` and `string`).

---

## 💻 Installation & Setup

1. **Save the File:** Copy the python script code and save it as `password_gen.py` inside your desired directory.

2. **Open Terminal / Command Prompt:**
   Navigate into the folder where your script file resides:
   ```bash
   cd path/to/your/password-generator-folder
