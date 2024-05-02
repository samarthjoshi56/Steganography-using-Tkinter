def encryption(key, message):
    print("Result: ", end='')
    for i in str(message):
        print(chr(ord(i) + key), end='')


print("Enter the key: ")
key = int(input())
print("Enter the message to hide: ")
message = input()
encryption(key, message)
