# Collatz Conjecture | By Tredon Austin
# Quick exercise for the well known Collatz Conjecture problem. Going to do
# an initial implementation and then updating if there's a more optimal
# solution.

def collatzConjecture(num):
    if num == 1:
        return 0
    else:
        if num % 2 == 0:
            return 1 + collatzConjecture(num / 2)
        return 1 + collatzConjecture((num * 3) + 1)

userInput = input("Please enter the number that you would like to know the" +
                  " solution to the Collatz Conjecture for: ")
while not (int(userInput) % 1 == 0) or not (userInput.isdigit()):
    print("Input Invalid! Please enter a whole number greater than 0: ")
answer = collatzConjecture(int(userInput))
print("The number of steps that your number takes is " + str(answer))
