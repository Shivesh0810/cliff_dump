import random as r

print(" NUMBER GUESSING GAME ")
print("Insturctions: \n 1) The final number should be greater than the initial number")
print(" 2) Your guess should be in the given range \n 3) Your initial number cannot be equal to final number")
print(" 4) The values you enter should be in integer form")

try:
    i = int(input("Enter initial = "))
    f = int(input("Enter final = "))

    if (i > f) or (i == f):
        print("Please follow the given instructions")
        exit()

    pc_guess = r.randint(i, f)
    while True:
        guess = int(input("Enter your guess = "))
        if guess == pc_guess:
            print("CONGRATS, YOU FOUND THE NUMBER!")
            break
        elif guess < i:
            print(f"The number is between the range {i} and {f}")
            continue
        elif guess > f:
            print(f"The number is between the range {i} and {f}")
            continue
        elif guess > pc_guess:
            print(f"Hint - The number is between {i} and {guess}")
        elif guess < pc_guess:
            print(f"Hint - The number is between {guess} and {f}")

except ValueError:
    print("Please follow the given instructions")