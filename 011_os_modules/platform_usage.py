import os

print(os.getcwd())
system = os.uname().sysname

if system == "Darwin":
    print("Mac User")
elif system == "Linux":
    print("Linux user")
else:
    print("Windows user")
