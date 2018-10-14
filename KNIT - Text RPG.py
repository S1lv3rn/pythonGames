#KNIT Text RPG
import random

def drawBoard(menu, description):
    #this will print out the menu screen and description
    print(description)
    print('+-----------+-----------+')
    print('| ' + menu[1] + ' | ' + menu[2] + ' |')
    print('+-----------+-----------+')
    print('| ' + menu[3] + ' | ' + menu[4] + ' |')
    print('+-----------+-----------+')

def whichPlace(local, menu, desc):
    #this will find where the player is
    if local == 'town':
        atTown(menu, desc)
    elif local == 'battle':
        atForest(menu, desc)
    elif local == 'wool':
        atWool(menu, desc)
    elif local == 'home':
        atHome(menu, desc)
    elif local == 'shop':
        atShop(menu, desc)

def atTown(Nenu, descr):
    #will display board and be in charge of the town
    Nenu[1] = 'Forest   '
    Nenu[2] = 'Wool     '
    Nenu[3] = 'Home     '
    Nenu[4] = 'SHop     '
    descr = 'You are in the TOWN.'
    drawBoard(Nenu, descr)



def atWool(Nenu, descr):
    #will display board and be in charge of wool
    Nenu[1] = 'Buy Needs'
    Nenu[2] = 'Depart   '
    Nenu[3] = '         '
    Nenu[4] = '         '
    descr = 'You are in WOOLCRAFTS. KNITTING NEEDLES are FIVE(5) GOLD.'
    drawBoard(Nenu, descr)




def atShop(Nenu, descr):
    #will display board and be in charge of the shop
    Nenu[1] = 'SellCloth'
    Nenu[2] = 'Buy Food '
    Nenu[3] = 'Buy Items'
    Nenu[4] = 'Depart   '
    descr = 'You are in DENNERS. CLOTHES are sold at TEN(10) GOLD each. FOOD and ITEMS are TEN(10) GOLD.'
    drawBoard(Nenu, descr)




def atHome(Nenu, descr):
    #will display board and be in charge of the town
    Nenu[1] = 'CUr8     '
    Nenu[2] = 'CR8      '
    Nenu[3] = 'Rest     '
    Nenu[4] = 'Depart   '
    descr = 'You are at HOME. You can make CLOTHES or ARMOUR with WOOL SQUARES here.'
    drawBoard(Nenu, descr)

def atForest(Nenu, descr):
    Nenu[1] = 'Attack   '
    Nenu[2] = 'Items    '
    Nenu[3] = 'Magic    '
    Nenu[4] = 'Depart   '
    descr = 'You are in the FOREST.'
    drawBoard(Nenu, descr)

def getReward(wlSQ, lv):
    gain = random.randint(0, 3)
    print('You defeated the WOOL MONSTER! You gain '+ str(gain) + ' WOOL SQUARES!')
    print('You gain ' + str(lv) + ' EXPERIENCE POINTS!')
    wlSQ += gain
    print('You now have ' + str(wlSQ) + ' WOOL SQUARE(S).')

def lvlUP(lvl, ex, nxEx, hp, mp):
    ex += lvl
    if ex == nxEx:
        nxEX += nxEX * (lvl/10)
        lvl += 1
        hp += hp * (lvl/10)
        mp += mp * (lvl/10)
        ex = 0
        print('You LEVELED UP!')
        print('You are now LEVEL ' + str(lvl) + '!')
        print(str(nxEX) + ' more EXPERIENCE POINTS to the next LEVEL.')

def playAgain():
    print('Do you wish to PLAY AGAIN?')
    return input().lower().startswith('y')


#######################################################
########### T H E  G A M E ############################
while True:
    playDone = False
    MAXHP = 50
    HP = MAXHP
    MAXMP = 30
    MP = MAXMP
    pAtt = 5
    pDef = 2
    pMag = 6
    pMdef = 3
    level = 1
    EX = 0
    ex2nxLV = 5
    battleStart = False

    gold = 5
    cloth = 0
    woolSq = 10
    items = 0
    food = 10
    work = ''
    workLeft = 0
    place = 'town'
    dec = ''
    Menu = ['', '', '', '', '']
    needleUse = 20
    armourUse = 0
    enePop = 10
    navi = ''



    #start############################################################
    print()
    print('               ~Welcome to KNIT the TEXT RPG~')
    print('''
At HOME you can CUR8 your INVENTORY, CR8 CLOTHES or ARMOR using WOOL SQUARES in the evening before RESTING.
You can BATTLE WOOL MONSTERS in the FOREST to gain the WOOL SQUARES.
In the SHOP DENNERS, you can SELL the CLOTHES for GOLD and BUY FOOD and ITEMS.
In WOOLCRAFTS, you can more BUY KNITTING NEEDLES.
                       ~-~-~-~-~-~-~-~-~
                       ''')
    print('Enter the CAPITAL letters to SELECT your choice or enter QUIT to QUIT.')
    print
    whichPlace(place, Menu, dec)
    while playDone == False:


        if place == 'town':
        #town##############################################
            navi = ''
            while navi not in 'f w h sh'.split():
                navi = input().lower()
                if navi == 'f':
                    print('You enter the FOREST.')
                    input()
                    place = 'battle'
                    whichPlace(place, Menu, dec)
                elif navi == 'w':
                    print('You enter WOOLCRAFTS.')
                    input()
                    place = 'wool'
                    whichPlace(place, Menu, dec)
                elif navi == 'h':
                    print('You return HOME.')
                    input()
                    place = 'home'
                    whichPlace(place, Menu, dec)
                elif navi == 'sh':
                    print('You enter DENNERS.')
                    input()
                    place = 'shop'
                    whichPlace(place, Menu, dec)
                elif navi == 'quit':
                    playDone = True
                    break
                else:
                    print('Invalid, try again.')


        elif place == 'wool':
        #WOOL###############################################
            print('You have ' + str(gold) + ' GOLD.')
            navi = ''
            while navi not in 'bn d'.split():
                navi = input().lower()
                if navi == 'bn':
                    #buy needles
                    if gold >= 5:
                        gold -= 5
                        needleUse += 10
                        print('You have bought a pair of KNITING NEEDLES.')
                        print('You now have ' + str(gold) + ' GOLD.')
                    else:
                        print('You do not have enough GOLD to buy that.')
                    input()
                    place = 'wool'
                    whichPlace(place, Menu, dec)

                elif navi == 'd':
                    #back
                    print('You leave WOOLCRAFTS.')
                    input()
                    place = 'town'
                    whichPlace(place, Menu, dec)

                elif navi == 'quit':
                    playDone = True
                    break

                else:
                    print('Invalid, try again.')


        elif place == 'battle':
        # F O R E S T #####################################
            if battleStart == False:
                if needleUse >= 1 and enePop >= 1:
                    woolSq += 1
                    print('You wander through the trees and a WOOL MONSTER crosses your path.')
                    input()

                    #set enemy stats
                    MAXeHP = random.randint(24, 35)
                    eAtt = random.randint(1, 3)
                    eMag = (5 - eAtt) * level
                    eAtt = eAtt * level
                    eDef = random.randint(0, 3)
                    eMdef = (5 - eDef) * level
                    eDef = eDef * level
                    eHP = MAXeHP


                    battleStart = True
                    place = 'battle'
                    whichPlace(place, Menu, dec)

                elif enePop >= 1 and needleUse <= 0:
                    #add code for running out of enemies - limit is 10
                    print('But your KNITTING NEEDLES are worn out! You return to buy new ones.')
                    input()
                    place = 'town'
                    whichPlace(place, Menu, dec)

                else:
                    print('You look around but all there is the howling winds.')
                    input()
                    place = 'town'
                    whichPlace(place, Menu, dec)
            else:
                print('WL MNSTR HP: ' + str(eHP)+ '/' + str(MAXeHP))
                print()
                print('HP: ' + str(HP) + '/' + str(MAXHP))
                print('MP: ' + str(MP) + '/' + str(MAXMP))
                navi = ''
                while navi not in 'a i m d'.split():
                    navi = input().lower()
                    #attack
                    if navi == 'a':
                        print('You decide to ATTACK with a KNIT stitch.')
                        input()
                        if pAtt > eDef:
                            eHP = eHP - (pAtt - eDef)
                            print('You KNIT a STICH!')
                            #check dead
                            if eHP <= 0:
                                HP += 5
                                enePop -= 1
                                armourUse -= 1
                                getReward(woolSq, level)
                                lvlUP(level, EX, ex2nxLV, MAXHP, MAXMP)
                                input()
                                battleStart = False
                                place = 'battle'
                                whichPlace(place, Menu, dec)


                        else:
                            print('The WOOL MONSTER dodges and you SLIP the STICH!')
                        input()

                        ##########ene Move
                        choi = random.randint(0,2)
                        if choi == 1:
                            print('The WOOL MONSTER comes in with a LASH ATTACK.')
                            input()
                            if armourUse >= 1:
                                armP = 1 * level
                            else:
                                armP = 0

                            if eAtt > (pDef + armP):
                                HP = HP - (eAtt - (pDef + armP))
                                print('The ATTACK lands!')
                            else:
                                print('You dodge roll out the way.')

                        else:
                            print('The WOOL MONSTER starts to WRAP around and CAST ON you.')
                            input()
                            if armourUse >= 1:
                                armP = 1 * level
                            else:
                                armP = 0

                            if eMag > (pMdef + armP):


                                HP = HP - (eMag - (pMdef + armP))
                                print('You are tied up tight!')

                                if HP == 0:
                                    print('You take so much damage that you die!')
                                    input()
                                    playDone = True
                            else:
                                print('You deflect the CAST ON!')
                        input()
                        place = 'battle'
                        whichPlace(place, Menu, dec)

                    #magic
                    elif navi == 'm':
                        if MP >= 2:
                            print('You decide to CAST ON a PURL STICH')
                            MP -= 2
                            input()

                            if pAtt > eDef:
                                eHP = eHP - (pMag - eMdef)
                                print('You PURL a STICH!')
                                #check dead
                                if eHP <= 0:
                                    HP += 5
                                    enePop -= 1
                                    armourUse -= 1
                                    getReward(woolSq, level)
                                    lvlUP(level, EX, ex2nxLV)
                                    input()
                                    battleStart = False
                                    place = 'battle'
                                    whichPlace(place, Menu, dec)


                            else:
                                print('The WOOL MONSTER dodges and you SLIP the STICH!')
                            input()

                           ########ene Move
                            choi = random.randint(0,2)
                            if choi == 1:
                                print('The WOOL MONSTER comes in with a LASH ATTACK.')
                                input()
                                if armourUse >= 1:
                                    armP = 1 * level
                                else:
                                    armP = 0

                                if eAtt > (pDef + armP):
                                    HP = HP - (eAtt - (pDef + armP))
                                    print('The ATTACK lands!')
                                else:
                                    print('You dodge roll out the way!')

                            else:
                                print('The WOOL MONSTER starts to WRAP around and CAST ON you.')
                                input()
                                if eMag > (pMdef + armP):
                                    if armourUse >= 1:
                                        armP = 1 * level
                                    else:
                                        armP = 0

                                    HP = HP - (eMag - (pMdef + armP))
                                    print('You are tied up tight!')

                                    if HP == 0:
                                        print('You take so much damage that you die!')
                                        input()
                                        playDone = True
                                else:
                                    print('You deflect the CAST ON!')
                        else:
                            print('You do not have enough MP to CAST a PURL.')
                        input()
                        place = 'battle'
                        whichPlace(place, Menu, dec)

                    #use item
                    elif navi == 'i':
                        if items >= 1:
                            print('You use ONE(1) ALL ROUND HEAL.')
                            items -= 1
                            MP += 10
                            HP += 10

                            ##########ene Move
                            choi = random.randint(0,2)
                            if choi == 1:
                                print('The WOOL MONSTER comes in with a LASH ATTACK.')
                                input()
                                if armourUse >= 1:
                                    armP = 1 * level
                                else:
                                    armP = 0

                                if eAtt > (pDef + armP):
                                    HP = HP - (eAtt - (pDef + armP))
                                    print('The ATTACK lands!')
                                else:
                                    print('You dodge roll out the way!')

                            else:
                                print('The WOOL MONSTER starts to WRAP around and CAST ON you.')
                                input()
                                if eMag > (pMdef + armP):
                                    if armourUse >= 1:
                                        armP = 1 * level
                                    else:
                                        armP = 0

                                    HP = HP - (eMag - (pMdef + armP))
                                    print('You are tied up tight!')

                                    if HP == 0:
                                        print('You take so much damage that you die!')
                                        input()
                                        playDone = True
                                else:
                                    print('You deflect the CAST ON!')

                        else:
                            print('You do not have any ITEMS.')
                        input()
                        place = 'battle'
                        whichPlace(place, Menu, dec)


                    elif navi == 'd':
                        #back
                        print('You run away from the BATTLE.')
                        input()
                        place = 'town'
                        whichPlace(place, Menu, dec)

                    elif navi == 'quit':
                        playDone = True
                        break

                    else:
                        print('Invalid, try again.')


        elif place == 'shop':
        # S H O P ############################################
            print('You have ' + str(gold) + ' GOLD')
            navi = ''
            while navi not in 'sc bf bi d'.split():
                navi = input().lower()
                if navi == 'sc':
                    #sell clothes
                    if cloth <= 0:
                        print('You do not have any CLOTHES to sell')
                    else:
                        cloth -= 1
                        gold += 10
                        print('You sold ONE(1) CLOTHES')
                        print('You now have ' + str(gold) + ' GOLD')
                    input()
                    place = 'shop'
                    whichPlace(place, Menu, dec)

                elif navi == 'bf':
                    #buy food
                    if gold >= 10:
                        gold -= 10
                        food += 5
                        print('You buy FIVE(5) FOOD')
                        print('You now have ' + str(gold) + ' GOLD')
                    else:
                        print('You do not have enough GOLD to buy that')
                    input()
                    place = 'shop'
                    whichPlace(place, Menu, dec)

                elif navi == 'bi':
                    #buy items
                    if gold >= 10:
                        gold -= 10
                        items += 1
                        print('You buy ONE(1) ALL ROUND HEAL')
                        print('You now have ' + str(gold) + ' GOLD')
                    else:
                        print('You do not have enough GOLD to buy that')
                    input()
                    place = 'shop'
                    whichPlace(place, Menu, dec)

                elif navi == 'd':
                    print('You leave DENNERS')
                    input()
                    place = 'town'
                    whichPlace(place, Menu, dec)

                elif navi == 'quit':
                    playDone = True
                    break

                else:
                    print('Invalid, try again')


        elif place == 'home':
        # H O M E ###################################################
            navi = ''
            while navi not in 'cu cr r d'.split():
                navi = input().lower()
                if navi == 'cr':
                    print('You have ' + str(woolSq) +' WOOL SQUARE(S).')
                    if work == '' and workLeft <= 0 and woolSq >= 10:
                        print('You can CR8 ARMOUR(A), CLOTHES(C) or go back(B)')
                        work = input().lower()
                        if work == 'a':
                            woolSq -= 10
                            workLeft = 5
                            print('Your evening project is ARMOUR')
                        elif work == 'c':
                            woolSq -= 10
                            workLeft = 5
                            print('Your evening project is CLOTHES')
                        elif work == 'b':
                            work = ''
                            #input()
                            place = 'home'
                            #whichPlace(place, Menu, dec)
                            #print('wl:' + str(workLeft) +' W:"'+work + '" wq:'+str(woolSq))
                        else:
                            print('Invalid, try again')
                            work = input().lower()

                    elif woolSq < 10 and work == '' and workLeft <= 0 :
                        print('You do not have enough WOOL SQUARES for an evening project')
                    else:
                        print('You already have an evening project')
                    input()
                    place = 'home'
                    whichPlace(place, Menu, dec)

                elif navi == 'cu':
                    print('HP: ' + str(HP) + '/' + str(MAXHP) + ', MP: ' + str(MP) + '/' + str(MAXMP))
                    print('EXP: ' + str(EX) + '/' + str(ex2nxLV))
                    print('You have:' + str(gold) + ' GOLD, ' + str(woolSq) + ' WOOL SQUARE(S), ' + str(cloth) + ' CLOTHES, ' + str(items) + ' ALL ROUND HEAL(S) and ' + str(food) + ' FOOD')
                    input()
                    place = 'home'
                    whichPlace(place, Menu, dec)

                elif navi == 'r':
                    if food >= 1:
                        if work == '':
                            food -= 1
                            print('You eat your evening meal and REST for the night')
                            HP = MAXHP
                            MP = MAXMP
                            enePop = 10

                        elif work == 'a' or work == 'c':
                            food -= 1
                            workLeft -= 1
                            print('You work on your evening project, eat and REST for the night')
                            HP = MAXHP
                            MP = MAXMP
                            enePop = 10
                            if workLeft <= 0:
                                if work == 'a':
                                    print('You have finished the ARMOUR')
                                    armourUse += 5
                                elif work == 'c':
                                    print('You have finished the CLOTHES')
                                    cloth += 1
                                else:
                                    print('ERROR')
                        else:
                            print('ERROR')
                    else:
                        print('You are too hungry to REST')

                    input()
                    place = 'home'
                    whichPlace(place, Menu, dec)

                elif navi == 'd':
                    print('You leave your HOME')
                    input()
                    place = 'town'
                    whichPlace(place, Menu, dec)

                elif navi == 'quit':
                    playDone = True
                    break

                else:
                    print('Invalid, try again')

    #######################################################################################################################
    if playDone:
        if  not playAgain():
            break
