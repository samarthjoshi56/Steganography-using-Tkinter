def TextToText_Encryption(text, message):
    message = "".join(format(ord(i), "08b") for i in str(message))
    midpoint = int((len(text) / 2) // 1)

    result = ""
    for i in list(str(message)):
        if i == "0":
            result += "\u200b"
        elif i == "1":
            result += "\u200c"
        else:
            result += ""
    print(text[:midpoint] + result + text[midpoint:])


print("Enter the cover text: ")
text = input()
print("Enter the text to hide: ")
message = input()
TextToText_Encryption(text, message)
