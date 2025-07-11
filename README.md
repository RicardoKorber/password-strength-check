# 🔐 Password Strength Checker

A modular Python application that analyzes the strength of a user's password using key security criteria. Built as part of an educational journey into back-end development and system analysis, this tool evaluates passwords based on composition, variety, and repetition.

## ⚙️ Features

- ✅ Checks minimum length (8 characters)
- ✅ Verifies use of both uppercase and lowercase letters
- ✅ Confirms presence of numerical digits
- ✅ Detects use of special characters (symbols)
- ✅ Identifies repeated characters
- 📊 Provides feedback on password weaknesses
- 💾 Modular architecture for future expansion and reuse

## 🛠 Project Structure

PSC/
├── checks/
│ ├── len_check.py
│ ├── cases_check.py
│ ├── digit_check.py
│ ├── symbol_check.py
│ └── duplicate_check.py
├── collector.py
├── judge.py
└── main.py

markdown
Copiar
Editar

- **main.py** — Central execution file that collects input, runs checks, and delivers judgment.
- **collector.py** — Collects the user’s password securely.
- **judge.py** — Compares the password’s score against strength criteria and provides feedback.
- **checks/** — Contains individual modules, each responsible for verifying a specific password property.

## 💡 How It Works

1. User submits a password.
2. Each module checks for a specific strength criterion.
3. A strength score is calculated based on passed checks.
4. If the score is less than maximum, the user receives feedback with detailed weaknesses.
5. If all checks pass, the password is deemed strong.

## ▶️ Running the Program

Ensure you are in the root directory (`PSC/`) and run:

```bash
python main.py
Requires Python 3.10+ for proper formatting and compatibility.

🧠 Author's Note
This project was forged during my foundational study of Python and system design, with the goal of:

Building functional, modular tools

Demonstrating back-end logic

Strengthening real-world coding skills

May the Omnissiah bless your passwords and guard them from heretical brute-force 
