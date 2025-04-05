# -------- PyBhai Example (Based on Provided Translator) --------

# Import karna hai math ko root nikalne ke liye
Bhai math la

# Kuch variables set karte hain
Ab man lo student_name = "Raju"
Ab man lo marks = 78.3
Ab man lo numbers = [15, -5, 10, 25, -1]
Ab man lo message_str = " PyBhai Rocks "

# Screen pe print karte hain
bol bhai "Student ka Naam:", student_name
bol bhai "Marks:", marks
bol bhai "Number list:", numbers

# User se input lete hain
Ab man lo city = mang le "Aapka shehar kaunsa hai? "
bol bhai "Aap", city, "se ho."

# If/Else logic check karte hain
bol bhai "--- Conditions Check ---"
Agar marks se bada 75 toh:
    bol bhai student_name, "pass ho gaya Distinction ke saath!"
maggar marks se bada 40 toh:
    bol bhai student_name, "pass ho gaya."
Nhi toh:
    bol bhai student_name, "ko aur mehnat karni padegi."

# Logical operators ka istemal
Agar marks se bada 70 aur city ke barabar "Delhi" toh:
    bol bhai "Delhi ke topper ho bhai!"
Agar marks se chota 40 ya nhi (marks se bada 0) toh: # Using 'nhi' for 'not'
    bol bhai "Marks mein kuch gadbad hai ya fail ho gaye."

# While loop
bol bhai "--- While Loop ---"
Ab man lo count_down = 3
Jab tak count_down se bada 0 tab tak:
    bol bhai "T minus", count_down
    Ab man lo count_down = count_down - 1
bol bhai "Blast off!"

# For loop
bol bhai "--- For Loop ---"
bhai i ko 5 bar chakkar lagayein:
    bol bhai "Yeh chakkar number hai:", i

# Function banate hain aur call karte hain
bol bhai "--- Function ---"
Bhai calculate_bonus banate h (current_marks):
    Ab man lo bonus = current_marks * 0.1
    bol bhai "Bonus calculated:", bonus
    Bhai bonus wapis de # Return statement

Ab man lo final_bonus = calculate_bonus(marks)
bol bhai "Mila hua bonus:", final_bonus

# Class banate hain (simple)
bol bhai "--- Class ---"
Bhai class Student:
    Bhai __init__ banate h(self, name):
        Ab man lo self.name = name
    Bhai display banate h(self):
        bol bhai "Student object for:", self.name

Ab man lo s1 = Student(student_name)
s1.display()

# List operations
bol bhai "--- List Operations ---"
bol bhai "Original numbers:", numbers
bol bhai "Total numbers:", bhai count_kro(numbers)
bol bhai "Sabka total (sum):", bhai mila(numbers)
bhai dalde(numbers, 50) # Append 50
bol bhai "50 dalne ke baad:", numbers
bhai saja_do(numbers) # Sort
bol bhai "Sajane (sort) ke baad:", numbers
Ab man lo last_num = bhai akhri_ko_nikaldo(numbers) # Pop
bol bhai "Akhri nikala:", last_num
bol bhai "Ab bache numbers:", numbers
bol bhai "Sabse chota number:", bhai chota_no_dhond(numbers) # min()
bol bhai "Sabse bada number:", bhai bada_no_dhond(numbers) # max()

# String operations
bol bhai "--- String Operations ---"
bol bhai "Original message:", message_str
bol bhai "Lowercase mein:", bhai lowercase_krdo(message_str)
bol bhai "Uppercase mein:", bhai uppercase_krdo(message_str)
Ab man lo words = bhai tod_dete_h(message_str) # split
bol bhai "Shabdon mein toda:", words
# Note: The translator's jod_dete_h might be basic. Assuming it joins without separator
# bol bhai "Shabdon ko joda:", bhai jod_dete_h(words) # join (use with caution)

# Built-in function wrappers
bol bhai "--- Built-in Wrappers ---"
Ab man lo negative_marks = -85.6
bol bhai negative_marks, "ka sign hatake:", bhai sign_hatao(negative_marks) # abs()
bol bhai negative_marks, "ko round karke:", bhai no_ko_ghumao(negative_marks) # round()
bol bhai "100 ka square root:", bhai root_nikalo(100) # math.sqrt()

# Type conversions
bol bhai "--- Type Conversions ---"
Ab man lo marks_string = bhai english_main_krdo(marks) # float to string
bol bhai "Marks string mein:", marks_string
Ab man lo integer_marks = bhai number_bnao(marks) # float to int
bol bhai "Marks integer mein:", integer_marks
Ab man lo marks_float_again = bhai decimal_banade(integer_marks) # int to float
bol bhai "Marks wapis float mein:", marks_float_again
bol bhai "Kya 0 sach hai?", bhai sach_ya_jhut(0) # bool()
bol bhai "Kya 1 sach hai?", bhai sach_ya_jhut(1) # bool()

# Exception handling and File operations
bol bhai "--- File Ops & Exceptions ---"
Bhai try:
    Ab man lo file_handle = bhai kholdo("my_pybhai_file.txt", "w") # open for writing
    bhai likhlo(file_handle, "Yeh PyBhai se likha hai.\n") # write
    bhai likhlo(file_handle, city + " shehar se.\n")
    bhai band_krdo(file_handle) # close
    bol bhai "File 'my_pybhai_file.txt' mein likh diya."

    Ab man lo file_handle = bhai kholdo("my_pybhai_file.txt", "r") # open for reading
    Ab man lo content = bhai padhlo(file_handle) # read
    bol bhai "File se padha:"
    bol bhai content
    bhai band_krdo(file_handle) # close

    # Trying to read a non-existent file to trigger except
    bol bhai "Ab ek non-existent file kholne ki koshish..."
    Ab man lo f_error = bhai kholdo("nahi_hai.txt", "r")
    bhai band_krdo(f_error)

Bhai except FileNotFoundError: # Specific exception
    bol bhai "Oops! File mili nahi bhai."
Bhai except Exception: # Generic exception for others
    bol bhai "File operation mein koi aur error aa gaya!"
Bhai finally:
    bol bhai "File operations ka block khatam hua."


bol bhai "------ Program Execution Finished ------"