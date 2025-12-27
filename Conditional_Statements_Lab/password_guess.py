# Input: user-provided password string
password = input()

# Identity verification logic
# Note: String comparison is case-sensitive
if password == "s3cr3t!P@ssw0rd":
    print('Welcome')
else:
    # Action taken if the credentials do not match
    print("Wrong password!")
