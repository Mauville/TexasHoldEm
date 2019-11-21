import random

from Texas.cards import getcards, createdeck, getresult, debugprint, prettyprint, getdummy

playername = input("Please input your name!\n")
pot = 0
winner = ""
player1money = 20000
player2money = 20000
player3money = 20000
player4money = 20000
player1state = "Player 1:"
player2state = "Player 2:"
player3state = "Player 3:"
player4state = playername
player1hand = getdummy([])
player2hand = getdummy([])
player3hand = getdummy([])
player4hand = []
hole = []
currentbet = 0

action1 = ""
action2 = ""
action3 = ""

small = 0

actions = ("Call", "Raise ", "Check", "Fold")

online = True


def printthing():
    screenClear = "\n"
    print(screenClear * 15)
    image = '''
    
	           ╔╦═════════════════════════════╦╦╗
	           ╠╣  ♠  ♣  𝕿𝖊𝖝𝖆𝖘 𝕳𝖔𝖑𝖉'𝖊𝖒   ♥  ♦  ╠╬╣
	           ╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╬╣
	           ╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝

              {player1}                  {player2}
              ${money1}                     ${money2}
              Cards:                     Cards:
              {cards1}                         {cards2}

                          Pot: $ {pot}

                          {hole}


              {player3}                  {player4}
              ${money3}                     ${money4}
              Cards:                     Cards:
              {cards3}                         {cards4}

        //=========[]==[]============[]==[]===========\\
        || 1) {action1} ||  ||  2) {action2} ||  ||   3) {action3} ||
        \\==========[]==[]============[]==[]===========//
        {winner}
        
    '''
    image = image.format(
        player1=player1state,
        player2=player2state,
        player3=player3state,
        player4=player4state,

        money1=player1money,
        money2=player2money,
        money3=player3money,
        money4=player4money,

        cards1=prettyprint(player1hand),
        cards2=prettyprint(player2hand),
        cards3=prettyprint(player3hand),
        cards4=prettyprint(player4hand),

        pot=pot,
        hole=prettyprint(hole),
        action1=action1,
        action2=action2,
        action3=action3,
        winner=winner
    )
    print(image)


def getblinds():
    global small
    value = 30
    if small == 0:
        bet(0, value)
        bet(1, value * 2)
    elif small == 1:
        bet(1, value)
        bet(2, value * 2)
    elif small == 2:
        bet(2, value)
        bet(3, value * 2)
    elif small == 3:
        var = int(input("How much for the small blind? \n $ "))
        bet(3, var)
        bet(0, var * 2)
    printthing()


def roundbet(second=False, currentbet=random.randint(1, 10)):
    global action1
    global action2
    global action3
    global player1state
    global player2state
    global player3state
    global player4state
    global player1hand
    global player2hand
    global player3hand
    if small == 0 or small == 1 or small == 3:
        foldfactor = random.randint(1, 100)
        # whofolds
        if foldfactor < 20 or currentbet > player1money:
            player1state = "FOLD"
            player1hand = []
        if 20 < foldfactor < 25 or currentbet > player2money:
            player2state = "FOLD"
            player2hand = []
        if 25 < foldfactor < 35 or currentbet > player3money:
            player3state = "FOLD"
            player3hand = []

        if player1state != "FOLD":
            bet(0, currentbet)
        if player2state != "FOLD":
            bet(1, currentbet)
        if player3state != "FOLD":
            bet(2, currentbet)
        if player4state != "FOLD" and second is not True and currentbet < player4money:
            action1 = actions[0]
            action2 = actions[1]
            action3 = actions[3]
            printthing()
            # prompt player for call raise or fold
            action = input("Action: ")
            if action == "1":
                bet(3, currentbet)
            elif action == "2" and second is False:
                raisal = int(input("$ "))
                bet(3, currentbet + raisal)
                roundbet(second=True, currentbet=raisal)
            elif action == "3":
                player4state = "FOLD"

    if small == 2:
        action1 = actions[1]
        action2 = actions[2]
        action3 = actions[3]
        # input bet
        # prompt for bet


def round():
    global player1hand
    global pot
    global player1money
    global player2money
    global player3money
    global player4money
    global playername
    global player1state
    global player2state
    global player3state
    global player4state
    global player1hand
    global player2hand
    global player3hand
    global player4hand
    global currentbet
    global hole
    global winner
    global action1
    global action2
    global action3
    global small
    deck = createdeck()
    player4hand = getcards(player4hand, 2, deck)
    getblinds()
    roundbet()
    hole = getcards(hole, 3, deck)
    roundbet()
    hole = getcards(hole, 1, deck)
    roundbet()
    hole = getcards(hole, 1, deck)
    roundbet()
    player1hand.clear()
    player2hand.clear()
    player3hand.clear()
    player1hand = getcards(player1hand, 2, deck)
    player2hand = getcards(player2hand, 2, deck)
    player3hand = getcards(player3hand, 2, deck)
    showdown()
    small += 1
    if small > 3:
        small = 0
    player1state = "Player 1:"
    player2state = "Player 2:"
    player3state = "Player 3:"
    player4state = playername
    player1hand = getdummy([])
    player2hand = getdummy([])
    player3hand = getdummy([])
    player4hand = []
    hole = []
    currentbet = 0
    winner = ""
    pot = 0

    action1 = ""
    action2 = ""
    action3 = ""

    # get cards results


def getbestgame(hand, hole):
    result = 0
    backhole = hole[:]
    # Single card case
    for j in range(0, 1):
        currentcard = hand[j]
        for i in range(0, len(hole) - 1):
            hole[i] = currentcard
            if getresult(hole) > result:
                result = getresult(hole)
            hole = backhole[:]

    # multi card case
    cleanhole = hole[:]
    for i in range(0, len(hole)):
        hole = cleanhole
        for j in range(i + 1, len(hole)):
            hole[i] = hand[0]
            hole[j] = hand[1]
            if (getresult(hole) > result):
                result = getresult(hole)

    return result


def payout(playernum):
    global player1money
    global player2money
    global player3money
    global player4money
    global pot
    if playernum == 0:
        player1money += pot
        pot = 0
    if playernum == 1:
        player2money += pot
        pot = 0
    if playernum == 2:
        player3money += pot
        pot = 0
    if playernum == 3:
        player4money += pot
        pot = 0


def showdown():
    global winner
    vals = [4]
    vals.append(getbestgame(player1hand, hole))
    vals.append(getbestgame(player2hand, hole))
    vals.append(getbestgame(player3hand, hole))
    vals.append(getbestgame(player4hand, hole))
    maximum = vals.index(max(vals))
    if maximum == 0:
        payout(0)
    if maximum == 1:
        payout(1)
    if maximum == 2:
        payout(2)
    if maximum == 3:
        payout(3)
        winner = "You've won!"
    printthing()


def bet(playernum, money):
    global player1money
    global player2money
    global player3money
    global player4money
    global pot
    if playernum == 0:
        player1money -= money
        pot += money
    elif playernum == 1:
        player2money -= money
        pot += money
    elif playernum == 2:
        player3money -= money
        pot += money
    elif playernum == 3:
        player4money -= money
        pot += money


def game():
    while True:
        round()
        if input("Another round? Enter for yes, anything else for no.") != "":
            print("Thanks for playing.")
            break


game()
