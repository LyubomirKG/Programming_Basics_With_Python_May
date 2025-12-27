# Simple login authentication system
stored_username = input()
stored_password = input()

# Initial attempt to enter the password
attempted_password = input()

# Repeat until the input matches the stored credential
while attempted_password != stored_password:
    attempted_password = input()

# Successful login message
print(f"Welcome {stored_username}!")
