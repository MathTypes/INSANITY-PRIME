from flask import Flask, render_template, request, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import random, time
from save_code_enter import save_code_func

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# rarities: [absolutely terrible, not as bad as you, decent, fine, rare, epic, legendary, mythic,
# divine, godly, what the heck how did you get this, alright you're a hacker]

absolutely_terrible = ['Training Sword', 'Wired Sword', 'Nothing Sword', 'Nonexistent Sword', 'Fight Me, Me Bow', 'Useless Bow', 'You Bow', 'Noob Scythe']
not_as_bad_as_you = ['Dummy Sword', 'Game Sword', 'Listening Sword', 'Deaf Sword', 'Mistake Sword', 'Dumb Bow', 'Not as bad as you Bow', 'U suk Bow', 'Fake Scythe', 'Lmao Scythe']
decent = ['Decent Sword', 'Ok Sword', 'Name every way to say decent Sword', 'Welcome Sword', 'Weirdly good Sword', 'Bow of Hummdinger', 'Wow Bow', 'Existence Bow', 'Duolingo', 'You', 'Terribly decent Bow', 'Scythe']
fine = ['Eye Sword', 'I was mistaken about this Sword', 'Listen Sword', 'Good Sword', 'Chicken Sword', 'Bow Bow', 'Fine Bow', 'Wow its good Bow', 'Im done with the jokes Bow', 'Al Capone Scythe', 'WAIT Scythe']
rare = ['Wow dis rare Sword', 'Rare Sword', 'Stone Sword', 'Sword', 'Joke Bow', 'Francais Bow', 'France Bow', 'French Bow', 'Slaughter Bow', 'Harold Scythe', 'Scythe of Jokes']
epic = ['Excellent Sword', 'Peashooter Bow', 'Red Stinger Bow']
legendary = ['Not You', 'Cracker', 'Deafen', 'Professional Demon', 'Not A Flamethrower', 'Alvin and Jere']
mythic = ['The Prime\'s Crusher', 'Death\'s Destroyer', 'Demolisher']
divine = ['Drill of Divan', 'Murder Scythe', 'You\'re trash kid']
what_the_heck_how_did_you_get_this = ['Ray of God', 'Ray of Death']
alright_ur_a_hacker = ['?sudo']

absolutely_terrible_dict = {
    'Training Sword':10,
    'Wired Sword':11,
    'Nothing Sword':12,
    'Nonexistent Sword':13,
    'Fight Me, Me Bow':14,
    'Useless Bow':15,
    'You Bow':16,
    'Noob Scythe':17,
}

not_as_bad_as_you_dict = {
    'Dummy Sword':200,
    'Game Sword':22,
    'Listening Sword':24,
    'Deaf Sword':26,
    'Mistake Sword':28,
    'Dumb Bow':30,
    'Not as bad as you Bow':32,
    'U suk Bow': 34,
    'Fake Scythe': 36,
    'Lmao Scythe': 38,
}

decent_dict = {
    'Decent Sword':50,
    'Ok Sword':55,
    'Name every way to say decent Sword':60,
    'Welcome Sword':65,
    'Weirdly good Sword':70,
    'Bow of Hummdinger':75,
    'Wow Bow':80,
    'Existence Bow':85,
    'Duolingo':90,
    'You':95,
    'Terribly decent Bow':100,
    'Scythe':105,
}

fine_dict = {
    'Eye Sword':200,
    'I was mistaken about this Sword':210,
    'Listen Sword':220,
    'Good Sword':230,
    'Chicken Sword':240,
    'Bow Bow':250,
    'Fine Bow':260,
    'Wow its good Bow':270,
    'Im done with the jokes Bow':280,
    'Al Capone Scythe':290,
    'WAIT Scythe':300,
}

rare_dict = {
    'Wow dis rare Sword':500,
    'Rare Sword':525,
    'Stone Sword':550,
    'Sword':575,
    'Joke Bow':600,
    'French Bow':625,
    'France Bow':650,
    'Francais Bow':675,
    'Slaughter Bow':700,
    'Harold Scythe':725,
    'Scythe of Jokes':750,
}

epic_dict = {
    'Excellent Sword':2500,
    'Peashooter Bow':2600,
    'Red Stinger Bow':2700,
}

legendary_dict = {
    'Not You':10000,
    'Cracker':10500,
    'Deafen':11000,
    'Professional Demon':11500,
    'Not A Flamethrower':12000,
    'Alvin and Jere':12500,
}

mythic_dict = {
    'The Prime\'s Crusher':50000,
    'Death\'s Destroyer':51000,
    'Demolisher':52000,
}

divine_dict = {
    'Drill of Divan':250000,
    'Murder Scythe':500000,
    'You\'re trash kid':1000000,
}

what_the_heck_how_did_you_get_this_dict = {
    'Ray of God':5000000,
    'Ray of Death':50000000,
}

alright_ur_a_hacker_dict = {
    '?sudo':float('inf')
}

rarities = ['filler', 'absolutely terrible', 'not as bad as you', 'decent', 'fine', 'rare', 'epic', 'legendary', 'mythic', 'divine', 'what the heck how did you get this', 'alright ur a hacker']

username = ''
password = ''
numberid = 0

coins = 0
gems = 0

level = 0.00
health = 100 + level * 10
weapon = 'None'
rarity = 'None'

rarity_num = 0

first_time = True

dmg = 0
critchance = 1
critdmg = 1.00

use_health = health

enemy = ''
enemydmg = 0
enemyhealth = 100
use_enemyhealth = enemyhealth

dropped_weapon = 'None'
dropped_rarity = "yeah it doesn't exist"
dropped_rarity_num = 0
increase_dmg = 0

turn = 1

training = False

first_time_spiral = True
first_time_spiral2 = True
first_time_spiral3 = True
spiral = False
first_time_ww3 = True

minions_killed = 0
velvet_alive = True
god_guy_alive = True

zombie_killer_alive = True
first_time_trialI = True
first_time_trialII = True
trial_i = False
trial_ii = False

save_code = ''


zombie_killer_alive = True

@app.route('/assets/<path:path>', methods=["GET"])
def hub_music(path):
    return send_from_directory("assets", path)

@app.route('/', methods=['POST', 'GET'])
def enterinfo():
    global username, password, numberid, coins, gems, level, health, weapon, rarity, dmg, critchance, critdmg, enemy, enemyhealth, use_enemyhealth, enemydmg, dropped_weapon, dropped_rarity, increase_dmg, turn, first_time, training, first_time_spiral, first_time_spiral2, first_time_spiral3, first_time_ww3, trial_i, trial_ii, first_time_trialI, first_time_trialII, first_time_ww3, save_code
    if request.method == 'POST':
        username = ''
        password = ''
        numberid = 0

        coins = 0
        gems = 0

        level = 0.00
        health = 100 + level * 10
        weapon = 'None'
        rarity = 'None'

        rarity_num = 0

        dmg = 0
        critchance = 1
        critdmg = 1.00

        use_health = health

        enemy = ''
        enemydmg = 0
        enemyhealth = 100
        use_enemyhealth = enemyhealth

        dropped_weapon = 'None'
        dropped_rarity = "yeah it doesn't exist"
        dropped_rarity_num = 0
        increase_dmg = 0

        turn = 1

        training = False

        first_time_spiral = True
        first_time_spiral2 = True
        first_time_spiral3 = True
        spiral = False
        first_time_ww3 = True

        minions_killed = 0
        velvet_alive = True
        god_guy_alive = True

        zombie_killer_alive = True
        first_time_trialI = True
        first_time_trialII = True
        trial_i = False
        trial_ii = False


        zombie_killer_alive = True

        if first_time is True:
            first_time = False
            while True:
                save_code = str(username) + '-' + str(password) + '-' + str(numberid) + '-' + str(coins) + '-' + str(gems) + '-' + str(
level) + '-' + str(health) + '-' + str(weapon) + '-' + str(rarity) + '-' + str(first_time) + '-' + str(dmg) + '-' + str(critchance) + '-' + str(
critdmg) + '-' + str(enemy) + '-' + str(enemydmg) + '-' + str(enemyhealth) + '-' + str(dropped_weapon) + '-' + str(dropped_rarity) + '-' + str(
increase_dmg) + '-' + str(turn) + '-' + str(training) + '-' + str(first_time_spiral) + '-' + str(first_time_spiral2) + '-' + str(first_time_spiral3) + '-' + str(
spiral) + '-' + str(first_time_ww3) + '-' + str(minions_killed) + '-' + str(velvet_alive) + '-' + str(god_guy_alive) + '-' + str(zombie_killer_alive) + '-' + str(
first_time_trialI) + '-' + str(first_time_trialII) + '-' + str(trial_i) + '-' + str(trial_ii) + '-' + str(coins)
                time.sleep(5)
                print(save_code)

        username = request.form.get('username')
        password = request.form.get('password')
        numberid = (len(username) + len(password)) * 2 + 1
        print(numberid)
        if username == '' or password == '':
            return render_template("login_error.html")
        if username == 'Jere' and password == 'tomato_yummy' or username == 'Oliver' and password == 'yerpsh96':
            password2 = input("Enter admin password: ")
            if password2 == "yerpsh":
                gems = float('inf')
                coins = float('inf')
                critchance = 100
                weapon = '?sudo'
                rarity = 'admin power'
                dmg = float('inf')
                critdmg = float('inf')
                return render_template("signedin.html", username=username, password=password)
            else:
                return '''FAKE ADMIN ALERT!!!'''
        return render_template("signedin.html", username=username, password=password)
    return render_template('username.html')


@app.route('/save', methods=['POST', 'GET'])
def save():
    if request.method == 'POST':
        return render_template('save.html', save_code=save_code)
    return render_template('save.html')

@app.route('/entersave', methods=['POST', 'GET'])
def entersave():
    global username, password, numberid, coins, gems, level, health, weapon, rarity, first_time, dmg, critchance, critdmg, enemy, enemydmg, enemyhealth, dropped_rarity
    global dropped_weapon, increase_dmg, turn, training, first_time_spiral, first_time_spiral2, first_time_spiral3, spiral, first_time_ww3, minions_killed, velvet_alive
    global god_guy_alive, zombie_killer_alive, first_time_trialI, first_time_trialII, trial_i, trial_ii
    if request.method == 'POST':
        save_code2 = request.form.get('save_code')

        current_numberid = numberid

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
        save_num = 1
        for letter in save_code2: 
            if save_num == 34:
                if letter == 'T' and first13 is True:
                    trial_ii = True
                    first13 = False

                elif letter == 'F' and first13 is True:
                    trial_ii = False
                    first13 = False
                elif first13 is True:
                    while True:
                        return '''You suk!'''
            elif save_num == 33:
                first13 = True
                if letter == 'T' and first12 is True:
                    trial_i = True
                    first12 = False

                elif letter == 'F' and first12 is True:
                    trial_i = False
                    first12 = False
                elif first12 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 32:
                first12 = True
                if letter == 'T' and first11 is True:
                    first_time_trialII = True
                    first11 = False

                elif letter == 'F' and first10 is True:
                    first_time_trialII = False
                    first11 = False
                elif first11 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 31:
                first11 = True
                if letter == 'T' and first10 is True:
                    first_time_trialI = True
                    first10 = False

                elif letter == 'F' and first10 is True:
                    first_time_trialI = False
                    first10 = False
                elif first10 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 30:
                first10 = True
                if letter == 'T' and first9 is True:
                    zombie_killer_alive = True
                    first9 = False

                elif letter == 'F' and first9 is True:
                    zombie_killer_alive = False
                    first9 = False
                elif first9 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 29:
                first9 = True
                if letter == 'T' and first8 is True:
                    god_guy_alive = True
                    first8 = False

                elif letter == 'F' and first8 is True:
                    god_guy_alive = False
                    first8 = False
                elif first8 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 28:
                first8 = True
                if letter == 'T' and first7 is True:
                    velvet_alive = True
                    first7 = False

                elif letter == 'F' and first7 is True:
                    velvet_alive = False
                    first7 = False
                elif first7 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 27:
                if letter == '-':
                    minions_killed = ''.join(num for num in minions_killed)
                    save_num += 1
                else:
                    minions_killed.append(letter)
            elif save_num == 26:
                first7 = True
                if letter == 'T' and first6 is True:
                    first_time_ww3 = True
                    first6 = False

                elif letter == 'F' and first6 is True:
                    first_time_ww3 = False
                    first6 = False
                elif first6 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 25:
                first6 = True
                if letter == 'T' and first5 is True:
                    spiral = True
                    first5 = False

                elif letter == 'F' and first5 is True:
                    spiral = False
                    first5 = False
                elif first5 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 24:
                first5 = True
                if letter == 'T' and first4 is True:
                    first_time_spiral3 = True
                    first4 = False

                elif letter == 'F' and first4 is True:
                    first_time_spiral3 = False
                    first4 = False
                elif first4 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 23:
                first4 = True
                if letter == 'T' and first3 is True:
                    first_time_spiral2 = True
                    first3 = False

                elif letter == 'F' and first3 is True:
                    first_time_spiral2 = False
                    first3 = False
                elif first3 is True:
                    while True:
                        return '''Save Manipulation!'''
            elif save_num == 22:
                first3 = True
                if letter == 'T' and first2 is True:
                    first_time_spiral = True
                    first2 = False

                elif letter == 'F' and first2 is True:
                    first_time_spiral = False
                    first2 = False
                elif first2 is True:
                    while True:
                        return '''Save Manipulation!'''
            ### Stop Point up
            elif save_num == 21:
                first2 = True
                if letter == 'T' and first1 is True:
                    training = True
                    first1 = False

                elif letter == 'F' and first1 is True:
                    training = False
                    first1 = False
                elif first1 is True:
                    while True:
                        return '''Save Manipulation!'''
                else:
                    pass
            elif save_num == 20:
                first1 = True
                turn = 1
            elif save_num == 19:
                if letter == '-':
                    increase_dmg = ''.join(num for num in increase_dmg)
                    if increase_dmg == []:
                        increase_dmg = 0
                    save_num += 1
                else:
                    increase_dmg.append(letter) 
            elif save_num == 18:
                if letter == '-':
                    dropped_rarity = ''.join(str(num) for num in dropped_rarity)
                    save_num += 1
                else:
                    dropped_rarity.append(letter)
            elif save_num == 17:
                if letter == '-':
                    dropped_weapon = ''.join(str(num) for num in dropped_weapon)
                    save_num += 1
                else:
                    dropped_weapon.append(letter)
            elif save_num == 16:
                if letter == '-':
                    enemyhealth = ''.join(num for num in enemyhealth)
                    if enemyhealth == []:
                        enemyhealth = 0
                    save_num += 1
                else:
                    enemyhealth.append(letter)
            elif save_num == 15:
                if letter == '-':
                    enemydmg = ''.join(num for num in enemydmg)
                    save_num += 1
                else:
                    enemydmg.append(letter)
            elif save_num == 14:
                if letter == '-':
                    enemy = ''.join(str(num) for num in enemy)
                    save_num += 1
                else:
                    enemy.append(letter)
            elif save_num == 13:
                if letter == '-':
                    critdmg = ''.join(num for num in critdmg)
                    save_num += 1
                else:
                    critdmg.append(letter)
            elif save_num == 12:
                if letter == '-':
                    critchance = ''.join(num for num in critchance)
                    save_num += 1
                else:
                    critchance.append(letter)
            elif save_num == 11:
                if letter == '-':
                    dmg = ''.join(num for num in dmg)
                    if dmg == []:
                        dmg = 0
                    save_num += 1
                else:
                    dmg.append(letter)
            elif save_num == 10:
                save_num += 1
            elif save_num == 9:
                if letter == '-':
                    rarity = ''.join(str(num) for num in rarity)
                    save_num += 1
                else:
                    rarity.append(letter)
            elif save_num == 8:
                if letter == '-':
                    weapon = ''.join(str(num) for num in weapon)
                    save_num += 1
                else:
                    weapon.append(letter)
            elif save_num == 7:
                if letter == '-':
                    health = ''.join(num for num in health)
                    if health == []:
                        health = 0
                    save_num += 1
                else:
                    health.append(letter)
            elif save_num == 6:
                if letter == '-':
                    level = ''.join(num for num in level)
                    save_num += 1
                else:
                    level.append(letter)
            elif save_num == 5:
                if letter == '-':
                    gems = ''.join(num for num in gems)
                    if gems == []:
                        gems = 0
                    save_num += 1
                else:
                    gems.append(letter)
            elif save_num == 4:
                if letter == '-':
                    coins = ''.join(num for num in coins)
                    if coins == []:
                        coins = 0
                    save_num += 1
                else:
                    coins.append(letter)
            elif save_num == 3:
                if letter == '-':
                    numberid = ''.join(num for num in numberid)
                    save_num += 1
                else:
                    numberid.append(letter)
            elif save_num == 2:
                if letter == '-':
                    password = ''.join(str(num) for num in password)
                    save_num += 1
                else:
                    password.append(letter)
            elif save_num == 1:
                if letter == '-':
                    username = ''.join([str(num) for num in username])
                    save_num += 1
                else:
                    username.append(letter)
            
        return render_template('entersave.html', success='Success!')
    return render_template('entersave.html', success='Failed...')


@app.route('/start', methods=['POST', 'GET'])
def hub():
    if request.method == 'POST':
        return render_template('start.html', username=username)
    return render_template('hub.html', username=username, level=level, weapon=weapon, rarity=rarity, coins=coins, gems=gems, dmg=dmg)




# Remove the glitch where the dropped sword stays so if you fight op guy and lost, kill minion and get op loot
# Update 4/29/23: Fixed! - Arrow
# Nice! - DeathBlade

@app.route('/fight', methods=['POST', 'GET'])
def fight():
    global level, use_health, health, coins, gems, weapon, use_enemyhealth, enemyhealth, use_health
    global dmg, enemydmg, increase_dmg, dropped_weapon, dropped_rarity, turn, rarity, minions_killed
    global velvet_alive, god_guy_alive, zombie_killer_alive, trial_i, trial_ii
    
    xp_increase = enemyhealth * enemydmg / ((level+1)*100)
    coin_increase = enemyhealth * enemydmg / 1000
    gem_increase = round(enemyhealth * enemydmg / 10000)
    if gem_increase > 2500:
        gem_increase = 2500
    if coin_increase > 10000000:
        coin_increase = 10000000
    if request.method == 'POST':
        if use_enemyhealth < dmg+1:
            level += round(xp_increase, 2)
            health = 100 + level*10
            use_health = health
            coins += coin_increase
            gems += gem_increase
            turn = 1
            if enemy == 'Minion':
                minions_killed += 1
            elif enemy == 'Velvet' and velvet_alive == True:
                dropped_weapon = 'Fine Sword'
                dropped_rarity = 'fine'
                velvet_alive = False
            elif enemy == 'God Servant' and god_guy_alive == True:
                dropped_weapon = 'Godly Bad Sword'
                dropped_rarity = 'fine'
                god_guy_alive = False
            elif enemy == 'Zombie Killer' and zombie_killer_alive == True:
                dropped_weapon = 'Zombie Killer Sword'
                dropped_rarity = 'rare'
                zombie_killer_alive = False
            elif enemy == 'Trial Master I' and trial_i == False:
                dropped_weapon = 'Trial I Sword'
                dropped_rarity = 'rare'
                trial_i = True
            elif enemy == 'Trial Master II' and trial_ii == False:
                dropped_weapon = 'Trial II Sword'
                dropped_rarity = 'weak epic'
                trial_ii = True
            if dropped_weapon != weapon and dropped_weapon != None and increase_dmg > dmg:
                weapon = dropped_weapon
                dmg = increase_dmg
                rarity = dropped_rarity
                dropped_weapon = None
                dropped_rarity = None
                return render_template("fightsuccess.html", coin_increase=str(coin_increase), gem_increase=str(gem_increase), xp_increase=str(round(xp_increase, 2)), weapon=weapon, rarity=rarity)
            return render_template("fightsuccessnoweapon.html", coin_increase=str(coin_increase), gem_increase=str(gem_increase), xp_increase=str(round(xp_increase, 2)))
        elif use_health < enemydmg:
            coins += coin_increase / 10
            level += round(xp_increase / 100, 2)
            health = 100 + level*10
            use_health = health
            turn = 1
            return render_template("fighterror.html", coin_increase=str(coin_increase/10), xp_increase=str(round(xp_increase/100, 2)))
        else:
            if turn % 2 == 1:
                crithit = random.randint(1, 100)
                use_dmg = round(dmg * random.randint(0.8, 1.2))
                if crithit <= critchance:
                    use_enemyhealth -= use_dmg * critdmg + use_dmg
                else:
                    use_enemyhealth -= use_dmg
                turn += 1
                return render_template('fight.html', health=use_health, enemy=enemy, enemyhealth=use_enemyhealth, username=username)

            else:
                use_health -= round(enemydmg * random.randint(0.8, 1.2))
                turn += 1
                return render_template('fight.html', health=use_health, enemy=enemy, enemyhealth=use_enemyhealth, username=username)
    return render_template('fight.html', health=use_health, enemy=enemy, enemyhealth=use_enemyhealth, username=username)




@app.route('/gemgacha')
def gemgacha():
    return render_template('gemgacha.html')




@app.route('/gacha')
def gacha1():
    return render_template('gacha1.html')



@app.route('/gachagood')
def gachagood():
    return render_template('gachagood.html')

@app.route('/gemgacha1', methods=['POST', 'GET'])
def gemgachadraw1():
    global weapon, gems, rarity, dmg
    if gems < 250:
        return render_template("gachaerror.html")
    gems -= 250
    for items in range(1):
        gacha = random.randint(39, 1000)
        if gacha >= 500:
            item = random.randint(0, 11)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'
                weapon = decent[item]
                dmg = decent_dict[weapon]
            else:
                pass
        elif gacha >= 250 and gacha <= 499:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 125 and gacha <= 249:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 75 and gacha <= 124:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 50 and gacha <= 74:
            item = random.randint(0, 5)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
        elif gacha >= 40 and gacha <= 49:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic':
                rarity = 'mythic'
                weapon = mythic[item]
                dmg = mythic_dict[weapon]
            else:
                pass
        elif gacha == 39:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic' or rarity == 'divine':
                rarity = 'divine'
                weapon = divine[item]
                dmg = divine_dict[weapon]
            else:
                pass
    return render_template("gachasuccess.html", rarity=rarity, weapon=weapon)

@app.route('/gemgacha10', methods=['POST', 'GET'])
def gemgachadraw10():
    global weapon, gems, rarity, dmg
    if gems < 2000:
        return render_template("gachaerror10.html")
    gems -= 2000
    for items in range(10):
        gacha = random.randint(39, 1000)
        if gacha >= 500:
            item = random.randint(0, 11)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'
                weapon = decent[item]
                dmg = decent_dict[weapon]
            else:
                pass
        elif gacha >= 250 and gacha <= 499:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 125 and gacha <= 249:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 75 and gacha <= 124:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 50 and gacha <= 74:
            item = random.randint(0, 5)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
        elif gacha >= 40 and gacha <= 49:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic':
                rarity = 'mythic'
                weapon = mythic[item]
                dmg = mythic_dict[weapon]
            else:
                pass
        elif gacha == 39:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic' or rarity == 'divine':
                rarity = 'divine'
                weapon = divine[item]
                dmg = divine_dict[weapon]
            else:
                pass
    return render_template("gachasuccess.html", rarity=rarity, weapon=weapon)

@app.route('/gemgacha100', methods=['POST', 'GET'])
def gemgachadraw100():
    global weapon, gems, rarity, dmg
    if gems < 19000:
        return render_template("gachaerror100.html")
    gems -= 19000
    for items in range(100):
        gacha = random.randint(39, 1000)
        if gacha >= 500:
            item = random.randint(0, 11)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'
                weapon = decent[item]
                dmg = decent_dict[weapon]
            else:
                pass
        elif gacha >= 250 and gacha <= 499:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 125 and gacha <= 249:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 75 and gacha <= 124:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 50 and gacha <= 74:
            item = random.randint(0, 5)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
        elif gacha >= 40 and gacha <= 49:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic':
                rarity = 'mythic'
                weapon = mythic[item]
                dmg = mythic_dict[weapon]
            else:
                pass
        elif gacha == 39:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic' or rarity == 'divine':
                rarity = 'divine'
                weapon = divine[item]
                dmg = divine_dict[weapon]
            else:
                pass
    return render_template("gachasuccess.html", rarity=rarity, weapon=weapon)

@app.route('/weapongacha10', methods=['POST', 'GET'])
def gachadraw10():
    global weapon, coins, rarity, dmg
    if coins < 3000:
        return render_template("gachaerror10.html")
    coins -= 3000
    for items in range(10):
        gacha = random.randint(375, 10000)
        if gacha >= 5000:
            item = random.randint(0, 7)
            if rarity == 'None' or rarity == 'absolutely terrible':
                rarity = 'absolutely terrible'
                weapon = absolutely_terrible[item]
                dmg = absolutely_terrible_dict[weapon]
            else:
                pass
        elif gacha >= 2500 and gacha <= 4999:
            item = random.randint(0, 9)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you':
                rarity = 'not as bad as you'
                weapon = not_as_bad_as_you[item]
                dmg = not_as_bad_as_you_dict[weapon]
            else:
                pass
        elif gacha >= 1250 and gacha <= 2499:
            item = random.randint(0, 11)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'
                weapon = decent[item]
                dmg = decent_dict[weapon]
            else:
                pass
        elif gacha >= 750 and gacha <= 1249:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 500 and gacha <= 749:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 400 and gacha <= 499:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 375 and gacha <= 399:
            item = random.randint(0, 5)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
    return render_template("gachasuccess.html", rarity=rarity, weapon=weapon)

@app.route('/weapongacha100', methods=['POST', 'GET'])
def gachadraw100():
    global weapon, coins, rarity, dmg
    if coins < 29000:
        return render_template("gachaerror100.html")
    coins -= 29000
    for items in range(100):
        gacha = random.randint(375, 10000)
        if gacha >= 5000:
            item = random.randint(0, 7)
            if rarity == 'None' or rarity == 'absolutely terrible':
                rarity = 'absolutely terrible'
                weapon = absolutely_terrible[item]
                dmg = absolutely_terrible_dict[weapon]
            else:
                pass
        elif gacha >= 2500 and gacha <= 4999:
            item = random.randint(0, 9)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you':
                rarity = 'not as bad as you'
                weapon = not_as_bad_as_you[item]
                dmg = not_as_bad_as_you_dict[weapon]
            else:
                pass
        elif gacha >= 1250 and gacha <= 2499:
            item = random.randint(0, 11)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'
                weapon = decent[item]
                dmg = decent_dict[weapon]
            else:
                pass
        elif gacha >= 750 and gacha <= 1249:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 500 and gacha <= 749:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 400 and gacha <= 499:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 375 and gacha <= 399:
            item = random.randint(0, 5)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
    return render_template("gachasuccess.html", rarity=rarity, weapon=weapon)


@app.route('/weapongacha1', methods=['POST', 'GET'])
def gachadraw1():
    global weapon, coins, rarity, dmg
    if coins < 500:
        return render_template("gachaerror.html")
    coins -= 500
    for items in range(1):
        gacha = random.randint(375, 10000)
        if gacha >= 5000:
            item = random.randint(0, 7)
            if rarity == 'None' or rarity == 'absolutely terrible':
                rarity = 'absolutely terrible'
                weapon = absolutely_terrible[item]
                dmg = absolutely_terrible_dict[weapon]
            else:
                pass
        elif gacha >= 2500 and gacha <= 4999:
            item = random.randint(0, 9)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you':
                rarity = 'not as bad as you'
                weapon = not_as_bad_as_you[item]
                dmg = not_as_bad_as_you_dict[weapon]
            else:
                pass
        elif gacha >= 1250 and gacha <= 2499:
            item = random.randint(0, 11)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'
                weapon = decent[item]
                dmg = decent_dict[weapon]
            else:
                pass
        elif gacha >= 750 and gacha <= 1249:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 500 and gacha <= 749:
            item = random.randint(0, 10)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 400 and gacha <= 499:
            item = random.randint(0, 2)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 375 and gacha <= 399:
            item = random.randint(0, 5)
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
    return render_template("gachasuccess.html", rarity=rarity, weapon=weapon)






@app.route('/gachagood1', methods=['POST', 'GET'])
def gachagood1():
    global weapon, coins, rarity, dmg
    if coins < 1500:
        return render_template("gachaerror.html")
    coins -= 1500
    for items in range(1):
        gacha = random.randint(1, 10000)
        dmgincrease = 0
        if gacha >= 5000 and gacha <= 9999:
            item = random.randint(0, 9)
            dmgincrease += 2
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you':
                rarity = 'not as bad as you'
                weapon = not_as_bad_as_you[item]
                dmg = not_as_bad_as_you_dict[weapon]
            else:
                pass
        elif gacha >= 2500 and gacha <= 4999:
            item = random.randint(0, 11)
            dmgincrease += 5
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'                
                weapon = decent[item]
                dmg = decent_dict[item]
            else:
                pass
        elif gacha >= 1250 and gacha <= 2499:
            item = random.randint(0, 10)
            dmgincrease += 10
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 250 and gacha <= 1249:
            item = random.randint(0, 10)
            dmgincrease += 25
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 40 and gacha <= 249:
            item = random.randint(0, 2)
            dmgincrease += 100
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 2 and gacha <= 39:
            item = random.randint(0, 5)
            dmgincrease += 500
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
        elif gacha == 1:
            item = random.randint(0, 2)
            dmgincrease += 2500
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic':
                rarity = 'mythic'
                weapon = mythic[item]
                dmg = mythic_dict[weapon]
            else:
                pass
        dmg += dmgincrease
    return render_template("gachagoodsuccess.html", weapon=weapon, rarity=rarity, dmgincrease=dmgincrease) 

@app.route('/gachagood10', methods=['POST', 'GET'])
def gachagood10():
    global weapon, coins, rarity, dmg
    if coins < 10000:
        return render_template("gachaerror10.html")
    coins -= 10000
    for items in range(10):
        gacha = random.randint(1, 10000)
        dmgincrease = 0
        if gacha >= 5000 and gacha <= 9999:
            item = random.randint(0, 9)
            dmgincrease += 2
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you':
                rarity = 'not as bad as you'
                weapon = not_as_bad_as_you[item]
                dmg = not_as_bad_as_you_dict[weapon]
            else:
                pass
        elif gacha >= 2500 and gacha <= 4999:
            item = random.randint(0, 11)
            dmgincrease += 5
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'                
                weapon = decent[item]
                dmg = decent_dict[item]
            else:
                pass
        elif gacha >= 1250 and gacha <= 2499:
            item = random.randint(0, 10)
            dmgincrease += 10
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 250 and gacha <= 1249:
            item = random.randint(0, 10)
            dmgincrease += 25
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 40 and gacha <= 249:
            item = random.randint(0, 2)
            dmgincrease += 100
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 2 and gacha <= 39:
            item = random.randint(0, 5)
            dmgincrease += 500
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
        elif gacha == 1:
            item = random.randint(0, 2)
            dmgincrease += 2500
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic':
                rarity = 'mythic'
                weapon = mythic[item]
                dmg = mythic_dict[weapon]
            else:
                pass
        dmg += dmgincrease
    return render_template("gachagoodsuccess.html", weapon=weapon, rarity=rarity, dmgincrease=dmgincrease) 


@app.route('/gachagood100', methods=['POST', 'GET'])
def gachagood100():
    global weapon, coins, rarity, dmg
    if coins < 99000:
        return render_template("gachaerror100.html")
    coins -= 99000
    for items in range(100):
        gacha = random.randint(1, 10000)
        dmgincrease = 0
        if gacha >= 5000 and gacha <= 9999:
            item = random.randint(0, 9)
            dmgincrease += 2
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you':
                rarity = 'not as bad as you'
                weapon = not_as_bad_as_you[item]
                dmg = not_as_bad_as_you_dict[weapon]
            else:
                pass
        elif gacha >= 2500 and gacha <= 4999:
            item = random.randint(0, 11)
            dmgincrease += 5
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent':
                rarity = 'decent'                
                weapon = decent[item]
                dmg = decent_dict[item]
            else:
                pass
        elif gacha >= 1250 and gacha <= 2499:
            item = random.randint(0, 10)
            dmgincrease += 10
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine':
                rarity = 'fine'
                weapon = fine[item]
                dmg = fine_dict[weapon]
            else:
                pass
        elif gacha >= 250 and gacha <= 1249:
            item = random.randint(0, 10)
            dmgincrease += 25
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare':
                rarity = 'rare'
                weapon = rare[item]
                dmg = rare_dict[weapon]
            else:
                pass
        elif gacha >= 40 and gacha <= 249:
            item = random.randint(0, 2)
            dmgincrease += 100
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic':
                rarity = 'epic'
                weapon = epic[item]
                dmg = epic_dict[weapon]
            else:
                pass
        elif gacha >= 2 and gacha <= 39:
            item = random.randint(0, 5)
            dmgincrease += 500
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary':
                rarity = 'legendary'
                weapon = legendary[item]
                dmg = legendary_dict[weapon]
            else:
                pass
        elif gacha == 1:
            item = random.randint(0, 2)
            dmgincrease += 2500
            if rarity == 'None' or rarity == 'absolutely terrible' or rarity == 'not as bad as you' or rarity == 'decent' or rarity == 'fine' or rarity == 'rare' or rarity == 'epic' or rarity == 'legendary' or rarity == 'mythic':
                rarity = 'mythic'
                weapon = mythic[item]
                dmg = mythic_dict[weapon]
            else:
                pass
        dmg += dmgincrease
    return render_template("gachagoodsuccess.html", weapon=weapon, rarity=rarity, dmgincrease=dmgincrease) 




@app.route('/training', methods=['POST', 'GET'])
def trainingground():
    global training, weapon, rarity, coins, gems, enemy, enemydmg, enemyhealth, use_enemyhealth, dropped_weapon, dropped_rarity, increase_dmg, dmg
    if training is True:
        return render_template("trainingerror.html")
    weapon = 'Training Sword'
    rarity = 'absolutely terrible'
    dmg = 10
    enemy = 'Puppet'
    enemydmg = 1
    enemyhealth = 100
    use_enemyhealth = enemyhealth
    dropped_weapon = 'Dummy Sword'
    dropped_rarity = 'not as bad as you'
    increase_dmg = 15
    training = True
    gems += 50
    coins += 3000
    return render_template('training.html')

@app.route('/spiral', methods=['POST', 'GET'])
def spiral():
    global enemy, enemyhealth, use_enemyhealth, enemydmg, training, gems, first_time_spiral
    if training is False:
        return render_template("spiralerror.html")
    enemydmg = 20
    enemy = 'Minion'
    enemyhealth = 150
    use_enemyhealth = enemyhealth
    newareareward = ''
    if first_time_spiral is True:
        gems += 15
        first_time_spiral = False
        newareareward = '[NEW AREA!: The Spiral of Doom, reward: 15 gems]'
    return render_template('spiral.html', newareareward=newareareward)

@app.route('/spiralf2', methods=['POST', 'GET'])
def sprial2():
    global enemy, enemydmg, enemyhealth, use_enemyhealth, gems, dropped_weapon, dropped_rarity, increase_dmg, first_time_spiral2
    if minions_killed < 5:
        return render_template("spiral2error.html")
    enemydmg = 50
    enemy = 'Velvet'
    enemyhealth = 500
    increase_dmg = 225
    if velvet_alive == False:
        dropped_weapon = None
        dropped_rarity = None
    use_enemyhealth = enemyhealth
    newareareward = ''
    if first_time_spiral2 is True:
        gems += 25
        first_time_spiral2 = False
        newareareward = '[NEW AREA!: Floor 2 of the Spiral of Doom, reward: 25 gems]'
    return render_template('spiral2.html', newareareward=newareareward)

@app.route('/spiralf3', methods=['POST', 'GET'])
def sprial3():
    global enemy, enemydmg, enemyhealth, use_enemyhealth, gems, spiral, dropped_weapon, dropped_rarity, increase_dmg, coins, first_time_spiral3
    if velvet_alive == True:
        return render_template("spiral3error.html")
    enemydmg = 100
    enemy = 'God Servant'
    enemyhealth = 1000
    use_enemyhealth = enemyhealth
    increase_dmg = 250
    if god_guy_alive == False:
        dropped_weapon = None
        dropped_rarity = None
        spiral = True
    newareareward = ''
    if first_time_spiral3 is True:
        coins += 1000
        gems += 50
        first_time_spiral3 = False
        newareareward = '[NEW AREA: Floor 3 of the Spiral of Doom, reward: 1000 coins and 50 gems!]'
    return render_template('spiral3.html', newareareward=newareareward)

@app.route('/ww3', methods=['POST', 'GET'])
def ww3():
    global enemy, coins, enemyhealth, enemydmg, use_enemyhealth, dropped_weapon, dropped_rarity, increase_dmg, first_time_ww3
    enemy = 'Zombie Killer'
    enemyhealth = 2000
    enemydmg = 100
    use_enemyhealth = enemyhealth
    increase_dmg = 575
    newareareward = ''
    if first_time_ww3 is True:
        coins += 3000
        first_time_ww3 = False
        newareareward = '[NEW AREA: WW3 Battlefield, reward: 3000 coins!]'
    if zombie_killer_alive is False:
        dropped_weapon = None
        dropped_rarity = None
        return render_template("ww3success.html")
    return render_template('ww3.html', username=username, newareareward=newareareward)

@app.route('/trial1', methods=['POST', 'GET'])
def trial_1():
    global dropped_weapon, dropped_rarity, increase_dmg, enemy, enemyhealth, enemydmg, use_enemyhealth, first_time_trialI, coins, level
    increase_dmg = 650
    enemy = 'Trial Master I'
    enemyhealth = 10000
    use_enemyhealth = enemyhealth
    enemydmg = 100
    newareareward = ''
    if first_time_trialI is True:
        coins += 5000
        level += 5
        first_time_trialI = False
        newareareward = '[NEW AREA! Trial I Battlefield, reward: 5000 coins]'
    if trial_i == True:
        dropped_weapon = None
        dropped_rarity = None
        return render_template("trial_isuccess.html")
    return render_template('trial_i.html', newareareward=newareareward)

@app.route('/trial2', methods=['POST', 'GET'])
def trial_2():
    global dropped_weapon, dropped_rarity, increase_dmg, enemy, enemyhealth, enemydmg, use_enemyhealth, first_time_trialII, coins, level, dmg
    increase_dmg = 1500
    enemy = 'Trial Master II'
    enemyhealth = 3000
    use_enemyhealth = enemyhealth
    enemydmg = 5000
    newareareward = ''
    if first_time_trialII is True:
        coins += 7500
        dmg += 100
        first_time_trialII = False
        newareareward = '[NEW AREA! Trail II Dojo, reward: 7500 coins]'
    if trial_ii == True:
        dropped_weapon = None
        dropped_rarity = None
        return render_template('trial_iisuccess.html')
    return render_template('trial_ii.html', newareareward=newareareward)



if __name__ == "__main__":
    app.secret_key = 'XL2901'
    app.run(debug=True)
