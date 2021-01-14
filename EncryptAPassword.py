password = input("Enter Password: ")

new_password = ""

password_length = len(password)

for x in range(0, password_length):
    ascii = ord(password[x])
    ascii = ascii + 1

    if ascii > 90:
        ascii = ascii -26

    new_password = new_password+chr(ascii)

print(new_password)
