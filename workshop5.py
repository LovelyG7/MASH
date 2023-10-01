import random

def guess_random_number(tries,start,stop):
    target = random.randint(start,stop)
    while tries != 0:
        print("Number of tries remaining is ", tries)
        guess = int(input("Guess the number: "))

        if guess == target: 
            print("You guessed it!")
            break
        elif guess < target:
            print("Guess Higher!")
        elif guess > target:
            print("Guess lower!")
        tries -= 1
        
    print("You did not get it. No more tries. The target was: ", target)

#guess_random_number(3,0,10)

def guess_random_num_linear(tries,start,stop):
    ran = random.randint(start,stop)
    for i in range(start,stop):
        print("The program is guessing...",i)
        print("Number of tries left is", tries)
        tries -=1
        if i == ran:
            print("You found the target!")
            return i 
        if tries == 0:
            print("You ran out of tries!")
            break
    
#x = guess_random_num_linear(5,0,10) 
#print(x)   

def guess_random_num_binary(tries, start,stop):
    goal = random.randint(start,stop)
    print("Random number to find: ", goal)
    lower_bound = start
    upper_bound = stop
    while tries: 
        tries -= 1
        pivot = (lower_bound+upper_bound)//2
        if pivot == goal: 
            print("You found the target!",goal)
            return pivot
        if pivot > goal: 
            upper_bound = pivot
            print("Guessing higher")
        else: 
            lower_bound = pivot
            print("Guessing lower")
    print("Your program failed to find the number")
    return -1
#guess_random_num_binary(5,5,25)