import random
import string
def pass_generator(length, letters=True, digits=True,symbols=True):
    characters=''
    if letters:
        characters+=string.ascii_letters
    if digits:
        characters+=string.digits
    if symbols:
        characters+=string.punctuation

    if not characters:
        return "No characters types selected."
    return ''.join(random.choice(characters) for _ in range(length))

length=int(input("enter password lenght: "))
letters=input("Include letters? (y/n): ").lower()=='y'
digits=input("Include digits? (y/n): ").lower()=='y'
symbols=input("Include symbols? (y/n): ").lower()=='y'
print("Generated Password: ", pass_generator(length, letters, digits, symbols))
