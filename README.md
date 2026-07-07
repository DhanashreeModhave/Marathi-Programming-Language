# 🇮🇳 Marathi Programming Language

A custom programming language developed in **Marathi** to make programming easier and more accessible for native Marathi speakers. This project provides a simple compiler/interpreter along with a graphical IDE built using Streamlit.

---

## 📌 Project Overview

The Marathi Programming Language allows users to write programs using Marathi keywords instead of English programming syntax. It is designed as an educational programming language that demonstrates compiler construction concepts such as lexical analysis, parsing, Abstract Syntax Tree (AST) generation, and runtime execution.

This project was developed as a **Final Year Computer Engineering Project**.

---

## ✨ Features

- ✅ Programming using Marathi keywords
- ✅ Variable declaration and assignment
- ✅ Arithmetic operations
- ✅ Print statements
- ✅ Conditional statements (If)
- ✅ Loops (For, While)
- ✅ Break and Continue statements
- ✅ User-defined functions
- ✅ Function parameters and return values
- ✅ Arrays (List support)
- ✅ Built-in functions
  - `length()`
  - `push()`
- ✅ Runtime memory visualization
- ✅ Debug mode
- ✅ AST (Abstract Syntax Tree) visualization
- ✅ Syntax checking
- ✅ File Save (.mr)
- ✅ File Open (.mr)
- ✅ Streamlit-based IDE

---

## 🏗 Project Architecture

```
Source Code (.mr)
        │
        ▼
 Lexer (Tokenization)
        │
        ▼
 Parser (AST Generation)
        │
        ▼
 Runtime / Interpreter
        │
        ▼
 Program Output
```

---

## 📂 Project Structure

```
Marathi_Programming_Language/
│
├── marathi_lang/
│   ├── lexer.py
│   ├── parser.py
│   ├── runtime.py
│   ├── debugger.py
│   ├── syntax_checker.py
│   ├── ast_visual.py
│   ├── tokens.py
│   └── __init__.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── sample_programs/
```

---

## 🚀 Technologies Used

- Python 3
- Streamlit
- Graphviz
- Object-Oriented Programming
- Compiler Design Concepts

---

## 📖 Supported Marathi Keywords

| Marathi Keyword | Meaning |
|-----------------|---------|
| घे | Variable Declaration |
| छापा | Print |
| जर | If |
| अन्यथा | Else |
| साठी | For Loop |
| जोपर्यंत | While Loop |
| थांब | Break |
| सुरू_ठेवा | Continue |
| परत | Return |

---

## 💻 Example Program

```marathi
घे a = 10;
घे b = 20;

छापा(a + b);
```

### Output

```
30
```

---

## ▶️ Running the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Marathi-Programming-Language.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run IDE

```bash
streamlit run streamlit_app.py
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Code Editor
- Program Output
- AST Visualization
- Debug Mode

---

## 🎯 Educational Objectives

This project demonstrates the implementation of:

- Lexical Analysis
- Parsing
- AST Construction
- Runtime Environment
- Symbol Table
- Interpreter Design
- Custom Language Development
- IDE Development

---

## 🔮 Future Enhancements

- String handling
- Dictionaries
- Object-Oriented Programming
- Modules
- Package Manager
- Better Error Reporting
- Auto-completion
- Syntax Highlighting
- Compiler Optimization
- Executable (.exe) Generation

---

## 📜 License

This project is intended for educational and research purposes.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
