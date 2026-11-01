 
low, high = 1, 100 
 
print("Think of a number between 1 and 100.") 
print("Reply with higher, lower, or correct.") 
 
while low <= high: 
    guess = (low + high) // 2 
    print("Agent guesses:", guess) 
 
    feedback = input("Your feedback: ").lower() 
 
    if feedback == "correct": 
        print("Agent guessed the number!") 
        break 
    elif feedback == "higher": 
        low = guess + 1 
    elif feedback == "lower": 
        high = guess - 1 
    else: 
        print("Enter higher, lower, or correct.") 
else: 
    print("Inconsistent feedback!")
