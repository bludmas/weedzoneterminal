# /////////////////////////////////////////
# //              TERMINAL               \\
# //         WEEDZONE © 2023-2023        \\
# /////////////////////////////////////////

# ==> To add new commands, Please read instructions on modding. <==

import sys
import time
import ctypes
import random
import base64

## // SETTINGS \\
# [Version]
modded = False # change if you're modding this (big important)
vers = "1.1"
# [Balance]
credits = "0" # Cannot be changed. (overriden by a function.)
credits = int(credits)
# [User Data]
username = 'USER-3434'
if modded == True:
    username = 'USER-MOD38'
password = 'xlE3W5kd'
drunk = False
drugged = False
# [Storage]
storage = []
# [Store]
flashlightprice = 16
walkietalkieprice = 25
shovelprice = 19
dildoprice = 4
borsecprice = 2
book1 = 10
gunprice = 200
beerprice = 32
cocaineprice = 300
# //------------\\

class computer:
    # [Terminal Function]
    def terminal():
        global credits, flashlightprice, walkietalkieprice, shovelprice, dildoprice, borsecprice, book1, gunprice, beerprice, drunk, cocaineprice, modded, drugged, drunk # Add variables here
        command = input('> ')
        if command == 'help':
            print('--== COMMAND LIST ==--')
            print('> help')
            print(' (Displays Command List)')
            print('> balance (or credits)')
            print(' (Displays The Amount Of Credits)')
            print('> store')
            print('(Displays the store of available items)')
            print('> buy')
            print(' (Lets you buy stuff available in the store)')
            print('> user')
            print(' (Displays current user)')
            print('> tinfo')
            print(' (Displays info about the terminal.)')
            print('> exit')
            print(' (Closes the terminal)')
            print('> othercom')
            print(' (Displays the other commands)')
            computer.terminal()
        elif command == 'store':
            print('--== STORE ==--')
            print('Flashlight = ' + str(flashlightprice) + '$')
            print('Walkie-Talkie = ' + str(walkietalkieprice) + '$')
            print('Shovel = ' + str(shovelprice) + '$')
            print('Dildo = ' + str(dildoprice) + '$')
            print('Borsec Bottle = ' + str(borsecprice) + '$')
            print('Book on how to kill kurimoti = ' + str(book1) + '$')
            print('Gun = ' + str(gunprice) + '$')
            print('Beer = ' + str(beerprice) + '$')
            print('Cocaine = ' + str(cocaineprice) + '$')
            print('(Use the command "buy" to buy the available items.)')
            computer.terminal()
        elif command == 'buy':
            boughtitem = input('Please type the item you wish to buy --> ')
            if boughtitem == 'flashlight':
                if credits < flashlightprice:
                    print('Not enough Credits.')
                    computer.terminal()
                else:
                    print('Flashlight has been bought')
                    credits = credits - flashlightprice
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('flashlight')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
            elif boughtitem == 'walkie-talkie':
                if credits < walkietalkieprice:
                    print('Not enough Credits.')
                    computer.terminal()
                else:
                    print('Walkie-Talkie has been bought')
                    credits = credits - walkietalkieprice
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('walkie-talkie')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
            elif boughtitem == 'shovel':
                    if credits < shovelprice:
                        print('Not enough Credits.')
                        computer.terminal()
                    else:
                        print('Shovel has been bought')
                        credits = credits - shovelprice
                        with open("credits.dat", "w") as file:
                            file.write(computer.encode(credits))
                        storage.append('shovel')
                        with open("storage.dat", "w") as sfile:
                            sfile.write(computer.encode(storage))
                        print(f'Your new balance is: {credits} Credits.')
                        computer.terminal()
            elif boughtitem == 'dildo':
                    if credits < dildoprice:
                        print('Not enough Credits.')
                        computer.terminal()
                    else:
                        print('Dildo has been bought (What are you fucking doing with a dildo?)')
                        credits = credits - dildoprice
                        with open("credits.dat", "w") as file:
                            file.write(computer.encode(credits))
                        storage.append('dildo')
                        with open("storage.dat", "w") as sfile:
                            sfile.write(computer.encode(storage))
                        print(f'Your new balance is: {credits} Credits.')
                        computer.terminal()
            elif boughtitem == 'borsec bottle':
                if credits < borsecprice:
                    print('Not Enough Credits.')
                    computer.terminal()
                else:
                    print('Borsec Bottle has been bought')
                    credits = credits - borsecprice
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('borsecbottle')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal() 
            elif boughtitem == 'book on how to kill kurimoti':
                if credits < book1:
                    print('Not Enough Credits.')
                    computer.terminal()
                else:
                    print('Book On How To Kill Kurimoti has been bought')
                    credits = credits - book1
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('bookonhowtokillkurimoti')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')    
                    computer.terminal()
            elif boughtitem == 'gun':
                if credits < gunprice:
                    print('Not Enough Credits.')
                    computer.terminal()
                else:
                    print('gun has been bought')
                    credits = credits - gunprice
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('gun')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')    
                    computer.terminal()
            elif boughtitem == 'beer':
                if credits < beerprice:
                    print('Not Enough Credits.')
                    computer.terminal()
                else:
                    print('Beer has been bought')
                    credits = credits - beerprice
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('beer')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')    
                    computer.terminal()
            elif boughtitem == 'cocaine':
                if credits < cocaineprice:
                    print('Not Enough Credits.')
                    computer.terminal()
                else:
                    print('Cocaine has been bought (you sick fuck)')
                    credits = credits - cocaineprice
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    storage.append('cocaine')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print(f'Your new balance is: {credits} Credits.')    
                    computer.terminal()  
            elif boughtitem == 'cancel':
                print('Order Cancelled')
                computer.terminal()
            else:
                print(f'the "{boughtitem}" item was not found.')
                computer.terminal()
        elif command == 'balance':
            print(f'{credits} Credits')
            computer.terminal()
        elif command == 'credits':
            print(f'{credits} Credits')
            computer.terminal()
        elif command == 'user':
            print('USERNAME: ' + username)
            print('PASSWORD: ******')
            print('type "reveal" to reveal the password.')
            print('or type "back" to go back at the terminal')
            usermand = input()
            if usermand == 'reveal':
                print('PASSWORD: ' + password)
                computer.terminal()
            elif usermand == 'back':
                computer.terminal()
            else:
                computer.terminal()
        elif command == 'othercom':
            print('--== OTHER COMMANDS LIST ==--')
            print('> storage')
            print('(Displays the list of items in the storage)')
            print('> work')
            print('(Makes crew members work in exchange for money)')
            print('> buyhelp')
            print('(Displays instructions on how to buy items)')
            print('> bet')
            print('(Gamble money and pray that you win jackpot)')
            print('> rob')
            print('(Makes crew members rob a bank, a gun is required)')
            print('> sell')
            print('(Lets you sell stuff in your storage)')
            print('> use')
            print('(Lets you use stuff in your storage)')
            print('> undrunk')
            print('(Unbecome drunk)')
            print('> savecredits')
            print('(Saves your current balance)')
            print('> savestorage')
            print('(Saves your storage)')
            print('> saveall')
            print('(Saves everything, like credits and storage)')
            print('> find')
            print('(Find scrap metal and sell them in exchange for money)')
            print('> fortune')
            print('(Displays a random good/bad fortune)')
            print('> quote')
            print('(Displays a random quote)')
            print('> calculator')
            print('(calculates problems you insert.)')
            print('> call')
            print('(call people)')
            print('> drugtest')
            print('(take a drug test)')
            print('> drunktest')
            print('(take a drunk test)')
            print('> phonenumbers')
            print('(List of available phone numbers to call)')
            computer.terminal()
        elif command == 'storage':
            print('--== STORAGE ==--')
            if not storage:
                print('No items found.')
                computer.terminal()
            else:
                print('Items in storage:')
                for item in storage:
                    print(item.strip())
                computer.terminal()
        elif command == 'work':
            print('Loading...')
            print('Transporting crew members...')
            time.sleep(5)
            print('Transporting crew members... (5 km left)')
            time.sleep(5)
            print('Transporting crew members... (1 km left)')
            time.sleep(5)
            print('Destination arrived.')
            time.sleep(1)
            print('Finding Loot... (Takes about 60-120 seconds)')
            time.sleep(random.randint(60,120))
            randomnumber = random.randint(1,4)
            if randomnumber == 2:
                if storage:
                    remitem = random.choice(storage)
                    print(f'{remitem} was lost during the scavenge.')
                    storage.remove(remitem)
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
            else:
                print('No items were lost during the scavenge')
            print('Arriving back...')
            time.sleep(10)
            print('Selling Scrap...')
            time.sleep(15)
            randomcreditsn = random.randint(1,6)
            if randomcreditsn == 1:
                print('Obtained Credits:')
                randomcredits = random.randint(4,30)
                print(f'{randomcredits} Credits')
                credits = credits + randomcredits
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
            elif randomcreditsn == 2:
                print('Obtained Credits:')
                random1credits = random.randint(30,60)
                print(f'{random1credits} Credits')
                credits = credits + random1credits
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
            elif randomcreditsn == 3:
                random2credits = random.randint(60,346)
                print('Obtained Credits:')
                print(f'{random2credits} Credits')
                credits = credits + random2credits
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
            elif randomcreditsn == 4:
                random3credits = random.randint(346,912)
                print(f'{random3credits} Credits')
                credits = credits + random3credits
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
            elif randomcreditsn == 5:
                random4credits = random.randint(912,1124)
                print(f'{random4credits} Credits')
                credits = credits + random4credits
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
            else:
                print('The scrap had no value.')
            computer.terminal()
        elif command == 'buyhelp':
            print('--== BUYING HELP ==--')
            print("If you don't know how to buy items here's a tutorial on how to do it:")
            print('1. Type the command in (buy) and nothing else')
            print('2. Type a item you wish to buy')
            print('List of available items:')
            print('flashlight')
            print('walkie-talkie')
            print('shovel')
            print('dildo')
            print('borsec bottle')
            print('book on how to kill kurimoti')
            print('gun')
            print('beer')
            print('cocaine')
            print('3. Make sure you have enough credits.')
            print('4. After you bought the item, you should now see it in your storage. (type storage to see it)')
            computer.terminal()
        elif command == 'bet':
            betamount = input('Insert the amount of credits you want to bet/gamble --> ')
            try:
                betamount = int(betamount)
                if betamount > credits:
                    print('You cannot bet anything higher than your balance.')
                    computer.terminal()
                elif betamount == 0:
                    print('Your bet must be greater than 0!')
                    computer.terminal()
                elif betamount < 0:
                    print('Your bet cannot be a negative number.')
                    computer.terminal()
                else:
                    print("You have bet:", betamount, "credits.")
                    print('Gambling...')
                    time.sleep(5)
                    if betamount < 15:
                        print(f'You have lost {betamount} credits.')
                        credits = credits - betamount
                        with open("credits.dat", "w") as file:
                            file.write(computer.encode(credits))
                        print(f'Your new balance is: {credits} Credits.')
                    elif betamount > 15 and betamount < 50:
                        randomjackpot = random.randint(1,30)
                        if randomjackpot == 11:
                            randombetcredits = random.randint(1,204)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount == 15:
                        randomjackpot = random.randint(1,30)
                        if randomjackpot == 15:
                            randombetcredits = random.randint(1,204)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount > 50 and betamount < 100:
                        randomjackpot = random.randint(1,10)
                        if randomjackpot == 3:
                            randombetcredits = random.randint(103,521)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount == 50:
                        randomjackpot = random.randint(1,9)
                        if randomjackpot == 3:
                            randombetcredits = random.randint(102,521)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount > 100:
                        randomjackpot = random.randint(1,5)
                        if randomjackpot == 4:
                            randombetcredits = random.randint(321,1024)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount == 100:
                        randomjackpot = random.randint(1,6)
                        if randomjackpot == 2:
                            randombetcredits = random.randint(204,1023)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount > 1000:
                        randomjackpot = random.randint(1,3)
                        if randomjackpot == 3:
                            randombetcredits = random.randint(503,1142)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    elif betamount == 1000:
                        randomjackpot = random.randint(1,4)
                        if randomjackpot == 1:
                            randombetcredits = random.randint(494,1042)
                            print(f'You have won {randombetcredits} credits!')
                            credits = credits + randombetcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                        else:
                            print(f'You have lost {betamount} credits.')
                            credits = credits - betamount
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
            except ValueError:
                print("Invalid input.")
                computer.terminal()
        elif command == 'rob':
            if 'gun' in storage:
                print('Robbing a bank...')
                print('Transporting crew members to nearest bank available...')
                time.sleep(random.randint(5,30))
                print('Arrived')
                time.sleep(2)
                print('Rethink your choice. Are you sure you wanna do this?')
                print('Y for yes, N for no')
                print('(If you get arrested you lose money too)')
                time.sleep(2)
                rechoice = input('Choice: ')
                if rechoice == 'Y':
                    print('You chose to rob the bank.')
                    time.sleep(2)
                    print('Robbing in progress...')
                    time.sleep(random.randint(30,60))
                    arrest = random.randint(1,6)
                    if arrest == 4:
                        print('You succesfully robbed the bank.')
                        stolencredits = random.randint(503,1024)
                        print(f'Money Stolen: {stolencredits} Credits.')
                        credits = credits + stolencredits
                        print(f'Your new balance is: {credits} Credits.')
                        with open("credits.dat", "w") as file:
                            file.write(computer.encode(credits))
                        computer.terminal()
                    elif arrest == 2:
                        print('You altmost got caught but you managed to take little money.')
                        stolencredits1 = random.randint(15,113)
                        print(f'Money Stolen: {stolencredits1} Credits.')
                        credits = credits + stolencredits1
                        print(f'Your new balance is: {credits} Credits.')   
                        with open("credits.dat", "w") as file:
                            file.write(computer.encode(credits))
                        computer.terminal()
                    else:
                        print('You got caught and arrested.')
                        if credits > 0:
                            removedcredits = random.randint(1,credits)
                            print(f'You have lost {removedcredits} credits. (and your gun too)')
                            storage.remove("gun")
                            credits = credits - removedcredits
                            with open("credits.dat", "w") as file:
                                file.write(computer.encode(credits))
                            print(f'Your new balance is: {credits} Credits.')
                            computer.terminal()
                        else:
                            print('You did not lose any credits since you didnt have any') 
                            computer.terminal()               
                elif rechoice == 'N':
                    print('You decided to not rob the bank.')
                    computer.terminal()
                else:
                    print('Invalid Choice.')
                    print('Automatically selected N.')
                    computer.terminal()
            else:
                print('A gun is required to rob the bank.')
                computer.terminal()
        elif command == '(.)(.)':
            print('Boobas!')
            computer.terminal()
        elif command == 'sell':
            sellitem = input('Insert the item you wish to sell --> ')
            if sellitem == 'flashlight':
                if 'flashlight' in storage:
                    selledcredits = random.randint(1,flashlightprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('flashlight')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a flashlight!')
                    computer.terminal()
            elif sellitem == 'walkie-talkie':
                if 'walkie-talkie' in storage:
                    selledcredits = random.randint(1,walkietalkieprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('walkie-talkie')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a walkie-talkie!')
                    computer.terminal()
            elif sellitem == 'shovel':
                if 'shovel' in storage:
                    selledcredits = random.randint(1,shovelprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('shovel')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a shovel!')
                    computer.terminal()
            elif sellitem == 'dildo':
                if 'dildo' in storage:
                    selledcredits = random.randint(1,dildoprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('dildo')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a dildo! (you wish you did)')
                    computer.terminal()
            elif sellitem == 'borsecbottle':
                if 'borsecbottle' in storage:
                    selledcredits = random.randint(1,borsecprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('borsecbottle')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a borsecbottle!')
                    computer.terminal()
            elif sellitem == 'bookonhowtokillkurimoti':
                if 'bookonhowtokillkurimoti' in storage:
                    selledcredits = random.randint(1,book1)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('bookonhowtokillkurimoti')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
            elif sellitem == 'gun':
                if 'gun' in storage:
                    selledcredits = random.randint(1,gunprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('gun')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a gun!')
                    computer.terminal()
            elif sellitem == 'beer':
                if 'beer' in storage:
                    selledcredits = random.randint(1,beerprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('beer')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own a beer!')
                    computer.terminal()
            elif sellitem == 'cocaine':
                if 'cocaine' in storage:
                    selledcredits = random.randint(1,cocaineprice)
                    print(f'Selled {sellitem} for {selledcredits} credits.')
                    storage.remove('cocaine')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    credits = credits + selledcredits
                    with open("credits.dat", "w") as file:
                        file.write(computer.encode(credits))
                    print(f'Your new balance is: {credits} Credits.')
                    computer.terminal()
                else:
                    print('You do not own cocaine!')
                    computer.terminal()                
            else:
                print('Invalid Item.')
                computer.terminal()
        elif command == 'use':
            useitem = input('Insert the item you wish to use --> ')
            if useitem == 'flashlight':
                if 'flashlight' in storage:
                    print('What are you using a flashlight on?')
                    computer.terminal()
                else:
                    print('You do not own a flashlight!')
                    computer.terminal()
            elif useitem == 'walkie-talkie':
                if 'walkie-talkie' in storage:
                    print('"Hey, Mike, where are you buddy?"')
                    time.sleep(5)
                    print('"Mike?"')
                    time.sleep(3)
                    print('"Yeah.. i think hes dead."')
                    time.sleep(2)
                    computer.terminal()
                else:
                    print('You do not own a walkie-talkie!')
                    computer.terminal()
            elif useitem == 'shovel':
                if 'shovel' in storage:
                    print('You dig a hole and feel proud of it (ikea effect)')
                    computer.terminal()
                else:
                    print('You do not own a shovel!')
                    computer.terminal()
            elif useitem == 'dildo':
                if 'dildo' in storage:
                    print('Restricted Content. A access code must be entered!')
                    accesscode = input('Access Code: ')
                    if accesscode == password:
                        print('You put the dildo in your ass.')
                        print("You're now officially a weird dude")
                        computer.terminal()
                    else:
                        print('Incorrect Code')
                        computer.terminal()
                else:
                    print('You do not own a dildo! (dont buy it)')
                    computer.terminal()
            elif useitem == 'borsecbottle':
                if 'borsecbottle' in storage:
                    print('You drink the bottle. You feel hydrated.')
                    storage.remove('borsecbottle')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    if drunk == True:
                        drunk = False
                        print('You also unbecome drunk.')
                    else:
                        drunk = False
                    computer.terminal()
                else:
                    print('You do not own a borsecbottle!')
                    computer.terminal()
            elif useitem == 'bookonhowtokillkurimoti':
                if 'bookonhowtokillkurimoti' in storage:
                    print('You read the book. You are now equipped with the knowledge of killing kurimoti')
                    computer.terminal()
                else:
                    print('You do not own a bookonhowtokillkurimoti!')
                    computer.terminal()
            elif useitem == 'gun':
                if 'gun' in storage:
                    print('You practice shooting.')
                    computer.terminal()
                else:
                    print('You do not own a gun!')
                    computer.terminal()
            elif useitem == 'beer':
                if 'beer' in storage:
                    print('You become drunk')
                    drunk = True
                    storage.remove('beer')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    computer.terminal()
                else:
                    print('You do not own a beer!')
                    computer.terminal()
            elif useitem == 'peperonnipizza':
                if 'peperonnipizza' in storage:
                    storage.remove('peperonnipizza')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print('You eat the pizza. It was delicious.')
                    computer.terminal()
                else:
                    print('You do not own a peperonnipizza!')
                    computer.terminal()
            elif useitem == 'cheesepizza':
                if 'cheesepizza' in storage:
                    storage.remove('cheesepizza')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print('You eat the pizza. It was delicious.')
                    computer.terminal()
                else:
                    print('You do not own a cheesepizza!')
                    computer.terminal()
            elif useitem == 'specialpizza':
                if 'specialpizza' in storage:
                    storage.remove('specialpizza')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print('You eat the pizza. It felt.. weird.')
                    computer.terminal()
                else:
                    print('You do not own a specialpizza!')
                    computer.terminal()  
            elif useitem == 'cocaine':
                if 'cocaine' in storage:
                    storage.remove('cocaine')
                    with open("storage.dat", "w") as sfile:
                        sfile.write(computer.encode(storage))
                    print('You snort the cocaine. You are now on drugs')
                    drugged = True
                    computer.terminal()
                else:
                    print('You do not own cocaine!')
                    computer.terminal()
            else:
                print('Invalid Item.')
                computer.terminal()          
        elif command == 'undrunk':
            if drunk == False:
                print('You are not even drunk??')
                computer.terminal()
            else:
                print('You beat yourself to sleep and wake up in a fine condition')
                drunk = False
                computer.terminal()
        elif command == 'vers':
            if modded == False:
                print(f'Version: {vers}')
                computer.terminal()
            elif modded == True:
                print(f'Version: {vers} MODDED')
                computer.terminal()
            else:
                print('Version Error! (Modded is not set to False nor True.)')
                computer.terminal()
        elif command == 'sigurd':
            print('oh my god what are you doing?')
            computer.terminal()
        elif command == 'savecredits':
            with open("credits.dat", "w") as file:
                file.write(computer.encode(credits))
            print('Saved Credits.')
            computer.terminal()
        elif command == 'savestorage':
            with open("storage.dat", "w") as sfile:
                sfile.write(computer.encode(storage))
            print('Saved storage list.')
            computer.terminal()
        elif command == 'find':
            print('Finding scrap...')
            time.sleep(random.randint(1,20))
            chance = random.randint(1,15)
            if chance == 4:
                foundcredits = random.randint(1,25)
                foundcredits = int(foundcredits)
                print(f'You found scrap metal worth of {foundcredits} Credits!')
                credits = credits + foundcredits
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
                computer.terminal()
            elif chance == 1:
                foundcredits1 = random.randint(1,4)
                foundcredits1 = int(foundcredits1)
                print(f'You only found junk worth of {foundcredits1} Credits.')
                credits = credits + foundcredits1
                with open("credits.dat", "w") as file:
                    file.write(computer.encode(credits))
                print(f'Your new balance is: {credits} Credits.')
                computer.terminal()
            else:
                print('You found nothing.')
                computer.terminal()
        elif command == 'saveall':
            with open("storage.dat", "w") as sfile:
                sfile.write(computer.encode(storage))  
            with open("credits.dat", "w") as file:
                file.write(computer.encode(credits))
            print('Saved credits and storage list.')
            computer.terminal()
        elif command == '2.2.2022':
            print('-.-- --- ..- / ... .... --- ..- .-.. -.. -. .----. - / .... .- ...- . / -.. --- -. . / - .... .- - .-.-.-')
            time.sleep(0.1)
            sys.exit()
        elif command == 'fortune':
            goodorbad = random.randint(1,2)
            if goodorbad == 1:
                print('Your fortune: ' + computer.fortuner())
                computer.terminal()
            elif goodorbad == 2:
                print('Your fortune: ' + computer.goodfortuner())
                computer.terminal()
        elif command == 'quote':
            print(computer.quote())
            computer.terminal()
        elif command == 'calculator':
            computer.calculator()
            computer.terminal()
        elif command == 'tinfo':
            print('--== TERMINAL INFO ==--')
            print('Terminal is a program made by weedzone, the project started in Wednesday, December 13, 2023, at 5:38:40 PM')
            print('The program has in total of 1300+ lines of code. It has fun, secret and normal commands')
            print('Type "help" or "othercom" to see a list of them. (Total of commands : 32)')
            print('The program also features buying, selling, working for money, and you can also gamble money by using the "bet" command.')
            print('The communication server is discord.gg/VcbbKwWnTR')
            print('Fun fact: Terminal was inspired by Lethal Company.')
            computer.terminal()
        elif command == 'femboy':
            print('Are you a femboy?')
            computer.terminal()
        elif command == 'call':
            number = input('Insert number to call --> ')
            try:
                numerical = computer.hasdigits(number)
                if numerical:
                    print('Calling...')
                    time.sleep(5)
                    if number == '123 123 123':
                        print('You are now in a call with: 123 123 123')
                        time.sleep(1)
                        print('Hello?')
                        time.sleep(3)
                        print('H-hello?')
                        time.sleep(4)
                        print('Who is this?')
                        time.sleep(3)
                        print('[CALL ENDED]')
                        computer.terminal()
                    elif number == '666':
                        chance = random.randint(1,66)
                        if chance == 6:
                            print('You are now in a call with: 666')
                            time.sleep(6)
                            print('⊬⍜⎍ ⏃⍀⟒ ⎅⟒⏃⎅')
                            time.sleep(1)
                            sys.exit()
                        else:
                            print('The number you have tried to call is unavailable at this time. Please try again later')
                            computer.terminal()
                    elif number == '888':
                        print('Jesus loves everyone')
                        computer.terminal()
                    elif number == '911':
                        print('You are now in a call with: 911')
                        time.sleep(2)
                        print('911 what is your emergency?')
                        time.sleep(5)
                        print('[CALL ENDED]')
                        computer.terminal()
                    elif number == '112':
                        print('You are now in a call with: 112')
                        time.sleep(2)
                        print('112 what is your emergency?')
                        time.sleep(5)
                        print('[CALL ENDED]')
                        computer.terminal()
                    elif number == '453 234 123':
                        print('You are now in a call with: 453 234 123')
                        time.sleep(4)
                        print('Luigi Pizza what do you want to order?')
                        print('MENU:')
                        print('- Peperroni (5$)')
                        print('- Cheese (3$)')
                        print('- Special (12$)')
                        order = input('Order: ')
                        if order == 'Peperroni':
                            print('Okay sir, peperonni pizza coming right up!')
                            print('Please wait...')
                            time.sleep(15)
                            print('Peperonni pizza is done! 5 dollars please!')
                            time.sleep(2)
                            if credits < 5:
                                print('You dont have enough credits for peperonni?')
                                time.sleep(2)
                                print('Call back when you have 5 dollars!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            elif credits > 4:
                                print('Here you go sir!')
                                credits = credits - 5
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                storage.append('peperonnipizza')
                                with open("storage.dat", "w") as sfile:
                                    sfile.write(computer.encode(storage))
                                print('Enjoy your pizza!')
                                time.sleep(1)
                                print('Luigi Out!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()      
                            else:
                                print('[CALL ENDED]')
                                computer.terminal()
                        elif order == 'Cheese':
                            print('Okay sir, cheese pizza coming right up!')
                            print('Please wait...')
                            time.sleep(15)
                            print('Cheese pizza is done! 3 dollars please!')
                            time.sleep(2)
                            if credits < 3:
                                print('You dont have enough credits for cheese pizza?')
                                time.sleep(2)
                                print('Call back when you have 3 dollars!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            elif credits > 2:
                                print('Here you go sir!')
                                credits = credits - 3
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                storage.append('cheesepizza')
                                with open("storage.dat", "w") as sfile:
                                    sfile.write(computer.encode(storage))
                                print('Enjoy your pizza!')
                                time.sleep(1)
                                print('Luigi Out!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()      
                            else:
                                print('[CALL ENDED]')
                                computer.terminal()      
                        elif order == 'Special':
                            print('Special... Okay sir, one "special" pizza coming right up!')
                            print('Please wait...')
                            time.sleep(15)
                            print('Special pizza is done! 12 dollars please!')
                            time.sleep(2)
                            if credits < 12:
                                print('You dont have enough credits for special pizza?')
                                time.sleep(2)
                                print('Call back when you have 12 dollars!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            elif credits > 11:
                                print('Here you go sir!')
                                credits = credits - 12
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                storage.append('specialpizza')
                                with open("storage.dat", "w") as sfile:
                                    sfile.write(computer.encode(storage))
                                print('Enjoy your pizza!')
                                time.sleep(1)
                                print('Luigi Out!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()   
                            else:
                                print('[CALL ENDED]')
                                computer.terminal()
                        else:
                            print('We dont sell that.')
                            time.sleep(1)
                            print('[CALL ENDED]')
                            computer.terminal()                      
                    elif number == '666 666 666':
                        sys.exit()
                    elif number == '090 4444 4444':
                        time.sleep(5)
                        chance1 = random.randint(1,50)
                        if chance1 == 4:
                            print('You are now in a call with: 090 4444 4444')
                            time.sleep(3)
                            print('1週間。')
                            time.sleep(0.5)
                            print('[CALL ENDED]')
                            computer.terminal()
                        else:
                            print('The number you have tried to call is unavailable at this time. Please try again later')
                            computer.terminal()
                    elif number == '203 153 323':
                        print('You are now in a call with: 203 153 323')
                        time.sleep(2)
                        print('Tryna sell pizzas fo me?')
                        sellitem1 = input('Sell: ')
                        if sellitem1 == 'Peperonni':
                            if 'peperonnipizza' in storage:
                                print('Peperonni huh? Ill take it fam')
                                time.sleep(2)
                                storage.remove('peperonnipizza')
                                with open("storage.dat", "w") as sfile:
                                    sfile.write(computer.encode(storage))
                                selledcredits2 = random.randint(1,5)
                                credits = credits + selledcredits2
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                print(f'Selled peperonnipizza for {selledcredits2} Credits.')
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                print(f'Your new balance is: {credits} Credits.')
                                time.sleep(2)
                                print('Ay.. it was a pleasure doing business with you')
                                time.sleep(3)
                                print('Bye')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            else:
                                print('Liar, You dont have that shi fam')                   
                                time.sleep(1)
                                print('Come back when you have it')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                        elif sellitem1 == 'Cheese':
                            if 'cheesepizza' in storage:
                                print('Cheese huh? Ill take it fam')
                                time.sleep(2)
                                storage.remove('cheesepizza')
                                with open("storage.dat", "w") as sfile:
                                    sfile.write(computer.encode(storage))
                                selledcredits2 = random.randint(1,3)
                                credits = credits + selledcredits2
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                print(f'Selled cheesepizza for {selledcredits2} Credits.')
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                print(f'Your new balance is: {credits} Credits.')
                                time.sleep(2)
                                print('Ay.. it was a pleasure doing business with you')
                                time.sleep(3)
                                print('Bye')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            else:
                                print('Liar, You dont have that shi fam')                   
                                time.sleep(1)
                                print('Come back when you have it')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                        elif sellitem1 == 'Special':
                            if 'specialpizza' in storage:
                                print('Special huh? Ill take it fam')
                                time.sleep(2)
                                storage.remove('specialpizza')
                                with open("storage.dat", "w") as sfile:
                                    sfile.write(computer.encode(storage))
                                selledcredits2 = random.randint(1,11)
                                credits = credits + selledcredits2
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                print(f'Selled specialpizza for {selledcredits2} Credits.')
                                with open("credits.dat", "w") as file:
                                    file.write(computer.encode(credits))
                                print(f'Your new balance is: {credits} Credits.')
                                time.sleep(2)
                                print('Ay.. it was a pleasure doing business with you')
                                time.sleep(3)
                                print('Bye')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            else:
                                print('Liar, You dont have that shi fam')
                                time.sleep(1)
                                print('Come back when you have it')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                        else:
                            print('That doesnt exist. Fuck you')
                            time.sleep(1)
                            print('[CALL ENDED]')
                            computer.terminal()
                    elif number == '198 523 134':
                        print('You are now in a call with: 198 523 134')
                        time.sleep(5)
                        print('Hello your computer has a virus')
                        time.sleep(1)
                        sys.exit()
                    elif number == '#164':
                        if modded == False:
                            modded = True
                            computer.terminal()
                        else:
                            modded = False
                            computer.terminal()
                    elif number == '500 694 102':
                        print('Hello welcome to unbecome drugged or drunk, how may i help you?')
                        time.sleep(2)
                        print('Drunk - Makes you undrunk')
                        print('Drugged - Makes you undrugged')
                        order = input('- ')
                        if order == 'Drunk':
                            print('Okay sir, im going to be undrunking you.')
                            print('Please Wait...')
                            time.sleep(5)
                            if drunk == True:
                                drunk = False
                                print('You are now undrunked.')
                                time.sleep(1)
                                print('Bye!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                            else:
                                print('Well sir, it looks like you are not drunk at all.')
                                time.sleep(1)
                                print('Bye, Have a nice day!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()                                
                            computer.terminal()
                        elif order == 'Drugged':
                            print('Okay sir, im going to be undrugging you.')
                            print('Please Wait...')
                            time.sleep(10)
                            if drugged == True:
                                drugged = False
                                print('You are now undrungged.')
                                time.sleep(1)
                                print('Bye!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                            else:
                                print('Well sir, it looks like you are not drugged at all.')
                                time.sleep(1)
                                print('Bye, Have a nice day!')
                                time.sleep(1)
                                print('[CALL ENDED]')
                                computer.terminal()
                        else:
                            print('Invalid order, sir.')
                            time.sleep(1)
                            print('Call back again')
                            time.sleep(1)
                            print('[CALL ENDED]')
                            computer.terminal()                            
                    else:
                        print('The number you have tried to call doesnt exist or is unavailable. Try again later')
                        computer.terminal()
                else:
                    print('Invalid digit/number.')
                    computer.terminal()
            except ValueError:
                print('Invalid digit/number.')
                computer.terminal()
        elif command == 'drugtest':
            if drugged == True:
                print('Drug Test: Positive (you are on drugs)')
            else:
                print('Drug Test: Negative (you arent on drugs)')
            computer.terminal()
        elif command == 'drunktest':
            if drunk == True:
                print('Drunk Test: Positive (you are drunk)')
            else:
                print('Drug Test: Negative (you arent drunk)')
            computer.terminal()
        elif command == 'phonenumbers':
            print('--== PHONE NUMBERS ==--')
            print('123 123 123 - Neighbor')
            print('453 234 123 - Luigi Pizza')
            print('203 153 323 - Pizza Buyer')
            print('911 - Emergency Services')
            print('112 - Local Emergency Services')
            print('500 694 102 - Undrunker/Undrugger')
            computer.terminal()
        elif command == 'exit':
            with open("storage.dat", "w") as sfile:
                sfile.write(computer.encode(storage))
            with open("credits.dat", "w") as file:
                file.write(computer.encode(credits))
            sys.exit()
        else:
            print('"' + command + '"' + ' not found.')
            computer.terminal()
    # [Console Color Functions]
    def set_console_color(color):
        STD_OUTPUT_HANDLE = -11
        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    def reset_console_color():
        computer.set_console_color(7)
    # [Misc]
    def hasdigits(input_str):
        return any(char.isdigit() for char in input_str)
    # [Decode, Encode]
    def encode(value):
        encoded_value = base64.b64encode(str(value).encode()).decode()
        return encoded_value
    def decode(encoded_value):
        decoded_value = base64.b64decode(encoded_value.encode()).decode()
        return decoded_value
    # [Command Functions]
    def fortuner():
        fortunes = ['You will get eaten by a mutated dog.', 'Your life gets worser each second', 'Youre a alien', 'A weirdo masturbates to your pictures everytime you take a step', 'You will die in 3 years', 'You will die in 3 days', 'You cannot count to 3', 'Theres someone behind you', 'You are fat', 'you will become a whore for the rest of your life', 'you will never get hired', 'you will be raped by alien life', 'you will lose all your money after gambling', 'you have autism', 'you are gay', 'you become the bitch', 'you will never be loved', 'you have clinical depression', 'youre black', 'youre racist', 'youre a alcholic father', 'youre a lazy bastard', 'You will lose big']
        return random.choice(fortunes)
    def goodfortuner():
        goodfortunes = ['Your life actually becomes better', "lmao they caught that boy lacking guess he wasn't really about that life", 'Youre secretly a crush to 5 girls that wanna jump on your dick', 'You will get a good skin in cs2', 'you are not fat', 'You are cooler than me :(', 'you will become the second mrbeast for the rest of your life', 'you become a python coder and get hired', 'Kanye west is gonna give you 50 credits for your work', 'you will win 1000 credits after gambling', 'you get more than 2 bitches', 'you are happy', 'justin bieber', 'youre white', 'you believe in god', 'You give kindness to people', 'You will succed', 'youre not lazy', 'You will win big']
        return random.choice(goodfortunes)
    def quote():
        quotes = ['"The weakest fart the loudest and the cock lovers cum the biggest." -Jonathan 2003', '"Those who are worthy enough of experiencing sex will only experience civil war in trolbel." -Jamal Hostel, 2016', '"Certainly, I will never let you down." -Peter The Porn Seller, 2023 before dying.', '"Americans stereotype everything but their fatness is double the amount as peter griffin weights." -Jamal Hostel, 2023', '"Whenever I get bored of a game, I always start playing it again with a new idea." -Jamal Hostel. 2008', '"Violence isnt the solution to everything, but it surely never ends when it comes to discord arguments." Ion Hostel, 2020 (Son of jamal hostel)', '"Secrets always get revealed, even if you still added a extra layer to it." -Ethan Fernsby, 2 weeks before the first bomb hit',
        '"Look man, its closing time. Tommorow ill sell you the water bottle." -Joe, 2014 before dying from a gas station explosion.', '"Everything is a cycle, expect either something good happens or bad instead." -Jonathan, 2019', '"I know you hate being as a kid but just be happy that at least youre far from old age death." -Jonathan, 2020 before dying.', '"No matter what, everything will get much harder unless you do something about it." -Jamal Hostel, 2021', '"THERES CUM ON ME KEBAB, SPONGEBOB!" -Drug Inspector, 2023']
        return random.choice(quotes)
    def calculator():
        calc = input("Enter a math problem: ")
        try:
            result = eval(calc)
            print(f"{result}")
        except Exception:
            print("Invalid input.")

try:
    with open("credits.dat", "r") as file:
        encoded_credits = file.read().strip()
        credits = int(computer.decode(encoded_credits))
except FileNotFoundError:
    credits = 60 # If youre a lazy bastard you would change this

try:
    with open("storage.dat", 'r') as file:
        for encoded_line in file:
            encoded_line = encoded_line.strip()
            
            decoded_bytes = base64.b64decode(encoded_line)
 
            decoded_text = decoded_bytes.decode('utf-8').strip("[]'\"")

            decoded_text = decoded_text.replace("'", "")
            
            items = decoded_text.split(',')

            storage.extend(item.strip() for item in items if item.strip())
except FileNotFoundError:
    storage = []

computer.set_console_color(2)
computer.terminal()
