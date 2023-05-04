
class save_code_func():
    username = []
    password = []
    numberid = []
    coins = []
    gems =  []
    level =  []
    health =  []
    weapon =  []
    rarity =  []
    first_time =  []
    dmg =  []
    critchance =  []
    critdmg = []
    enemy =  []
    enemydmg =  []
    enemyhealth =  []
    dropped_weapon =  []
    dropped_rarity =  []
    increase_dmg =  []
    turn =  []
    training =  []
    first_time_spiral =  []
    first_time_spiral2 =  []
    first_time_spiral3 =  []
    spiral =  []
    first_time_ww3 =  []
    minions_killed =  []
    velvet_alive =  []
    god_guy_alive =  []
    zombie_killer_alive =  []
    first_time_trialI =  []
    first_time_trialII =  []
    trial_i =  []
    trial_ii =  []
    def __init__(self):
        pass
        global username, password, numberid, coins, gems, level, health, weapon, rarity, first_time, dmg, critchance, critdmg, enemy, enemydmg, enemyhealth, dropped_weapon, dropped_rarity
        global increase_dmg, turn, training, first_time_spiral, first_time_spiral2, first_time_spiral3, spiral, first_time_ww3, minions_killed, velvet_alive, god_guy_alive
        global zombie_killer_alive, first_time_trialI, first_time_trialII, trial_i, trial_ii

    def enter_save(save_code):
        global username, password, numberid, coins, gems, level, health, weapon, rarity, first_time, dmg, critchance, critdmg, enemy, enemydmg, enemyhealth, dropped_rarity
        global dropped_weapon, increase_dmg, turn, training, first_time_spiral, first_time_spiral2, first_time_spiral3, spiral, first_time_ww3, minions_killed, velvet_alive
        global god_guy_alive, zombie_killer_alive, first_time_trialI, first_time_trialII, trial_i, trial_ii

        for letter in save_code:
            while letter != '-':
                username.append(letter)
            ''.join(username)
            while letter != '-':
                password.append(letter)
            ''.join(password)
            while letter != '-':
                numberid.append(letter)
            ''.join(numberid)
            if numberid != (len(username) + len(password)) * 2 + 1:
                return '''Tried to cheat the system, did you?'''
            while letter != '-':
                coins.append(letter)
            ''.join(coins)
            while letter != '-':
                gems.append(letter)
            ''.join(gems)
            while letter != '-':
                level.append(letter)
            ''.join(level)
            while letter != '-':
                health.append(letter)
            ''.join(health)
            while letter != '-':
                weapon.append(letter)
            ''.join(weapon)
            while letter != '-':
                rarity.append(letter)
            ''.join(rarity)
            while letter != '-':
                first_time.append(letter)
            ''.join(first_time)
            while letter != '-':
                dmg.append(letter)
            ''.join(dmg)
            while letter != '-':
                critchance.append(letter)
            ''.join(critchance)
            while letter != '-':
                critdmg.append(letter)
            ''.join(critdmg)
            while letter != '-':
                enemy.append(letter)
            ''.join(enemy)
            while letter != '-':
                enemydmg.append(letter)
            ''.join(enemydmg)
            while letter != '-':
                enemyhealth.append(letter)
            ''.join(enemyhealth)
            while letter != '-':
                dropped_weapon.append(letter)
            ''.join(dropped_weapon)
            while letter != '-':
                dropped_rarity.append(letter)
            ''.join(dropped_rarity)
            while letter != '-':
                increase_dmg.append(letter)
            ''.join(increase_dmg)
            if type(increase_dmg) != int:
                return '''Invalid Code'''
            while letter != '-':
                turn.append(letter)
            ''.join(turn)
            if turn != 1 and turn != 2:
                return '''Invalid Code'''
            while letter != '-':
                training.append(letter)
            ''.join(training)
            if training != False and training != True:
                return '''Invalid Code'''
            while letter != '-':
                first_time_spiral.append(letter)
            ''.join(first_time_spiral)
            if first_time_spiral != False and first_time_spiral != True:
                return '''Invalid Code'''
            while letter != '-':
                first_time_spiral2.append(letter)
            ''.join(first_time_spiral2)
            if first_time_spiral2 != False and first_time_spiral2 != True:
                return '''Invalid Code'''
            while letter != '-':
                first_time_spiral3.append(letter)
            ''.join(first_time_spiral3)
            if first_time_spiral3 != False and first_time_spiral3 != True:
                return '''Invalid Code'''
            while letter != '-':
                spiral.append(letter)
            ''.join(spiral)
            if spiral != False and spiral != True:
                return '''Invalid Code'''
            while letter != '-':
                first_time_ww3.append(letter)
            ''.join(first_time_ww3)
            if first_time_ww3 != False and first_time_ww3 != True:
                return '''Invalid Code'''
            while letter != '-':
                minions_killed.append(letter)
            ''.join(minions_killed)
            if type(minions_killed) != int:
                return '''Invalid Code'''
            while letter != '-':
                velvet_alive.append(letter)
            ''.join(velvet_alive)
            if velvet_alive != False and velvet_alive != True:
                return '''Invalid Code'''
            while letter != '-':
                god_guy_alive.append(letter)
            ''.join(god_guy_alive)
            if god_guy_alive != False and god_guy_alive != True:
                return '''Invalid Code'''
            while letter != '-':
                zombie_killer_alive.append(letter)
            ''.join(zombie_killer_alive)
            if zombie_killer_alive != False and zombie_killer_alive != True:
                return '''Invalid Code'''
            while letter != '-':
                first_time_trialI.append(letter)
            ''.join(first_time_trialI)
            if first_time_trialI != False and first_time_trialI != True:
                return '''Invalid Code'''
            while letter != '-':
                first_time_trialII.append(letter)
            ''.join(first_time_trialII)
            if first_time_trialII != False and first_time_trialII != True:
                return '''Invalid Code'''
            while letter != '-':
                trial_i.append(letter)
            ''.join(trial_i)
            if trial_i != False and trial_i != True:
                return '''Invalid Code'''
            while letter != '-':
                trial_ii.append(letter)
            ''.join(trial_ii)
            if trial_ii != False and trial_ii != True:
                return '''Invalid Code'''