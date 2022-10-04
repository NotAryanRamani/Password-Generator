UpperCase = \
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
string = str()
for ch in UpperCase:
    string += ch
LowerCase = list(string.lower())
Numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
SpecialCharacters = ['@', '/', '$', '&', '!']
AllCharacters = UpperCase + LowerCase + Numbers + SpecialCharacters
