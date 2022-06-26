

print("B is default. Choose wisely.\n")
input("They say that the flap of a butterfly's wings in the Amazon can cause a tornado in Texas.\n")
input("Such small creature caused fatal damage.\n")
input()
input("Similar to the power of one's decision in life.\n")
input("Be minute or huge, quick or slow decisions.\n")
input("The future rests on every decision.\n")
messge = ""
user_input =""
while True:
    user_input =""
    input("-"*25)
    input()
    input("BZZZ......  "*3)
    input()
    if len(messge) >1:
        input("You had a such a strange dream.\n")
        input(messge)
        input("A message being echoed.")
        input("You ignored it as it doesn't make sense.")

    input("You woke up to an alarm, starting the day for another work day.\n")
    path = ""
    path_Later=""
    input()
    # decision one, turn off then sleep, or prepare to work
    while user_input !="a" and user_input!="b":
        user_input = input("You decide to?\nA) Wake up, go to work.\nB) Continue to sleep\n\n").lower()
    # if sleep
    if user_input == "a":
        input("You got up to prepare for another normal day.\n")
        input("."*24)
        path = "early"
        messge = "Sleep more"
    # if to work
    else:
        if user_input == "b":
            input("You're feeling a bit lazy.\nYou dozed off........\n")
        else:
            input("A bit naughty, not following instructions?\n")
            input()
            input("Such person would sleep.........\n")
        messge = "WAKE UP NOW!!!!"
        input("\n")

    # path sa early
    if user_input == "a":
        input("You left the house and to walk to your office.\n")
        input()
        path = "early"
        input("Greenlight, you can't cross.\n")
        input("A man you are familiar appeared. The High School BULLY.\Approached and belittled you.\n")
        user_input = ""
        while user_input !="a" and user_input!="b":
            user_input = input("What would you do?\nA)You ignore the bully.\nB)Confront the bully.\n\n").lower()
        if user_input == "a":
            input("The bully got ignored. His face flushed.... he got embarassed. He bowed down and tried to cross the road.\n")
            input("A fast moving truck appeared.... \n")
            input("He didn't notice\nYou saw the truck and  got time to react\nWhat would you do?\n")
            user_input = ""
            while user_input != "a"and user_input!="b":
                user_input = input("A)Save him.\nB)Ignore.\n").lower()
            if user_input == "a":
                path = "save"
                messge = "IGNORE HIM"
            else:
                messge = "SAVE HIM"
                path = "ignore"
        else:
            input("Those years of torment must end. You confronted the bully\nArgument got intense. He tried to stab you with a knife, but you pushed him.\n")
            input("A truck ran him over.\n")
            input("It tormented you for years.\nYou were innocent for self-defense, but never free.\n")
    else:
        input("You woke up late and left the house ran to your office.\nOn your way, an accident happened.\n")
        path="late"
        input("A familiar person got hit by a truck, rumors say he was chased while waving a knife.\n")
        input("The bully who tormented you for years. Died.")
        user_input = ""
        while user_input !="a" and user_input!="b":
            user_input = input("What would you feel?\nA)Sympathy, as a person you recognize died.\nB)Satisfied, as your bully got karma.\n")
        if user_input == "A":
            input("You sympathized thinking how life can be fragile.")
            path_Later = "symp"
        else:
            path_Later = "angry"
            input("You were satisfied. That somehow karma bit earlier than expected.")
            input("Maybe you got some anger issues in life.")
        input("The days continued. after this eventful day.\n")
        path = "path2"

    if path == 'save':
        input("You ran, as swift as you can.\n")

        input("You pushed him off.\n")

        input("You got hit instead........YOU DIED.....\n")
        path = "path1"
    elif path == "ignore":
        input("You remembered all those tormenting days.\n\n'BANG'\nThe sound of hitting a metal\n\nThe bully died on the spot.\n\nIs this karma?.......\n")

    if path == "path1":
        input("You died\nIt's all dark\nSilence\nNothingness\n")
        input("A light appeared\n")
        input("You were reincarnated to another world.\n")
        input("A world in ruins\n")
        input("With the remaining hope, you.\n")
        input("OR ARE YOU!?\n")

        input("A strange orb appeared, asking you.\nTo become a paladin, to follow and do the righteous, save the world.\nOr become an emissary of evil.\nWith the fate to destroy all who remain.\n")
        user_input = ""
        while user_input!="a"and user_input!="b":
            user_input == input("A)Become a Paladin\nB)Destroy everything\n\n").lower()
        if user_input == "a":
            input("You felt sad seeing the ruins of this world.")
            input("You decided be the hope of this world.\n")
            path = "path1"
        else:
            input("You remembered how you saved your bully.\n")
            input("Fate is funny, such heroism would result in death.\n")
            input("UNACCEPTABLE\n")
            input("You were consumed by anger, and decided to go against FATE.\n")
            path = "path1-2"
    elif path == "path2":
        input("Years passed.....\n")
        input("BOOM!!\n")
        input("You woke up with Demons attacking the City!!\n")
        input("A leader of sort came searching for you\n")
        input("A familiar face. The bully of your high school, who tormented you.\n")
        input("But should have died years ago.\n")
        input("He tortured you now. As he explained that you are the reason for this.\n")
        input("He explained, that on that fateful day, you should have died as determined by the FATE.\n")
        input("You grew weak...dying.\n")
        input("A power within you grew strong. You knew, this power can free you and destroy those demons.\n")
        input("You broke free.\n")
        input("And destroyed all attackers.\n\n")
        input("As you fight and win\nEveryone cheered and delighted.\nYou are the hope.\n")



    if path == "path1":
        input("You embarked on your journey\n")
        input("You searched far and wide\n")
        input("Saved human settlements. YOU became hope\n")
        input("It took months\n")
        input("But the humans are now liberated, from the attack by demons.\n")
        input("....Centuries passed....\n")
        input("YOU CANNOT DIE. Your decision to become hope would last for eternity. You looked for reasons why, with no fruit.\n")
        input("You grew bitter and hated fate.\n")
        

    elif path == "path1-2":
        input("You desecrated the world.\nBurned everything that moves.\n")
        input()
        input("The humans got no chance.\n")
        input()
        input("Weeks passed then the ruins, turned to asses.\n")
        input()
        input("Years passed. LIVING in this burned land.\n")
        input()
        input("You grew bitter of this fate. You travelled across planets, in search for solutions.\n")
        input()

    if path_Later == "symp":
        input("You became the protector of Earth.\n")
        input("PEACE is found\n")
        input("Now and for centuries.\n")
        input("....Centuries passed....\n")
        input("YOU CANNOT DIE.\n")
        input("Your decision to become hope would last for eternity. You looked for reasons why, with no fruit.\n")
        input("You grew bitter and hated fate.\n")
        messge= ("Save him")
    elif path_Later == "angry":
        input("You saved them. But most people blamed you.")
        input("You grew bitter of their ungratefulness.")
        input("You decided to be just.")
        input("Absolute power must be displayed")
        input("You ruled for centuries.")
        input("....Centuries passed....\n")
        input("YOU CANNOT DIE.\n")
        input("Your decision to accept the power gave you eternal life full of suffering. You looked for reasons why, with no fruit.\n")
        input("You grew bitter and hated fate.\n")
        messge = "Do not be bitter."
    # endgame
    # if path == "endgame":
    input("You discovered a power, that can turn back time to a specific point.This would erase all events after, even the memories.\n")
    input("BUT, hope is there, that your decision may change, HOPE, that your decision can change YOUR future.\n")
    input("You go back, on the day you reunited with your bully.\n")