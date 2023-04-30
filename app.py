from flask import Flask, render_template, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import random, time

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
    'Noneistent Sword':13,
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
    'Terribly Decent Bow':100,
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

first_time = False

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
trial_i = False

zombie_killer_alive = True

@app.route('/', methods=['POST', 'GET'])
def enterinfo():
    global username, password, numberid, coins, gems, level, health, weapon, rarity, dmg, critchance, critdamage, enemy, enemyhealth, use_enemyhealth, enemydmg, dropped_weapon, dropped_rarity, increase_dmg, turn, first_time, training, first_time
    if request.method == 'POST':
        if first_time == True:
            first_time = False
            while True:
                for rarity in rarities:
                    if rarity == dropped_rarity:
                        dropped_rarity_num = rarities.index(rarity)
                    pass
                for rarity1 in rarities:
                    if rarity1 == rarity:
                        rarity_num = rarities.index(rarity)
                    pass
        username = ''
        password = ''
        numberid = 0

        coins = 0
        gems = 0

        level = 0.00
        health = 100 + level * 10
        weapon = 'None'
        rarity = 'None'
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
        increase_dmg = 0

        turn = 1

        training = False

        first_time = False

        username = request.form.get('username')
        password = request.form.get('password')
        numberid = (len(username) + len(password)) * 2 + 1
        print(numberid)
        if username == '' or password == '' or username == 'Username' or password == 'Password':
            return '''Error: username or password field is empty.<br>
                   <a href="/">Retry</a>'''
        return f'''Sucessfully signed in. Your username is {username} and your password is {password}.<br>
                <form method="POST" action="/start" class="inline">
                    <button type="submit" value="Start your adventure!" class="link-button">
                        Start your adventure!
                    </button>
                </form>'''
    return render_template('username.html')





@app.route('/start', methods=['POST', 'GET'])
def hub():
    if request.method == 'POST':
        return render_template('start.html', username=username)
    return render_template('hub.html', username=username, level=level, weapon=weapon, rarity=rarity, coins=coins, gems=gems, dmg=dmg)




# Remove the glitch where the dropped sword stays so if you fight op guy and lost, kill minion and get op loot

@app.route('/fight', methods=['POST', 'GET'])
def fight():
    global level, use_health, health, coins, gems, weapon, use_enemyhealth, enemyhealth, use_health
    global dmg, enemydmg, increase_dmg, dropped_weapon, dropped_rarity, turn, rarity, minions_killed
    global velvet_alive, god_guy_alive, zombie_killer_alive, trial_i
    
    xp_increase = enemyhealth * enemydmg / ((level+1)*100)
    coin_increase = enemyhealth * enemydmg / 10
    gem_increase = round(enemyhealth * enemydmg / 1000)
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
            elif enemy == 'Velvet':
                velvet_alive = False
            elif enemy == 'God Servant':
                god_guy_alive = False
            elif enemy == 'Zombie Killer':
                zombie_killer_alive = False
            elif enemy == 'Trial Master I':
                trial_i = True
            if dropped_weapon != weapon and dropped_weapon != None and dropped_rarity_num >= rarity_num:
                weapon = dropped_weapon
                dmg = increase_dmg
                rarity = dropped_rarity
                dropped_weapon = None
                dropped_rarity = None
                return f'''You win! You gained {str(coin_increase)} coins and {str(gem_increase)} gems! You also gained {str(round(xp_increase, 2))} xp!<br>
                    You also get a {weapon} which rarity is {rarity}!<br>
                    <a href="/start">Back to home</a>'''
            return f'''You win! You gained {str(coin_increase)} coins and {str(gem_increase)} gems! You also gained {str(round(xp_increase, 2))} xp!<br>
                    <a href="/start">Back to home</a>'''
        elif use_health < enemydmg:
            coins += coin_increase / 100
            level += round(xp_increase / 100, 2)
            health = 100 + level*10
            use_health = health
            turn = 1
            return f'''You lost. However, we will still give you {str(coin_increase/100)} coins and {str(round(xp_increase/100, 2))} xp.<br>
                    <a href="/start">Back to home</a>'''
        else:
            if turn % 2 == 1:
                crithit = random.randint(1, 100)
                if crithit <= critchance:
                    use_enemyhealth -= dmg * critdmg + dmg
                else:
                    use_enemyhealth -= dmg
                turn += 1
                return render_template('fight.html', health=use_health, enemy=enemy, enemyhealth=use_enemyhealth, username=username)

            else:
                use_health -= enemydmg
                turn += 1
                return render_template('fight.html', health=use_health, enemy=enemy, enemyhealth=use_enemyhealth, username=username)
    return render_template('fight.html', health=use_health, enemy=enemy, enemyhealth=use_enemyhealth, username=username)




@app.route('/gacha')
def gacha1():
    return render_template('gacha1.html')



@app.route('/gachagood')
def gachagood():
    return render_template('gachagood.html')


@app.route('/weapongacha10', methods=['POST', 'GET'])
def gachadraw10():
    global weapon, coins, rarity, dmg
    if coins < 3000:
        return '''You cannot afford a 10 pull.<br>
                <a href="/gacha">Back</a>'''
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
    return '''You got your items<br>
           <a href="/start">Go back</a>'''

@app.route('/weapongacha1', methods=['POST', 'GET'])
def gachadraw1():
    global weapon, coins, rarity, dmg
    if coins < 500:
        return '''You cannot afford a gacha pull.<br>
                <a href="/gacha">Back</a>'''
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
    return '''You got your items<br>
           <a href="/start">Go back</a>'''






@app.route('/gachagood1', methods=['POST', 'GET'])
def gachagood1():
    global weapon, coins, rarity, dmg
    if coins < 1500:
        return '''You cannot afford a gacha pull.<br>
                <a href="/gacha">Back</a>'''
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
    return f'''You got your items and +{dmgincrease} dmg!<br> 
           <a href="/start">Go back</a>''' 

@app.route('/gachagood10', methods=['POST', 'GET'])
def gachagood10():
    global weapon, coins, rarity, dmg
    if coins < 10000:
        return '''You cannot afford a 10 pull.<br>
                <a href="/gacha">Back</a>'''
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
    return f'''You got your items and +{dmgincrease} dmg!<br> 
           <a href="/start">Go back</a>''' 







@app.route('/training', methods=['POST', 'GET'])
def trainingground():
    global training, weapon, rarity, coins, gems, enemy, enemydmg, enemyhealth, use_enemyhealth, dropped_weapon, dropped_rarity, increase_dmg, dmg
    if training is True:
        return '''You have already completed the training camp.<br>
               <a href="/start">Back</a>'''
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
        return '''You have not gone into the training grounds yet.<br>
               <a href="/start">Back</a>'''
    enemydmg = 20
    enemy = 'Minion'
    enemyhealth = 150
    use_enemyhealth = enemyhealth
    if first_time_spiral is True:
        gems += 30
        first_time_spiral = False
        return '''(Glenthrosh): Well, well, well. Look at what we have here. A ... soul.<br>
                  (God of Murder): Then let him die. Our minions are enough.<br>
                  [NEW AREA!: The Spiral of Doom, reward: 30 gems]<br>
                  <a href="/fight">Fight Minion 1</a><br>
                  <a href="/fight">Fight Minion 2</a><br>
                  <a href="/fight">Fight Minion 3</a><br>
                  <a href="/fight">Fight Minion 4</a><br>
                  <a href="/fight">Fight Minion 5</a><br>
                  <a href="/spiralf2">Go to floor 2</a><br>
                  <a href="/start">Back</a><br>'''
    return render_template('spiral.html')

@app.route('/spiralf2', methods=['POST', 'GET'])
def sprial2():
    global enemy, enemydmg, enemyhealth, use_enemyhealth, gems, dropped_weapon, dropped_rarity, increase_dmg, first_time_spiral2
    if minions_killed < 5:
        return '''You have not killed 5 minions yet.<br>
               <a href="/spiral">Back</a>'''
    enemydmg = 50
    enemy = 'Velvet'
    enemyhealth = 500
    dropped_weapon = 'Fine Sword'
    dropped_rarity = 'fine'
    increase_dmg = 225
    if velvet_alive == False:
        dropped_weapon = None
        dropped_rarity = None
    use_enemyhealth = enemyhealth
    if first_time_spiral2 is True:
        gems += 25
        first_time_spiral2 = False
        return '''This is the 2cd floor of the Spiral of Doom.<br>
                  [NEW AREA!: Floor 2 of the Spiral of Doom, reward: 25 gems]<br>
                  (VELVET MAN): AHA! I see you there. You. Will. Die.<br>
                  <a href="/fight">FIGHT HIM</a><br>
                  <a href="/spiralf3">Go to the final floor!</a><br>
                  <a href="/spiral">Back</a><br>'''
    return render_template('spiral2.html')

@app.route('/spiralf3', methods=['POST', 'GET'])
def sprial3():
    global enemy, enemydmg, enemyhealth, use_enemyhealth, gems, spiral, dropped_weapon, dropped_rarity, increase_dmg, coins, first_time_spiral3
    if velvet_alive == True:
        return '''You have not killed Velvet yet.<br>
               <a href="/spiralf2">Back</a>'''
    enemydmg = 100
    enemy = 'God Servant'
    enemyhealth = 2500
    use_enemyhealth = enemyhealth
    dropped_weapon = 'Godly Bad Sword'
    dropped_rarity = 'fine'
    increase_dmg = 250
    if god_guy_alive == False:
        dropped_weapon = None
        dropped_rarity = None
        spiral = True
    if first_time_spiral3 is True:
        coins += 1000
        gems += 500
        first_time_spiral3 = False
        return '''This is the FINAL FLOOR of the Spiral of Doom!<br>
                  [NEW AREA: Floor 3 of the Spiral of Doom, reward: 1000 coins and 50 gems!]
                  (GOD SERVANT): Hi! Time to fight.<br>
                  <a href="/fight">Fight him</a><br>
                  <a href="/gachagood">Go to the Spiral Gacha</a><br>
                  <a href="/spiralf2">Back</a><br>'''
    return render_template('spiral3.html')

@app.route('/ww3', methods=['POST', 'GET'])
def ww3():
    global enemy, coins, enemyhealth, enemydmg, use_enemyhealth, dropped_weapon, dropped_rarity, increase_dmg, first_time_ww3
    enemy = 'Zombie Killer'
    enemyhealth = 5000
    enemydmg = 100
    use_enemyhealth = enemyhealth
    dropped_weapon = 'Zombie Killer Sword'
    dropped_rarity = 'rare'
    increase_dmg = 575
    if first_time_ww3 is True:
        coins += 3000
        first_time_ww3 = False
        return f'''World. War. III!!!<br>
                   You are fighting in WW3! But is it as it seems?<br>
                   [NEW AREA: WW3 Battlefield, reward: 3000 coins!]<br>
                   (God of Death): Fight this enemy, will you, { username }?<br>
                   (Zombie Killer): BLERSHIVICH FOR THE MURDER GOD!<br>
                   <a href="/fight">Fight Zombie Killer</a><br>
                   <a href="/start">Back</a><br>
                   *After killing the zombie killer, come back to this page.<br>'''
    if zombie_killer_alive is False:
        dropped_weapon = None
        dropped_rarity = None
        return '''(God of Death): Good!<br>
                  (God of Death): You are can enter trials now!<br>
                  <a href="/trial1">Trials</a><br>
                  <a href="/start">Back</a>'''
    return render_template('ww3.html', username=username)

@app.route('/trial1', methods=['POST', 'GET'])
def trial_1():
    global dropped_weapon, dropped_rarity, increase_dmg, enemy, enemyhealth, enemydmg, use_enemyhealth, first_time_trialI, coins, level
    dropped_weapon = 'Trial I Sword'
    dropped_rarity = 'rare'
    increase_dmg = 650
    enemy = 'Defense Master'
    enemyhealth = 50000
    use_enemyhealth = enemyhealth
    enemydmg = 100
    if first_time_trialI is True:
        coins += 3000
        level += 5
        first_time_trialI = False
        return '''[NEW AREA! Trial I Battlefield, reward: 3000 coins]<br>
                  The first Trial of many!<br>
                  THE DEFENSE TRAIL!<br>
                  Defeat the Defense Trial Master<br>
                  <a href="/fight">Fight Him!</a><br>
                  <a href="/ww3">Back</a>'''
    if trial_i == True:
        dropped_weapon = None
        dropped_rarity = None
        return '''(Defense Master): Yay!!!<br>
                  (Defense Master): You can now move on to Trial II!<br>
                  <a href="/trial2">Next Trial</a><br>
                  <a href="/ww3">Back</a>'''
    return render_template('trial_i.html')



if __name__ == "__main__":
    app.secret_key = 'XL2901'
    app.run(debug=True)
