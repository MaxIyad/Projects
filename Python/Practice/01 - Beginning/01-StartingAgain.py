import random

valid_Weapons = ["rock", "paper", "scissors"]
winStreak = 0

def main(valid_Weapons, winStreak):
    player_Weapon = input("Your Weapon: ")
    checkWeapon(valid_Weapons, player_Weapon, winStreak)

def checkWeapon(valid_Weapons, player_Weapon, winStreak):
    for weapon in valid_Weapons:
        if weapon == player_Weapon:
            opponents_Weapon = random.choice(valid_Weapons)
            print("Your op's choice: " + opponents_Weapon)
            compete(player_Weapon=player_Weapon, opponents_Weapon=opponents_Weapon, valid_Weapons=valid_Weapons, winStreak=winStreak)
            break
    else:
        print("Invalid input. Try again")
        main(valid_Weapons=valid_Weapons)


def compete(player_Weapon, opponents_Weapon, valid_Weapons, winStreak):
    if player_Weapon == opponents_Weapon:
        print("It's a draw!")
    elif valid_Weapons.index(player_Weapon) - valid_Weapons.index(opponents_Weapon) == 1 or valid_Weapons.index(player_Weapon) - valid_Weapons.index(opponents_Weapon) == -2:
        print("You've won!")
        winStreak += 1
        print("Wins: " + str(winStreak))
    else:
        print("You've lost.")
        winStreak = 0
    main(valid_Weapons=valid_Weapons, winStreak=winStreak)


main(valid_Weapons=valid_Weapons, winStreak=winStreak)