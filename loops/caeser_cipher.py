option = input("Enter e for encryption or d for decryption: ")
if option == "e":
    message = input("Enter your message here : ")
    shift_amount = int(input("Enter shift amount : "))
    new_message = ""
    for character in message:
        if "z" > character > "a":
            pos = ord(character) - ord("a")
            pos = (pos + shift_amount) % 26
            new_character = chr(pos + ord("a"))
            new_message = new_message + new_character
        elif "Z" > character > "A":
            pos = ord(character) - ord("A")
            pos = (pos + shift_amount) % 26
            new_character = chr(pos + ord("A"))
            new_message = new_message + new_character
        else:
            new_message += character
    print(new_message)

elif option == "d":
    message = input("Enter your encrypted message here : ")
    shift_amount = int(input("Enter shift amount : "))
    new_message = ""
    for character in message:
        if "z" > character > "a":
            pos = ord(character) - ord("a")
            pos = (pos - shift_amount) % 26
            new_character = chr(pos + ord("a"))
            new_message = new_message + new_character
        elif "Z" > character > "A":
            pos = ord(character) - ord("A")
            pos = (pos - shift_amount) % 26
            new_character = chr(pos + ord("A"))
            new_message = new_message + new_character
        else:
            new_message += character
    print(new_message)