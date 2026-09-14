import random


warrior = [
    {"life_PlayerOne": 1000, "life_PlayerTwo": 1000,
        "dano": 90, "curar": 50, "chanceCritica": 0.2}
]

assassin = [
    {"life_PlayerOne": 1000, "life_PlayerTwo": 1000,
        "dano": 45, "curar": 50, "chanceCritica": 0.44}
]


def realizar_ataque_playerOne():
    chanceCritica = classChoice_playerOne[0]["chanceCritica"]

    if random.random() < chanceCritica:
        dano_final = classChoice_playerOne[0]["dano"] * 2
    else:
        dano_final = classChoice_playerOne[0]["dano"]

    return dano_final

def realizar_ataque_playerTwo():
    chanceCritica =classChoice_playerTwo[0]["chanceCritica"]

    if random.random() < chanceCritica:
        dano_final = classChoice_playerTwo[0]["dano"] * 2
    else:
        dano_final = classChoice_playerTwo[0]["dano"]

    return dano_final


print("escolha sua arma player um: guerreiro ou assassino")
chooseClass_playerOne = input()

if chooseClass_playerOne == "guerreiro":
    classChoice_playerOne = warrior
elif chooseClass_playerOne == "assassino":
    classChoice_playerOne = assassin


print("escolha sua arma player dois: guerreiro ou assassino")
chooseClass_playerTwo = input()

if chooseClass_playerTwo == "guerreiro":
    classChoice_playerTwo = warrior
elif chooseClass_playerTwo == "assassino":
    classChoice_playerTwo = assassin


print("vida do player um", classChoice_playerOne[0]["life_PlayerOne"])

print("vida do player dois", classChoice_playerTwo[0]["life_PlayerTwo"])

while classChoice_playerOne[0]["life_PlayerOne"] > 0 and classChoice_playerTwo[0]["life_PlayerTwo"] > 0:
    print("iniciou o combate")

    print("é a vez do palyer um")
    print("você quer atacar, ou se curar?")
    chooseAction_playerOne = input()

    if chooseAction_playerOne == "atacar":
        classChoice_playerTwo[0]["life_PlayerTwo"] -= realizar_ataque_playerOne()
    elif chooseAction_playerOne == "curar":
        classChoice_playerOne[0]["life_PlayerOne"] += classChoice_playerOne[0]["curar"]

    print("vida do player um", classChoice_playerOne[0]["life_PlayerOne"])

    print("vida do player dois", classChoice_playerTwo[0]["life_PlayerTwo"])

    print("é a vez do palyer dois")
    print("você quer atacar, ou se curar?")
    chooseAction_playerTwo = input()

    if chooseAction_playerTwo == "atacar":
        classChoice_playerOne[0]["life_PlayerOne"] -= realizar_ataque_playerTwo()
    elif chooseAction_playerTwo == "curar":
        classChoice_playerTwo[0]["life_PlayerTwo"] += classChoice_playerTwo[0]["curar"]

    print("vida do player um", classChoice_playerOne[0]["life_PlayerOne"])

    print("vida do player dois", classChoice_playerTwo[0]["life_PlayerTwo"])

print("cabou")
