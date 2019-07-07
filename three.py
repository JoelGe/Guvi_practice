vowels=('a','e','i','o','u','A','E','I','O','U')
usr=input("Input : ")
print("Output :")
if (usr>='a' and usr<='z') or (usr>='A' and usr<='Z'):
    if usr in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
