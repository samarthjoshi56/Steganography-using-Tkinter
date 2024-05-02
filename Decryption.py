def decryption(key, message):
    print("Result: ", end='')
    for i in str(message):
        print(chr(ord(i) - key), end='')


print("Enter the key: ")
key = int(input())
print("Decryption the hidden data: ")
message = input()
decryption(key, message)
