string = input("Enter your string here : ")

is_palindrome = True
new_string = string.replace(" ", "")
new_string2 = new_string.replace("!", "")
for i in range(0, len(new_string2.lower()) // 2):
    if new_string2[i] != new_string2[len(new_string2) - i - 1]:
        is_palindrome = False

if is_palindrome:
    print("Palindrome")

else:
    print("Not Palindrome")
