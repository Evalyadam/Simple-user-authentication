from name_ask import name_get
from name_ask import name_clear


logged = False

name_get()  # Call the specific function from name_ask

logged = True

if logged:
    print("Successfully logged in")
log_out_choice = input("Would you like to log out? (y/n)")

if log_out_choice.lower() == "y":
    name_clear()
    print("Successfully logged out.")

elif log_out_choice.lower() == "n":
    print("ok, i wont log you out :)")