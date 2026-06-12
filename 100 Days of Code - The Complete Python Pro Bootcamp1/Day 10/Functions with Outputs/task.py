def format_name(f_name,l_name):
    # f_name = input("Please enter your first name: ")
    # l_name = input("Please enter your last name: ")
    firstname = f_name.title()
    lastname = l_name.title()
    formatted_name = firstname + " " + lastname
    return formatted_name

print(format_name("abhineet","mitra"))
