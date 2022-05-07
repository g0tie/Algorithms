
def hashFunc(str):
    return sum([ord(str[i].lower()) ** 3 + ord(str[i].upper()) for i in range(len(str))]) % 1000000


def makeHashTable(keys, values):
    hashTable = [0] * 1000000
    
    for i in range(len(keys)):
        key = keys[i]
        val = values[i]
        
        index = hashFunc(key) 
        hashTable[index] = val
    
    return hashTable
        
        
extensions = ["jpeg", "pdf", "svg", "ppt", "zip", "mpeg"]
mimeType = ["image/jpeg", "txt/pdf", "image/svg+xml", "application/vnd.ms-powerpoint","application/zip", "video/mpeg"]    

hashTable = makeHashTable(extensions, mimeType)
search = "svg" 

print("Generated hash: {}".format(hashFunc(search))	)
print("Corresponding mime Type: {}".format(hashTable[hashFunc(search)]))
