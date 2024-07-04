import re
def password_complexity_checker(password):
    requirements ={ 'length':8 ,'uppercase':1 ,'lowercase':2, 'special_character':1}
    if len(password) < requirements['length']:
        return False
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"\d",password):
        return False
    if not re.search(r"\W",password):
        return False
    return True
password = str(input("enter the string: "))
if password_complexity_checker(password):
    print("the password is strong")
else:
    print("the password is weak")