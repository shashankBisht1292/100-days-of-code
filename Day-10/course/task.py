#function with output
def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

print(format_name("somil", "bisht"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()


output2 = function_2(function_1("hELLo"))
print(output2)

#function with multiple return and docstrings
def format_name(f_name, l_name):
    """Take a first name and last name and format it to
     return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "Your did not provide a valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name ?"), input("What is your last name ?")))

