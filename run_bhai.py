import sys
import bhai_py

if len(sys.argv) != 2:
    print("Usage: python run_bhai.py <bhai_py_file>")
    sys.exit(1)

# Read the Bhai_Py file
bhai_file = sys.argv[1]
with open(bhai_file, 'r', encoding='utf-8') as file:
    bhai_code = file.read()

# Translate and execute the code
python_code = bhai_py.translate_bhai_py(bhai_code)
# print("Translated Python code:")
# print(python_code)

# Execute the translated code with error handling
try:
    exec(python_code)
except ImportError as e:
    # ANSI escape code for red text
    print("\033[91mKya kar rha h bhai.. Yarr module error h dekh ye module h", e.name, "joh ki tune ya toh import nhi kiya ya toh install nhi hai. Ye krle 'pip install", e.name + "'\033[0m")
except NameError as e:
    # Handle undefined variable errors
    print("\033[91mKya kar rha h bhai.. Yarr variable error h dekh ye variable h", e.name, "joh ki tune define nhi kiya hai.\033[0m")
except SyntaxError as e:
    # Handle syntax errors
    print("\033[91mKya kar rha h bhai.. Yarr syntax error h dekh ye line no.", e.lineno, "pe h:", e.text, "\033[0m")
except TypeError as e:
    # Handle type errors
    print("\033[91mKya kar rha h bhai.. Yarr type error h dekh ye h:", e, "\033[0m")
except ValueError as e:
    # Handle value errors
    print("\033[91mKya kar rha h bhai.. Yarr value error h dekh ye h:", e, "\033[0m")
except FileNotFoundError as e:
    # Handle file not found errors
    print("\033[91mKya kar rha h bhai.. Yarr file error h dekh ye file h", e.filename, "joh ki tune open nhi kiya hai.\033[0m")
except Exception as e:
    # Handle any other unexpected errors
    print("\033[91mKya kar rha h bhai.. Yarr error h dekh ye h:", e, "\033[0m")