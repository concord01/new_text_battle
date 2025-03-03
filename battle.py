import random


class player:
    def __init__(self, player_health, player_damage,player_paralyzed, flame_charge):
        self.player_health = player_health
        self.player_damage = player_damage
        self.player_paralyzed = player_paralyzed
        self.flame_charge = flame_charge
    def punch(self, enemy_block):
        if (enemy_block):
            self.player_damage = 0
            return(self.player_damage)
        else:
            self.player_damage = random.choice([2,3])
            return(self.player_damage)
    def kick(self):
        self.player_damage = random.choice([1,4])
        return(self.player_damage)
    def health_check(self):
        return(self.player_health)
    def flamethrower(self):
        if self.flame_charge:
            self.player_damage = 5
            return(self.player_damage)
        else:
            self.player_damage = 0

class enemy:
    def __init__(self, enemy_health, enemy_damage, enemy_name):
        self.enemy_health = enemy_health
        self.enemy_damage = enemy_damage
        self.enemy_name = enemy_name
    def attack():
        attack_choice = random.choice([0,2])
        return(attack_choice)
    def enemy_health_check(self):
        return(self.enemy_health)
guy = player(10, 0, False)
super_skeleton = enemy(10,2,"super skeleton")
def battle_start(protag, villain):
    print("Battle Begin!")
    turn = random.choice([0,1])
    while guy.health_check() > 0 and super_skeleton.enemy_health_check() > 0:
        if turn == 0:
            print("Player's turn!")
            player_choice = input("Player can choose to: \n Punch \n Kick \n Flamethrower \n")
            player_choice = player_choice.lower
            if(player_choice == "punch"):
                print("Player punches!")
                guy.punch(False)
                super_skeleton.enemy_health = super_skeleton.enemy_health - guy.player_damage
            elif(player.choice == "kick"):
                print("Player kicks!")
                guy.kick()
                super_skeleton.enemy_health = super_skeleton.enemy_health - guy.player_damage
            elif(player_choice == "flamethrower"):
                print("Player flames!")
                guy.flamethrower()
                super_skeleton.enemy_health = super_skeleton.enemy_health - guy.player_damage
                print("You're out of flames!")
                guy.flame_charge == False
            print("End player turn!")
            turn = 1
        else:
            print(super_skeleton.enemy_name+"'s turn!")
            enemy_attack = super_skeleton.attack()
            if enemy_attack == 0:

            


