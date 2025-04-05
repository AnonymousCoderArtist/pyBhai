import re
import math # Added because root_nikalo uses math.sqrt

def translate_bhai_py(code):
    """
    Translates Bhai Lang code to Python code.

    Args:
        code: A string containing the Bhai Lang code.

    Returns:
        A string containing the translated Python code.
    """
    if isinstance(code, bytes):
        code = code.decode('utf-8')
    elif not isinstance(code, str):
        raise TypeError("code must be a string or bytes")

    # --- Remove comments first ---
    # Remove lines that are only comments
    code = re.sub(r'^\s*#.*$', '', code, flags=re.MULTILINE)
    # Remove end-of-line comments
    code = re.sub(r'\s+#.*$', '', code, flags=re.MULTILINE)

    # Import statements
    code = re.sub(r'Bhai (\w+) la', r'import \1', code, flags=re.IGNORECASE)
    code = re.sub(r'Bhai (\w+) ko (\w+) bulate h', r'import \1 as \2', code, flags=re.IGNORECASE)

    # Variable declarations (Allow word characters and dots in the name part)
    code = re.sub(r'Ab man lo ([\w\.]+) = (.+)', r'\1 = \2', code)

    # --- Operator Translations (MUST be before control flow) ---
    # Logical Operations (Order matters)
    code = re.sub(r'\b(aur)\b', r' and ', code, flags=re.IGNORECASE)
    code = re.sub(r'\b(ya)\b', r' or ', code, flags=re.IGNORECASE)
    code = re.sub(r'\b(nhi)\b(?! toh:)', r' not ', code, flags=re.IGNORECASE) # Avoid matching 'Nhi toh:'

    # Comparison operations (Order matters, longer phrases first)
    code = re.sub(r' ke barabar nhi', r' != ', code, flags=re.IGNORECASE)
    code = re.sub(r' se bada ya barabar', r' >= ', code, flags=re.IGNORECASE)
    code = re.sub(r' se chota ya barabar', r' <= ', code, flags=re.IGNORECASE)
    code = re.sub(r' se bada', r' > ', code, flags=re.IGNORECASE)
    code = re.sub(r' se chota', r' < ', code, flags=re.IGNORECASE)
    code = re.sub(r' ke barabar', r' == ', code, flags=re.IGNORECASE)

    # --- Basic Statements ---
    # Print statement (uses non-greedy match for content now)
    code = re.sub(r'(bhai )?bol\s+(bhai\s+)?(.+)', r'print(\3)', code, flags=re.MULTILINE | re.IGNORECASE)

    # Input statement
    code = re.sub(r'(bhai )?mang le\s+(.+)', r'input(\2)', code, flags=re.MULTILINE | re.IGNORECASE)

    # --- Control Flow ---
    # If-elif-else statements
    code = re.sub(r'Agar\s+(.+?)\s*toh:', r'if \1:', code, flags=re.MULTILINE | re.IGNORECASE)
    code = re.sub(r'Maggar\s+(.+?)\s*toh:', r'elif \1:', code, flags=re.MULTILINE | re.IGNORECASE)
    code = re.sub(r'Nhi\s+toh:', r'else:', code, flags=re.MULTILINE | re.IGNORECASE)

    # While loop
    code = re.sub(r'Jab tak\s+(.+?)\s*tab tak:', r'while \1:', code, flags=re.MULTILINE | re.IGNORECASE)

    # For loop
    code = re.sub(r'bhai\s+(\w+)\s+ko\s+(\d+)\s+bar\s+chakkar\s+lagayein:', r'for \1 in range(\2):', code, flags=re.MULTILINE | re.IGNORECASE)

    # --- Definitions ---
    # Function definitions
    code = re.sub(r'Bhai\s+(\w+)\s+banate\s+h\s*:', r'def \1():', code, flags=re.MULTILINE | re.IGNORECASE)
    code = re.sub(r'Bhai\s+(\w+)\s+banate\s+h\s*\((.*?)\):', r'def \1(\2):', code, flags=re.MULTILINE | re.IGNORECASE) # params non-greedy

    # Class definitions
    code = re.sub(r'Bhai\s+class\s+(\w+)\s*:', r'class \1:', code, flags=re.MULTILINE | re.IGNORECASE)

    # --- Exception Handling ---
    code = re.sub(r'Bhai\s+try\s*:', r'try:', code, flags=re.MULTILINE | re.IGNORECASE)
    code = re.sub(r'Bhai\s+except\s+(\w+)\s*:', r'except \1:', code, flags=re.MULTILINE | re.IGNORECASE) # Simple exception type
    code = re.sub(r'Bhai\s+except\s*:', r'except:', code, flags=re.MULTILINE | re.IGNORECASE) # Bare except
    code = re.sub(r'Bhai\s+finally\s*:', r'finally:', code, flags=re.MULTILINE | re.IGNORECASE)

    # --- Built-in Function Wrappers / Math ---
    # Pattern: (optional prefix)?(bhai_func_name)((arg)) -> Group 3 is arg
    code = re.sub(r'(bhai )?(sign_hatao)\((.+?)\)', r'abs(\3)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(no_ko_ghumao)\((.+?)\)', r'round(\3)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(root_nikalo)\((.+?)\)', r'math.sqrt(\3)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(mila)\((.+?)\)', r'sum(\3)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(count_kro)\((.+?)\)', r'len(\3)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(chota_no_dhond)\((.+?)\)', r'min(\3)', code, flags=re.IGNORECASE) # Corrected group \2 -> \3
    code = re.sub(r'(bhai )?(bada_no_dhond)\((.+?)\)', r'max(\3)', code, flags=re.IGNORECASE) # Corrected group \2 -> \3

    # --- List Operations (as methods) ---
    # Pattern: (optional prefix)?(bhai_method_name)((list_var, arg)) -> 3=list, 4=arg
    code = re.sub(r'(bhai )?(dalde)\((.+?)\s*,\s*(.+?)\)', r'\3.append(\4)', code, flags=re.IGNORECASE)
    # Pattern: (optional prefix)?(bhai_method_name)((list_var)) -> 3=list
    code = re.sub(r'(bhai )?(akhri_ko_nikaldo)\((.*?)\)', r'\3.pop()', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(saja_do)\((.*?)\)', r'\3.sort()', code, flags=re.IGNORECASE)

    # --- String Operations (as methods) ---
    # Pattern: (optional prefix)?(bhai_method_name)((string_var)) -> 3=string
    code = re.sub(r'(bhai )?(lowercase_krdo)\((.*?)\)', r'\3.lower()', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(uppercase_krdo)\((.*?)\)', r'\3.upper()', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?(tod_dete_h)\((.*?)\)', r'\3.split()', code, flags=re.IGNORECASE) # Assumes split() with no args
    # Pattern: (optional prefix)?(jod_dete_h)((separator, iterable)) -> 3=sep, 4=iter
    code = re.sub(r'(bhai )?(jod_dete_h)\((.+?)\s*,\s*(.+?)\)', r'\3.join(\4)', code, flags=re.IGNORECASE)
    # Pattern: (prefix)? (str_var) ko (old?) se badaldo \((new?)\s*,\s*(???)\) -> 2=str, 4=old, 5=new
    # This syntax is complex, consider simplifying BhaiLang syntax for replace if needed
    code = re.sub(r'(bhai )?(\w+) ko (\w+) se badaldo \((.*?)\s*,\s*(.*?)\)\s*', r'\2.replace(\4, \5)', code, flags=re.IGNORECASE)

    # --- Type Conversions ---
    # Pattern: (optional prefix)?(bhai_func_name)((arg)) -> Group 2 is arg
    code = re.sub(r'(bhai )?english_main_krdo\((.+?)\)', r'str(\2)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?number_bnao\((.+?)\)', r'int(\2)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?decimal_banade\((.+?)\)', r'float(\2)', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?sach_ya_jhut\((.+?)\)', r'bool(\2)', code, flags=re.IGNORECASE)

    # --- File Operations ---
    # Pattern: (optional prefix)?kholdo((filename, mode)) -> 2=filename, 3=mode
    code = re.sub(r'(bhai )?kholdo\((.+?)\s*,\s*(.+?)\)', r'open(\2, \3)', code, flags=re.IGNORECASE)
    # Pattern: (optional prefix)?(file_method)((file_handle)) -> 2=handle
    code = re.sub(r'(bhai )?padhlo\((.*?)\)', r'\2.read()', code, flags=re.IGNORECASE)
    code = re.sub(r'(bhai )?band_krdo\((.*?)\)', r'\2.close()', code, flags=re.IGNORECASE)
    # Pattern: (optional prefix)?likhlo((file_handle, content)) -> 2=handle, 3=content
    code = re.sub(r'(bhai )?likhlo\((.+?)\s*,\s*(.+?)\)', r'\2.write(\3)', code, flags=re.IGNORECASE)

    # --- Return Statement ---
    code = re.sub(r'Bhai (.+?) wapis de', r'return \1', code, flags=re.IGNORECASE) # content non-greedy

    # --- Final Cleanup ---
    # Remove potential excess empty lines created by comment removal
    code = re.sub(r'\n\s*\n', '\n', code)

    return code.strip() # Remove leading/trailing whitespace from the whole code
