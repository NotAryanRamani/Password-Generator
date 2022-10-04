from symbols import UpperCase, LowerCase, Numbers, SpecialCharacters, AllCharacters
import random
password = list()

def GeneratePassword(characters):
    temp_password = list()
    random_numbers = list()
    for i in range(0, characters):
        temp_password.append(' ')
        random_numbers.append(i)

    pass_ch = random.choice(UpperCase)
    pass_ind = random.choice(random_numbers)
    temp_password[pass_ind] = pass_ch
    random_numbers.remove(pass_ind)

    pass_ch = random.choice(LowerCase)
    pass_ind = random.choice(random_numbers)
    temp_password[pass_ind] = pass_ch
    random_numbers.remove(pass_ind)

    pass_ch = random.choice(Numbers)
    pass_ind = random.choice(random_numbers)
    temp_password[pass_ind] = pass_ch
    random_numbers.remove(pass_ind)

    pass_ch = random.choice(SpecialCharacters)
    pass_ind = random.choice(random_numbers)
    temp_password[pass_ind] = pass_ch
    random_numbers.remove(pass_ind)

    while len(random_numbers)!=0:
        pass_ch = random.choice(AllCharacters)
        pass_ind = random.choice(random_numbers)
        temp_password[pass_ind] = pass_ch
        random_numbers.remove(pass_ind)

    return temp_password


userInput = input("Do you need to generate a Password? ")
if userInput.lower() == 'yes':
    characters = int(input("How many characters do you need? (between 8 & 15) "))
    password = GeneratePassword(characters)
    final_password = str()
    for i in password:
        final_password += str(i)
    print("Generated Password: ", final_password)

else:
    print("No Worries")

