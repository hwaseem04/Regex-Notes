import validators

email = input("What's your email address?")

if validators.email(email) == True:
    print("Valid")
else:
    print("Invalid")
