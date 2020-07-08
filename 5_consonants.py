str = input("Enter a string")
vowels = ["a","e","i","o","u"]
for i in str:
    if i not in vowels:
        str = str.replace(i,"")
print(str)