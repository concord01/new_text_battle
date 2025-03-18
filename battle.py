import random


class player:
    def __init__(self, player_health, player_damage, flame_charge):
        self.player_health = player_health
        self.player_damage = player_damage
        self.flame_charge = flame_charge
    def punch(self):
        self.player_damage = random.choice([2,3])
        return(self.player_damage)
    def kick(self):
        self.player_damage = random.choice([1,4])
        return(self.player_damage)
    def health_check(self):
        return(self.player_health)
    def flamethrower(self):
        if self.flame_charge == True:
            self.player_damage = 6
            return(self.player_damage)
        else:
            self.player_damage = 0
            print("You're out of flames!")
            return(self.player_damage)

class enemy:
    def __init__(self, enemy_health, enemy_damage, enemy_name):
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.enemy_name = enemy_name
    def attack(self):
        attack_choice = random.choice([0,1])
        if attack_choice == 0:
            print("You are punched for 2 damage!")
            return(self.enemy_damage)
        elif attack_choice == 1:
            print("You are slashed at for 4 damage!")    
            return(self.enemy_damage * 2)
    def enemy_health_check(self):
        return(self.enemy_health)


guy = player(10, 0, True)
bad_guy_bank = ["super skeleton", "really big goblin", "comically large rat"]
bad_guy_selection = random.choice(bad_guy_bank)
bad_guy= enemy(10,2, bad_guy_selection)

def mandatory_helper_function(lower,higher):
    random_selection = random.choice([lower,higher])
    return random_selection

def battle_start(protag, villain):
    print("Battle Begin!")
    p_health = protag.player_health
    v_health = villain.enemy_health
    turn = mandatory_helper_function(0,1)
    while p_health > 0 and v_health > 0:
        print("You are at " + str(p_health) + " health!")
        print("The "+ villain.enemy_name +" is at " + str(v_health) + " health!")
        if turn == 0:
            print("Player's turn!")
            player_choice = input("Player can choose to: \n Punch \n Kick \n Flamethrower \n")
            player_choice = player_choice.lower()
            if(player_choice == "punch"):
                v_health = v_health - protag.punch()
                print("Player punches for "+str(protag.player_damage)+"!")
            elif(player_choice == "kick"):
                protag.kick()
                print("Player kicks for "+str(protag.player_damage)+"!")
                v_health = v_health - protag.kick()
            elif(player_choice == "flamethrower"):
                protag.flamethrower()
                print("Player flames for "+str(protag.player_damage)+"!")
                v_health = v_health- protag.flamethrower()
                protag.flame_charge = False
            else:
                print("Ok man, guess you skip")
            print("End player turn!")
            turn = 1
        else:
            print(villain.enemy_name+"'s turn!")
            p_health = p_health - villain.attack()
            turn = 0
    if p_health > 0:
        print("You beat the "+villain.enemy_name+"! You gain XX xp!")
    elif p_health <= 0:
        print("You died!")

            


            


battle_start(guy, bad_guy)