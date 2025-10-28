##  Python Syntax Validator (using PLY)

This project provides a basic syntax validation check for Python code snippets using the **PLY (Python Lex-Yacc)** library. It separates the lexical analysis (tokenizing) and parsing (syntax checking) into distinct modules for clarity and maintainability.

---

### 📝 Project Structure

The project is structured with three core files:

| File | Description |
| :--- | :--- |
| `lexer.py` | Defines the **lexical analysis** rules using `ply.lex`, including all tokens (keywords, identifiers, operators, etc.) and their corresponding regular expressions. |
| `parser.py` | Defines the **parsing** rules (the grammar) using `ply.yacc`, specifying how tokens can be combined into valid Python syntax (production rules). |
| `main.py` | The **execution script** that reads input code, imports and initializes the lexer and parser, and executes the validation process. |

---

### ✨ Key Features

* **Tokenization:** Converts a string of Python code into a stream of recognized tokens.
* **Syntax Validation:** Determines if the token stream conforms to the grammar rules defined in `parser.py`.
* **Error Reporting:** Utilizes PLY's built-in error handling (`p_error` in `parser.py`) to report syntax violations.

---

### ⚙️ Prerequisites

You need **Python 3.x** and the **PLY** library installed on your system.

