x = input()
vowels = ["A","E","I","U","Y","O","a","e","i","u","y","o"]
for i in x:
    if i in vowels:
        del i
    else:
        print(f".{i}".lower(),end="")