# Bhai_Py: Programming in Hinglish! 👋

Ever wanted to code in a language that feels more natural if you speak Hindi/Hinglish? Bhai_Py is here for the fun! It's a simple transpiler that translates code written using Hinglish keywords ("Bhai Lang") into standard Python code, which can then be executed.

Think of it like writing Python, but with a desi twist! 😎

## ✨ Features

*   **Hinglish Syntax:** Use keywords like `Ab man lo`, `bol bhai`, `Agar...toh`, `Jab tak...tab tak`, etc.
*   **Variable Declaration:** Easily declare variables.
*   **Input/Output:** Print to console and take user input.
*   **Control Flow:** Includes `if/elif/else`, `while`, and `for` loop structures.
*   **Functions & Classes:** Define your own functions and basic classes.
*   **Operators:** Supports common logical (`aur`, `ya`, `nhi`) and comparison (`ke barabar`, `se bada`, etc.) operators.
*   **Common Operations:** Built-in wrappers for common Python functions (math, list, string, type conversion).
*   **File Handling:** Basic file open, read, write, and close operations.
*   **Exception Handling:** `try/except/finally` blocks.
*   **Custom Error Messages:** Get friendly Hinglish error messages when things go wrong during execution!

## ⚙️ Installation

Currently, the primary way to use Bhai_Py is by running the `run_bhai.py` script directly.

1.  **Clone or Download:** Get the project files onto your machine.
    ```bash
    git clone <your-repo-url> # Replace with your repository URL
    cd bhai_py_project_directory # Navigate to the project folder
    ```
2.  **No explicit installation required** if you just use `run_bhai.py`.

*(Note: While a `setup.py` exists, the `console_script` entry point might need a `main` function in `bhai_py/__init__.py` to work directly as `bhai_py <filename>`. However, you could potentially install it locally using `pip install .` to make the `bhai_py` module available for import in other Python projects if needed).*

## 🚀 Usage

1.  **Write your code:** Create a file (e.g., `my_code.bhai` or `my_code.py`) and write your program using the Bhai Lang syntax (see guide below). Using a `.bhai` extension is recommended for clarity, but the script accepts any extension.
2.  **Run the transpiler script:** Execute your code using the `run_bhai.py` script in your terminal.

    ```bash
    python run_bhai.py <your_bhai_lang_file.bhai>
    ```

    For example:
    ```bash
    python run_bhai.py example.py
    ```

The script will:
1.  Read your Bhai Lang code.
2.  Translate it into standard Python code.
3.  Execute the translated Python code.
4.  If errors occur during execution, it will attempt to print helpful Hinglish error messages.

## 📖 Bhai Lang Syntax Guide

Here's a breakdown of the supported Bhai Lang syntax and its Python equivalent:

---

**1. Comments**

*   Just like Python, use `#` for comments.

    ```python
    # Yeh ek comment hai
    Ab man lo x = 10 # Yeh variable ke baad comment hai
    ```

---

**2. Imports**

*   **Import module:**
    *   Bhai Lang: `Bhai <module_name> la`
    *   Python: `import <module_name>`
    *   Example: `Bhai math la` -> `import math`

*   **Import module with alias:**
    *   Bhai Lang: `Bhai <module_name> ko <alias> bulate h`
    *   Python: `import <module_name> as <alias>`
    *   Example: `Bhai pandas ko pd bulate h` -> `import pandas as pd`

---

**3. Variable Declaration**

*   Bhai Lang: `Ab man lo <variable_name> = <value>`
*   Python: `<variable_name> = <value>`
*   Example:
    ```python
    Ab man lo name = "Sanjay"
    Ab man lo age = 25
    Ab man lo prices = [100, 200.5, 50]
    ```

---

**4. Printing Output**

*   Bhai Lang: `bol bhai <expression1>, <expression2>, ...`
*   Python: `print(<expression1>, <expression2>, ...)`
*   Example:
    ```python
    Ab man lo city = "Mumbai"
    bol bhai "Shehar:", city
    bol bhai 10 + 5
    ```

---

**5. Taking Input**

*   Bhai Lang: `mang le "<prompt_message>"` (Assign the result to a variable)
*   Python: `input("<prompt_message>")`
*   Example:
    ```python
    Ab man lo user_name = mang le "Apna naam batao: "
    bol bhai "Hello,", user_name
    ```

---

**6. Operators**

*   **Logical:**
    *   `aur` -> `and`
    *   `ya` -> `or`
    *   `nhi` -> `not` (Note: Be careful not to confuse with `Nhi toh:`)
*   **Comparison:** (Order matters in translation - longer phrases are checked first)
    *   `ke barabar nhi` -> `!=`
    *   `se bada ya barabar` -> `>=`
    *   `se chota ya barabar` -> `<=`
    *   `se bada` -> `>`
    *   `se chota` -> `<`
    *   `ke barabar` -> `==`
*   **Arithmetic:** Standard Python operators (`+`, `-`, `*`, `/`, `%`, `**`, `//`) work as usual.

    ```python
    Ab man lo score = 80
    Ab man lo age = 18
    Agar score se bada 75 aur age se bada ya barabar 18 toh:
        bol bhai "Eligible for distinction award"
    Agar nhi (score se chota 0) toh:
        bol bhai "Score seems valid"
    ```

---

**7. Control Flow**

*   **If-Elif-Else:**
    *   Bhai Lang:
        ```python
        Agar <condition> toh:
            # code block
        Maggar <condition> toh:
            # code block
        Nhi toh:
            # code block
        ```
    *   Python:
        ```python
        if <condition>:
            # code block
        elif <condition>:
            # code block
        else:
            # code block
        ```
    *   Example: See `example.py` lines 22-28.

*   **While Loop:**
    *   Bhai Lang: `Jab tak <condition> tab tak:`
    *   Python: `while <condition>:`
    *   Example:
        ```python
        Ab man lo count = 3
        Jab tak count se bada 0 tab tak:
            bol bhai count
            Ab man lo count = count - 1
        ```

*   **For Loop (Range):**
    *   Bhai Lang: `bhai <variable> ko <number> bar chakkar lagayein:`
    *   Python: `for <variable> in range(<number>):`
    *   Example:
        ```python
        bhai i ko 5 bar chakkar lagayein:
            bol bhai "Chakkar:", i
        ```

---

**8. Functions**

*   **Definition (No parameters):**
    *   Bhai Lang: `Bhai <function_name> banate h:`
    *   Python: `def <function_name>():`
*   **Definition (With parameters):**
    *   Bhai Lang: `Bhai <function_name> banate h (<param1>, <param2>, ...):`
    *   Python: `def <function_name> (<param1>, <param2>, ...):`
*   **Return Value:**
    *   Bhai Lang: `Bhai <value> wapis de`
    *   Python: `return <value>`
*   **Calling:** Call functions using standard Python syntax: `<function_name>(<arguments>)`
*   Example: See `example.py` lines 51-57.

---

**9. Classes**

*   **Definition:**
    *   Bhai Lang: `Bhai class <ClassName>:`
    *   Python: `class <ClassName>:`
*   **Methods:** Define methods (including `__init__`) using the function definition syntax inside the class block. Remember to include `self` as the first parameter.
*   **Instantiation & Usage:** Use standard Python syntax: `obj = ClassName(<args>)`, `obj.method(<args>)`
*   Example: See `example.py` lines 61-68.

---

**10. Exception Handling**

*   Bhai Lang:
    ```python
    Bhai try:
        # Risky code
    Bhai except <ExceptionType>: # Optional ExceptionType
        # Handle specific error
    Bhai except: # Catch any error
        # Handle general error
    Bhai finally:
        # Cleanup code (always runs)
    ```
*   Python:
    ```python
    try:
        # Risky code
    except <ExceptionType>:
        # Handle specific error
    except:
        # Handle general error
    finally:
        # Cleanup code
    ```
*   Example: See `example.py` lines 115-138.

---

**11. Built-in Function Wrappers / Math**

*(Optional `bhai ` prefix can be used)*

*   `sign_hatao(<value>)` -> `abs(<value>)`
*   `no_ko_ghumao(<value>)` -> `round(<value>)`
*   `root_nikalo(<value>)` -> `math.sqrt(<value>)` (Requires `Bhai math la` import)
*   `mila(<iterable>)` -> `sum(<iterable>)`
*   `count_kro(<sequence>)` -> `len(<sequence>)`
*   `chota_no_dhond(<iterable>)` -> `min(<iterable>)`
*   `bada_no_dhond(<iterable>)` -> `max(<iterable>)`

---

**12. List Operations**

*(Optional `bhai ` prefix can be used)*

*   `dalde(<list_var>, <item>)` -> `<list_var>.append(<item>)`
*   `akhri_ko_nikaldo(<list_var>)` -> `<list_var>.pop()`
*   `saja_do(<list_var>)` -> `<list_var>.sort()`

---

**13. String Operations**

*(Optional `bhai ` prefix can be used)*

*   `lowercase_krdo(<string_var>)` -> `<string_var>.lower()`
*   `uppercase_krdo(<string_var>)` -> `<string_var>.upper()`
*   `tod_dete_h(<string_var>)` -> `<string_var>.split()` (Splits by whitespace)
*   `jod_dete_h(<separator>, <iterable>)` -> `<separator>.join(<iterable>)`
*   `<string_var> ko <old> se badaldo (<new>)` -> *(Currently seems to expect 2 args in parens in transpiler, syntax might be tricky. The transpiler has `(\w+) ko (\w+) se badaldo \((.*?)\s*,\s*(.*?)\)` which translates to `string_var.replace(arg1, arg2)`. Check `example.py` if this syntax is used)*. Let's assume the intended syntax based on the translation:
    *   Bhai Lang: `bhai string_variable ko old_substring se badaldo (old_substring, new_substring)`
    *   Python: `string_variable.replace(old_substring, new_substring)`
    *   *(Example usage for this specific syntax is missing in `example.py`)*

---

**14. Type Conversions**

*(Optional `bhai ` prefix can be used)*

*   `english_main_krdo(<value>)` -> `str(<value>)`
*   `number_bnao(<value>)` -> `int(<value>)`
*   `decimal_banade(<value>)` -> `float(<value>)`
*   `sach_ya_jhut(<value>)` -> `bool(<value>)`

---

**15. File Operations**

*(Optional `bhai ` prefix can be used)*

*   `kholdo("<filename>", "<mode>")` -> `open("<filename>", "<mode>")` (Assign to a variable)
*   `padhlo(<file_handle>)` -> `<file_handle>.read()`
*   `likhlo(<file_handle>, <content_string>)` -> `<file_handle>.write(<content_string>)`
*   `band_krdo(<file_handle>)` -> `<file_handle>.close()`
*   Example: See `example.py` lines 115-126.

---

## ⚠️ Error Handling

When you run your code using `python run_bhai.py <your_file>`, if a standard Python error occurs during execution (like `NameError`, `TypeError`, `FileNotFoundError`, etc.), the script will catch it and print a message in Hinglish to help you understand the problem.

Example Error Messages:

*   `Kya kar rha h bhai.. Yarr module error h dekh ye module h <module> joh ki tune ya toh import nhi kiya ya toh install nhi hai. Ye krle 'pip install <module>'`
*   `Kya kar rha h bhai.. Yarr variable error h dekh ye variable h <variable> joh ki tune define nhi kiya hai.`
*   `Kya kar rha h bhai.. Yarr syntax error h dekh ye line no. <line> pe h: <text>`
*   `Kya kar rha h bhai.. Yarr file error h dekh ye file h <filename> joh ki tune open nhi kiya hai.`
*   `Kya kar rha h bhai.. Yarr error h dekh ye h: <error_details>`

## 📝 Example

Check out the `example.py` file included in this repository for a comprehensive demonstration of most Bhai Lang features!

```python
# Short Example:
Ab man lo naam = mang le "Bhai apna naam batao: "
bol bhai "Salaam,", naam

Agar naam ke barabar "Admin" toh:
    bol bhai "Welcome Boss!"
Nhi toh:
    bol bhai "Welcome Guest!"
```

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, new features, or find bugs:

1.  **Fork the repository.**
2.  **Create a new branch:** `git checkout -b feature/your-feature-name` or `bugfix/issue-description`.
3.  **Make your changes.** (Update the transpiler, add tests if possible).
4.  **Commit your changes:** `git commit -m "Add some feature"`
5.  **Push to the branch:** `git push origin feature/your-feature-name`
6.  **Open a Pull Request.**

Please ensure your code follows the existing style and that any new syntax is clearly documented.
