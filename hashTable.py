def hashFunc(str):
    return sum([ord(str[i]) for i in range(len(str))]) % 100


print(hashFunc("github"));
