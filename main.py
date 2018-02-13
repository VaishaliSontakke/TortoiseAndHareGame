from animal import  Animal
from hare import hare
from tortoise import tortoise
from random_num import RandomNum


def main():
    max_steps = 10
    tortoise1 = tortoise()
    hare1 = hare()
    rand = RandomNum()
    animal_hare = Animal(hare1)
    animal_tor = Animal(tortoise1)

    print("Game Started !")
    print("Hare  Tortoise Random_num")
    counter = 0
    rand_num = rand.random_num()

    while(not (hare1.is_reached(max_steps) or tortoise1.is_reached(max_steps))):
        counter += 1
        animal_tor.walk()
        #Game to play walk and food
        if counter == rand_num:
            animal_hare.food()
            print(str(hare1.countsteps) + "    " + str(tortoise1.countsteps) + "    " + str(rand_num) + "  " + str(counter))
            rand_num = rand.random_num()
            counter = 0
            continue

        animal_hare.walk()
        print(str(hare1.countsteps) + "    " + str(tortoise1.countsteps) + "    " + str(rand_num) + "  " + str(counter))

    if (hare1.countsteps >= max_steps):
        print "hare is winner "
    elif (tortoise1.countsteps >= max_steps):
        print "tortoise is winner"

if __name__ == "__main__":
    main()
