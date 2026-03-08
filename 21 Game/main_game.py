import math

def PlayerStarts(current_number,number_list):
    while True:
        if current_number + 1 == 21:
                return(0)
        else:
            print(f"Current numbers: \n{number_list}")
            no_of_numbers = int(input("How many numbers you want to enter? "))
            for x in range(no_of_numbers):
                number = int(input("Write your number "))
                if number < current_number:
                    return(0)
                elif (current_number+1)!=number:
                    return(0)
                else:
                    current_number = number
                    number_list.append(number)
                    x+=1
        print("Computers turn")
        if current_number+1 == 21:
            return(1)
        else:
            comp = 4-no_of_numbers
            for x in range(comp):
                current_number +=1
                number_list.append(current_number)
                x+=1


current_number = 0
number_list = []

print("21 Game")
print("Do you want to be first or the second player?")
start = input("To be first player type '1' to be second player type '2' write any other number to quit ")
if start == '1':
    game = PlayerStarts(current_number, number_list)
    if game == '1':
        print("You won!")
    else:
        print("You lost!")
elif start == 2:
    print('gaga')
else:
    print("Pa pa")
    quit()
