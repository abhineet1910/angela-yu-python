def format_name(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("what is your first name "), input("what is your last name ")))

