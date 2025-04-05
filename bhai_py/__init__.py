import sys
from .transpiler import translate_bhai_py

_BHAI_PY_IMPORTED = False

# Store original built-in functions
original_exec = sys.modules['builtins'].exec
original_eval = sys.modules['builtins'].eval

def _transform_code(code):
    python_code = translate_bhai_py(code)
    return python_code

def _bhai_py_exec(code, globals=None, locals=None):
    python_code = _transform_code(code)
    original_exec(python_code, globals, locals)

def _bhai_py_eval(expression, globals=None, locals=None):
    python_expression = _transform_code(expression)
    return original_eval(python_expression, globals, locals)

def activate():
    global _BHAI_PY_IMPORTED
    if not _BHAI_PY_IMPORTED:
        _BHAI_PY_IMPORTED = True
        # Override built-in functions with custom versions
        sys.modules['builtins'].exec = _bhai_py_exec
        sys.modules['builtins'].eval = _bhai_py_eval
        print("Bhai_Py is now active! Write your code in Bhai_Py syntax.")
