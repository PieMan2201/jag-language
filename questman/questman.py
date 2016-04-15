import os as OSMODULE

def clear():
    OSMODULE.system('cls' if OSMODULE.name == 'nt' else 'clear')
import random as RANDOMMODULE
import time as TIMEMODULE
print "----"
print "We recommend you set your 'clear' setting to 1 for this game."
print "----"
name = input("What is your name? ")
print name + ", you are on a quest."
print "You do not know where you are going."
health = 20
fullHealth = health
fullDodge = 5
fullAttack = 10
food = 2
time = 0
print "You will now begin your quest."
scene1 = open('./scene1.txt').read()
scene2 = open('./scene2.txt').read()
scene3 = open('./scene3.txt').read()
scene4 = open('./scene4.txt').read()
scene5 = open('./scene5.txt').read()
raw_input("Press enter to continue . . . ")
clear()
score = 0
while 1 == 1:
    random = RANDOMMODULE.randint(1,9)
    stay = 1
    while stay == 1:
        status = "Good"
        currentTime = str(time)
        print "Time: " + currentTime
        if health < fullHealth:
            if food > 0:
                diffHealth = fullHealth - health
                if diffHealth > 1:
                    diffHealth = 1

                if diffHealth > food:
                    diffHealth = food

                health = health + diffHealth
                food = food - diffHealth


        if health == fullHealth:
            if food > 0:
                diffFood = 0.2
                if diffFood > food:
                    diffFood = food

                food = food - diffFood


        if food == 0:
            status = "Hungry"
            health = health - 0.4

        if health < 5:
            status = "Weak"
            if health < 2:
                status = "Very Weak"


        if health < 0.1:
            print "You have died."
            score = str(score)
            print "Score: " + score
            raise SystemExit

        stringHealth = str(health)
        stringFullHealth = str(fullHealth)
        healthString = stringHealth + "/"
        healthString = healthString + stringFullHealth
        print "Health: " + healthString
        stringFood = str(food)
        print "Food: " + stringFood
        print "Status: " + status
        if random < 7:
            print scene1
            print "There is nothing here. You can [continue] or [stop]."
            choice = input("What do you do? ")
            if choice == "continue":
                print "Okay."
                stay = 0

            if choice != "continue":
                print "Interesting."


        if random == 7:
            print scene2
            print "A local asks you for help with something."
            yesno = input("Do you accept? ")
            if yesno == "y":
                score = score + 1
                questIntro = "He wants you to "
                questChoice = RANDOMMODULE.randint(1,3)
                attackUpgrade = 0
                dodgeUpgrade = 0
                healthUpgrade = 0
                if questChoice == 1:
                    menialTask = RANDOMMODULE.randint(1,3)
                    if menialTask == 1:
                        print questIntro + "brush his teeth."

                    if menialTask == 2:
                        print questIntro + "pick some flowers."

                    if menialTask == 3:
                        print questIntro + "find some dirt."

                    enterTimes = RANDOMMODULE.randint(10,20)
                    stringEnterTimes = str(enterTimes)
                    stringEnterTimes = stringEnterTimes + " times."
                    print "Press enter " + stringEnterTimes
                    while enterTimes > 0:
                        raw_input("Press enter to continue . . . ")
                        TIMEMODULE.sleep(0.4)
                        enterTimes = enterTimes - 1

                    healthUpgrade = RANDOMMODULE.randint(1,2)

                if questChoice == 2:
                    print questIntro + "solve some math problems."
                    numProbs = RANDOMMODULE.randint(5,15)
                    stringProbs = str(numProbs)
                    stringProbs = stringProbs + " problems."
                    print "You must solve " + stringProbs
                    while numProbs > 0:
                        num1 = RANDOMMODULE.randint(1,20)
                        num2 = RANDOMMODULE.randint(1,20)
                        opChoice = RANDOMMODULE.randint(1,3)
                        if opChoice == 1:
                            operator = " + "
                            solution = num1 + num2

                        if opChoice == 2:
                            operator = " - "
                            solution = num1 - num2

                        if opChoice == 3:
                            operator = " * "
                            solution = num1 * num2

                        probString = str(num1)
                        probString = probString + operator
                        num2String = str(num2)
                        probString = probString + num2String
                        print probString
                        answer = input("Solution: ")
                        if answer != solution:
                            print "You have failed."
                            break

                        numProbs = numProbs - 1

                    if numProbs == 0:
                        attackUpgrade = 2
                        dodgeUpgrade = 3


                if questChoice == 3:
                    print questIntro + "kill a wild animal."
                    enemyHealth = RANDOMMODULE.randint(5,15)
                    enemyAttack = RANDOMMODULE.randint(3,6)
                    enemyDodge = RANDOMMODULE.randint(1,2)
                    while enemyHealth > 0:
                        clear()
                        print "WILD ANIMAL:"
                        print enemyHealth
                        print enemyAttack
                        print enemyDodge
                        print "YOU:"
                        print health
                        print fullAttack
                        print fullDodge
                        print "You can [attack] or [defend]."
                        action = input("What do you do? ")
                        if action == "attack":
                            enemyDChance = RANDOMMODULE.randint(0,enemyDodge + 5)
                            enemyDChance2 = enemyDChance + 1
                            if enemyDodge > enemyDChance:
                                print "The enemy dodged your blow."

                            if enemyDodge < enemyDChance2:
                                print "Your blow was delivered."
                                enemyHealth = enemyHealth - fullAttack


                        if action != "attack":
                            print "You succeed in not hurting the enemy."

                        enemyAChance = RANDOMMODULE.randint(0,1)
                        if enemyAChance == 0:
                            print "The enemy chose not to attack."

                        if enemyAChance == 1:
                            print "The enemy attacked."
                            dChance = RANDOMMODULE.randint(0,fullDodge + 5)
                            dChance2 = dChance + 1
                            if fullDodge > dChance:
                                print "You dodged its blow."

                            if fullDodge < dChance2:
                                print "It hit you."
                                health = health - enemyAttack


                        if health < 0.1:
                            print "You died in battle."
                            score = str(score)
                            print "Score: " + score
                            raise SystemExit

                        raw_input("Press enter to continue . . . ")

                    attackUpgrade = 3
                    dodgeUpgrade = 2

                print "You have developed your skills."
                stringAttackUp = str(attackUpgrade)
                stringDodgeUp = str(dodgeUpgrade)
                stringHealthUp = str(healthUpgrade)
                print "Health up: " + stringHealthUp
                print "Evasiness up: " + stringDodgeUp
                print "Attack up: " + stringAttackUp
                fullAttack = fullAttack + attackUpgrade
                fullDodge = fullDodge + dodgeUpgrade
                fullHealth = fullHealth + healthUpgrade
                score = score + 1
                raw_input("Press enter to continue . . . ")

            if yesno != "y":
                print "Okay."
                stay = 0

            stay = 0

        if random == 8:
            print scene4
            print "You found some food!"
            foodChoice = RANDOMMODULE.randint(1,3)
            if foodChoice == 3:
                foodAmount = RANDOMMODULE.randint(1,5)
                stringFoodAmount = str(foodAmount)
                print stringFoodAmount + " food, to be exact."
                food = food + foodAmount

            if foodChoice != 3:
                print "Sadly, it is inedible."

            stay = 0
            raw_input("Press enter to continue . . . ")

        if random == 9:
            print scene3
            print "You have encountered a monster."
            print "You can [fight] it or attempt to [sneak] around."
            fightOrSneak = input("What do you try? ")
            if fightOrSneak == "sneak":
                sneakAttempt = RANDOMMODULE.randint(1,2)
                if sneakAttempt == 1:
                    print "You succeed in sneaking around the monster."

                if sneakAttempt == 2:
                    print "The monster notices you."
                    fightOrSneak = "fight"

                raw_input("Press enter to continue . . . ")

            if fightOrSneak != "sneak":
                print "Prepare to fight."
                TIMEMODULE.sleep(1)
                monsterChoice = RANDOMMODULE.randint(1,3)
                if monsterChoice == 1:
                    monster = "Ogre"
                    enemyHealth = RANDOMMODULE.randint(15,25)
                    enemyAttack = RANDOMMODULE.randint(1,4)
                    enemyDodge = RANDOMMODULE.randint(0,1)

                if monsterChoice == 2:
                    monster = "Red Sheep"
                    enemyHealth = RANDOMMODULE.randint(10,15)
                    enemyAttack = RANDOMMODULE.randint(9,14)
                    enemyDodge = RANDOMMODULE.randint(3,7)

                if monsterChoice == 3:
                    monster = "Bat"
                    enemyHealth = RANDOMMODULE.randint(7,12)
                    enemyAttack = RANDOMMODULE.randint(8,13)
                    enemyDodge = RANDOMMODULE.randint(5,10)

                while enemyHealth > 0:
                    clear()
                    print monster + ":"
                    print enemyHealth
                    print enemyAttack
                    print enemyDodge
                    print "YOU:"
                    print health
                    print fullAttack
                    print fullDodge
                    print "You can [attack] or [defend]."
                    action = input("What do you do? ")
                    if action == "attack":
                        enemyDChance = RANDOMMODULE.randint(0,enemyDodge + 5)
                        enemyDChance2 = enemyDChance + 1
                        if enemyDodge > enemyDChance:
                            print "The enemy dodged your blow."

                        if enemyDodge < enemyDChance2:
                            print "Your blow was delivered."
                            enemyHealth = enemyHealth - fullAttack


                    if action != "attack":
                        print "You succeed in not hurting the enemy."

                    enemyAChance = RANDOMMODULE.randint(0,1)
                    if enemyAChance == 0:
                        print "The enemy chose not to attack."

                    if enemyAChance == 1:
                        print "The enemy attacked."
                        dChance = RANDOMMODULE.randint(0,fullDodge + 5)
                        dChance2 = dChance + 1
                        if fullDodge > dChance:
                            print "You dodged its blow."

                        if fullDodge < dChance2:
                            print "It hit you."
                            health = health - enemyAttack


                    if health < 0.1:
                        print "You died in battle."
                        score = str(score)
                        print "Score: " + score
                        raise SystemExit

                    raw_input("Press enter to continue . . . ")

                print "You defeated the monster successfully."
                print "You keep its flesh and use it as food."
                food = food + 1
                score = score + 1
                raw_input("Press enter to continue . . . ")

            stay = 0

        time = time + 2
        if time == 12:
            clear()
            print scene5
            print "It is dark now."
            sleepChoice = input("Would you like to sleep? ")
            if sleepChoice == "y":
                print "Sleeping..."
                score = score + 1
                count = 0
                while health < fullHealth:
                    diffHealth = fullHealth - health
                    if diffHealth > 1:
                        diffHealth = 1

                    health = health + diffHealth
                    count = count + diffHealth
                    if count > 2:
                        break


                time = 0
                TIMEMODULE.sleep(5)

            if sleepChoice != "y":
                print "Okay then."


        if time == 24:
            time = 0

#       if score == :
        clear()