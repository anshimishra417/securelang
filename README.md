# SecureLang 🔐

A custom programming language and compiler built with security as a first-class feature. SecureLang enforces secure coding practices at the **language level** — preventing common vulnerabilities like SQL injection, sensitive data exposure, and invalid input handling before code even runs.

---

## Why SecureLang?

Most languages let developers write insecure code. SecureLang makes insecure patterns impossible by design:

- **Input is always validated** — user inputs are checked for alphanumeric safety automatically
- **Passwords are never printed** — the language masks sensitive fields at the syntax level
- **Database queries are always parameterized** — SQL injection is structurally prevented

---

## Features

| Feature | Description |
|---|---|
| 🛡️ Input Validation | All `INPUT` statements auto-generate `.isalnum()` checks |
| 🔒 Password Masking | `PRINT password` compiles to a hidden output, never exposing the value |
| 🧱 Safe SQL Queries | `QUERY` statements generate parameterized queries using `?` placeholders |
| ⚙️ Full Compiler Pipeline | Lexing → Parsing → Semantic Analysis → Code Generation |

---

## Project Structure

```
securelang/
├── lexer.py              # Tokenizer — breaks source into tokens
├── parser.py             # Syntax analyzer — builds AST
├── security_analyzer.py  # Semantic analysis + security rule enforcement
├── code_generator.py     # Generates safe Python output code
├── main.py               # Entry point
├── app.py                # Web interface (Flask)
├── templates/
│   └── index.html        # Frontend UI
└── sample.sec            # Example SecureLang source file
```

---

## How It Works

### Compiler Pipeline

```
Source Code (.sec)
      ↓
   Lexer (lexer.py)         → Tokenizes the source
      ↓
   Parser (parser.py)       → Builds Abstract Syntax Tree (AST)
      ↓
   Security Analyzer        → Enforces security rules on the AST
      ↓
   Code Generator           → Outputs safe, executable Python code
```

### Example

**SecureLang source (`sample.sec`):**
```
INPUT username
INPUT password
QUERY SELECT * FROM users WHERE name = username
PRINT username
PRINT password
```

**Generated Python output:**
```python
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

username = input('Enter username: ').strip()
if not username.isalnum():
    print('Invalid input detected!')

password = input('Enter password: ').strip()
if not password.isalnum():
    print('Invalid input detected!')

cursor.execute('SELECT * FROM users WHERE name=?', (username,))

print(username)
print('Password is hidden for security reasons')  # 🔒 auto-masked

conn.commit()
conn.close()
```

---

## Getting Started

### Requirements
- Python 3.x

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/securelang.git
cd securelang
```

### Run the Compiler

```bash
python main.py sample.sec
```

### Run the Web Interface

```bash
python app.py
```
Then open `http://localhost:5000` in your browser.

---

## Security Rules Enforced

| Vulnerability | How SecureLang Prevents It |
|---|---|
| SQL Injection | All queries use parameterized `?` placeholders |
| Sensitive Data Exposure | Password variables are never printed in plain text |
| Unvalidated Input | Every `INPUT` statement includes alphanumeric validation |

---

## Tech Stack

- **Language:** Python
- **Lexer:** Custom tokenizer (`lexer.py`)
- **Parser:** Custom AST parser (`parser.py`)
- **Web Interface:** Flask + HTML/CSS
- **Output:** Python code with security best practices built in

---

## Author

**Anshi Mishra**
B.Tech Computer Science — Graphic Era Hill University
[LinkedIn](https://linkedin.com/in/YOUR_PROFILE) • [GitHub](https://github.com/YOUR_USERNAME)

---

## License

MIT License — feel free to use, modify, and build on this project.
