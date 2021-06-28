# first

input = "racecar"
input2 = "nada"


def palindromo_checker(input):
    print(input)
    return input == input[::-1]




if __name__ == '__main__':
    print(palindromo_checker(input))
    print(palindromo_checker(input2))
