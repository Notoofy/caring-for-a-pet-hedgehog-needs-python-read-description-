from art import *
import random
import time
from threading import Timer
import sys


def game():
    print(time.ctime())
    print(
        "\033[1;33m Welcome!                                 All code writen by: 🦔"
    )
    tprint("Hedgehog Care", font="small")
    max_energy = 100
    energy = 100
    food = 10
    happiness = 100
    energy_boost = 0

    while True:
        choice = input(
            "What would you like to do?: Feed [1], Sleep [2], Find [3], Happy Wave [7] or Walk [4]? (press [5] for info about your pet, Press [6] for version info): ")
        print("_____________________________")
        print("   ")
        print("   ")

        if choice == '6':
            print("Current Version: 3")
            print("_____________________________")
            print(
                "Ver 1.2: This version added version history and pets being able to die from lose of energy. Also added cute indicator icons.  Fixed Dev Bug where you can get infinite energy by spamming sleep.  First Official Version. Color too.")
            print("__________________________________________")
            print(
                "Ver 2.0:  Added power ups like energy  boosts.  Added value 'max_energy' in correspondence to the new energy boost item.  Reduced added energy amount when sleeping.")
            print("++++++++++++++++++++++++++++++++++")
            print("Ver 2.4 (Cheat Version): Added a special cheat command which allows you to dupe all current stats.")
            print("Ver 3.0:  Added a use for happiness: 'Happy Wave'")

        if choice == '7':
            if energy <= 0:
                print("Oh NO!  Your pet has run out of \033[1;35m energy⚡ \033[1;33m and is now dying.")
                time.sleep(2)
                print(" You have not taken care of your pet and now it is dead.")
                sys.exit()
            if happiness >= 20:

                chance = random.randint(1, 2)

                if chance == 2:
                    print("Vwoom!")
                    food = food + 10
                    print("You have gained 10 \033[0;31m food🍗 \033[1;33m.")
                else:
                    happiness = happiness - 20
                    print("You didn't get anything and lost 20 \033[1;36m Happiness \033[1;33m.")
            else:
                print(f"You do not have enough \033[1;36m Happiness\033[1;33m.")
                continue

        if choice == '1':
            if energy <= 0:
                print("Oh NO!  Your pet has run out of \033[1;35m energy⚡ \033[1;33m and is now dying.")
                time.sleep(2)
                print(" You have not taken care of your pet and now it is dead.")
                sys.exit()

            eat = input('''
      What would you like to use? [1] for \033[0;32m energy 
      boost 🎉 \033[1;33m and [2] for  \033[0;31m food🍗 \033[1;33m. ''')
            if eat == "2":
                if energy >= max_energy:
                    print(
                        f"Your pet has [{energy}/{max_energy} or below] \033[1;35m energy⚡ \033[1;33m and thus is not hungry")
                    print("_____________________________")
                    print("   ")
                    print("   ")
                if energy < max_energy:
                    if food <= 0:
                        print("You have no more \033[0;31m food🍗 \033[1;33m left and thus cannot feed your pet.")
                        print(
                            "Press [3] to find more \033[0;31m food🍗 \033[1;33m .  If your \033[1;35m energy⚡ \033[1;33m goes down to 0, your pet will die!")
                        continue
                    else:
                        print("You have fed your pet!")
                        energy = energy + 20
                        print(f"Your pet now has {energy} / {max_energy} \033[1;35m energy⚡ \033[1;33m!")
                        food = food - 1
                        print(f"You now have {food} \033[0;31m food 🍗 \033[1;33m left.")

                    print("_____________________________")
                    print("   ")
                    print("   ")
            elif eat == "1":
                if energy_boost <= 0:
                    print("You do not have any \033[0;32m energy boost 🎉 \033[1;33m.")
                    print("Go find more.")
                    print("_____________________________")
                    print("   ")
                    print("   ")
                    continue
                else:
                    max_energy = max_energy + 100
                    print(
                        f"Your pet has eaten a \033[0;32m energy boost 🎉 \033[1;33m and now has {max_energy} max_energy.")
                    energy_boost = energy_boost - 1
                    print(f'You now have {energy_boost} \033[0;32m energy boost 🎉 \033[1;33m.')

        if energy <= 0:
            print("Oh NO!  Your pet has run out of \033[1;35m energy⚡\033[1;33m and is now dying.")
            time.sleep(2)
            print("You have not taken care of your pet and now it is dead.")
            sys.exit()




        elif choice == '2':
            if energy >= max_energy:
                print("Your pet is not sleepy right now.")
                print("_____________________________")
                print("   ")
                print("   ")

            else:
                print("Your pet is now feeling refreshed!")
                energy = energy + 2
                print(f"Your pet now has {energy} / {max_energy} \033[1;35m energy⚡ \033[1;33m!")
                print("_____________________________")
                print("   ")
                print("   ")

        if energy <= 0:
            print("Oh NO!  Your pet has run out of \033[1;35m energy⚡ \033[1;33m and is now dying.")
            time.sleep(2)
            print("You have not taken care of your pet and now it is dead.")
            sys.exit()





        elif choice == '4':
            print("Your pet is feeling tired.")
            energy = energy - 20
            print(
                f"Lost 20 \033[1;35m energy⚡ \033[1;33m.  {energy} / {max_energy} remaining \033[1;35m energy⚡ \033[1;33m.")
            print("_____________________________")
            print("   ")
            print("   ")

            # if happiness >= 100:
            #     print("Your pet is already happy.")
            #     print("_____________________________")
            #     print("   ")
            #     print("   ")

            if happiness >= 0:
                happiness = happiness + 10
                print(f"Your pet now has {happiness} / 100 \033[1;36m happiness❤ \033[1;33m.")
                print("_____________________________")
                print("   ")
                print("   ")
        if energy <= 0:
            print("Oh NO!  Your pet has run out of \033[1;35m energy⚡ \033[1;33m and is now dying.")
            time.sleep(2)
            print("You have not taken care of your pet and now it is dead.")
            sys.exit("Why did you let your pet die?")
        if energy <= 0:
            print("Oh NO!  Your pet has run out of \033[1;35m energy⚡ \033[1;33m and is now dying.")
            time.sleep(2)
            print("You have not taken care of your pet and now it is dead.")
            sys.exit()
        if choice == '5':
            print(f"\033[0;31m Food 🍗 \033[1;33m: {food}")
            print(f"\033[1;35m Energy ⚡ \033[1;33m: {energy} / {max_energy}")
            print(f"\033[1;36m Happiness ❤\033[1;33m : {happiness}")
            print(f"\033[0;32m Energy Boost 🎉 \033[1;33m : {energy_boost}")
            print("_____________________________")
            print("   ")
            print("   ")
        elif choice == '3':
            how_much = random.randint(1, 5)
            half_half = random.randint(1, 3)
            if half_half == 1:
                food = food + how_much
                print(f"Your pet has found {how_much} \033[0;31m food 🍗\033[1;33m!")

                print(f"You now have {food} \033[0;31m food 🍗 \033[1;33mleft!")
                print("_____________________________")
                print("   ")
                print("   ")
            if half_half == 1:
                energy_boost = energy_boost + 1
                print("Your pet has found \033[0;32m energy boost 🎉 \033[1;33m")
                print(f'You now have {energy_boost} \033[0;32m energy boost 🎉 \033[1;33m ')
                print("_____________________________")
                print("   ")
                print("   ")
            else:
                print("Your pet has not found anything for a long time and it is now very tired.  You should feed him.")
                energy = energy - 30
                print(f"Your pet now has {energy} / {max_energy} \033[1;35m energy⚡ \033[1;33m left.")
                print("_____________________________")
                print("   ")
                print("   ")
                if energy <= 0:
                    print("Oh NO!  Your pet has run out of \033[1;35m energy⚡ \033[1;33m and is now dying.")
                    time.sleep(2)
                    print("You have not taken care of your pet and now it is dead.")
                    sys.exit()


        elif choice == "0":
            energy = energy * 2
            food = food * 2
            happiness = happiness * 2
            energy_boost = energy_boost * 2
            max_energy = max_energy * 2

            print("Duped everything.")
            print("")
            print("__________________")


game()