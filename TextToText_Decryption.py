def TextToText_Decryption(text):
    result = ""
    for i in text:
        if i == "\u200b":
            result = result + "0"
        elif i == "\u200c":
            result = result + "1"
    result = "".join(chr(int(result[i:i + 8], 2)) for i in range(0, len(result), 8))
    print(result)


text = input("Enter the text: ")
TextToText_Decryption(text)
