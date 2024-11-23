""" Programme réalisé par Chabrot Guillaume Blonde Louis 1G1 """
from random import randint
import sys

print("""\033[1;32m
---------------------------------------------------------------------------------------------
       _______  ___   _  ___   _______  ___   ______   ______    ___   _______  _______ 
      |       ||   | | ||   | |  _    ||   | |      | |    _ |  |   | |       ||       |
      |  _____||   |_| ||   | | |_|   ||   | |  _    ||   | ||  |   | |____   ||____   |
      | |_____ |      _||   | |       ||   | | | |   ||   |_||_ |   |  ____|  | ____|  |
      |_____  ||     |_ |   | |  _   | |   | | |_|   ||    __  ||   | | ______|| ______|
       _____| ||    _  ||   | | |_|   ||   | |       ||   |  | ||   | | |_____ | |_____ 
      |_______||___| |_||___| |_______||___| |______| |___|  |_||___| |_______||_______|
---------------------------------------------------------------------------------------------
""")
salleTab = [{'name': 'salon', 'xy': '11', 'info': 'Que la chance soit avec toi', 'lock': False, 'color': '32'}, {'name': 'entrée', 'xy': '01', 'info': 'L\'unique porte de la maison est verrouillé', 'lock': False, 'color': '32'}, {'name': 'cuisine', 'xy': '12', 'info': '', 'lock': False, 'color': '32'}, {'name': 'couloir', 'xy': '13', 'info': '', 'lock': False, 'color': '32'}, {'name': 'salle de bain', 'xy': '23', 'info': '', 'lock': False, 'color': '32'}, {'name': 'chambre', 'xy': '03', 'info': '', 'lock': False, 'color': '32'}, {'name': 'garage', 'xy': '14', 'info': '', 'lock': True, 'color': '32'}, {'name': 'jardin', 'xy': '10', 'info': 'nnssoeoeba', 'lock': False, 'color': '32'}, {'name': 'toilettes', 'xy': '21', 'info': '', 'lock': False, 'color': '32'}]
ennemieTab = [{'name': '-1', 'salle': 'garage', 'xy': '14'}]
randomPlayer = randint(0, 5)
salle = salleTab[randomPlayer]
player = {'salle': salleTab[randomPlayer], 'xy': salleTab[randomPlayer]['xy']}
sallePlayer = salle['name']
print(f'\033[1;36mTu es dans \'{sallePlayer}\'')

def lb_set_map(salle):
    if lb_access(-10) == True:
        finish_game = '33'
    else:
        finish_game = '31'
    for i in range(0, len(salleTab)):
        if salleTab[i]['name'] == salle['name']:
            salleTab[i]['color'] = '35'
        else:
            salleTab[i]['color'] = '32'
    the_map = f"""
                  \033[1;{salleTab[-1]['color']}mToilettes       \033[1;{salleTab[-5]['color']}mSalle de bain\033[1;32m
                      |                |
              \033[1;{salleTab[-2]['color']}mJardin\033[1;32m-\033[1;{salleTab[0]['color']}mSalon\033[1;32m-\033[1;{salleTab[2]['color']}mCuisine\033[1;32m-\033[1;{salleTab[3]['color']}mCouloir\033[1;32m-\033[1;{salleTab[-3]['color']}mGarage\033[1;32m
                      |                |
                    \033[1;{salleTab[1]['color']}mEntrée          \033[1;{salleTab[-4]['color']}mChambre\033[1;{finish_game}m
                    ||||||
              """
    return the_map
def lb_position():
    sallePlayer = player['salle']['name']
    print(f'\033[1;36mTu es dans \'{sallePlayer}\'')
    return
def lb_access(cote):
    i = 0
    while i < len(salleTab):
        if salleTab[i]['lock'] == True:
            return False
        i += 1
    if ennemieTab == [] and player['salle']['name'] == 'entrée' and cote == -10:
        return True
    return False
def lb_mouvement(cote):
    i = 0
    if lb_access(cote) == True:
        lb_position()
        print('\033[1;33mTu as fini le jeu !')
        sys.exit(0)
        return 'dehors'
    while i < len(salleTab):
        if int(player['xy']) + cote == int(salleTab[i]['xy']):
            sallePlayer = salleTab[i]['name']
            if salleTab[i]['lock'] == False:
                player['xy'] = salleTab[i]['xy']
                player['salle'] = salleTab[i]
                
                print(f'\033[1;36mTu es dans le \'{sallePlayer}\'')
                j = 0
                while j < len(ennemieTab):
                    if ennemieTab[j]['xy'] == player['xy']:
                        lb_combat(j)
                    j += 1
                return salleTab[i]['name']
            else:
                print(f'\033[1;31m\'{sallePlayer}\' est fermé')
                return player['salle']
        i += 1
    print('\033[1;31mtape pas dans le mur')
    return player['salle']
def lb_combat(ennemie_num):
    score = 0
    bot = 0
    tabChoice = ['pierre', 'papier', 'ciseaux']
    manche = 1
    i = 1
    while i <= manche:
        print(f'\033[1;37m\n-------\nManche {i}\n-------')
        joueur = input('\033[1;36m[1] : Pierre\n\033[1;34m[2] : Papier\n\033[1;35m[3] : Ciseaux\033[1;37m\nTon choix : ')
        if joueur.isdigit() == False or int(joueur) > 3 or int(joueur) < 0:
            print('Saisie incorrect !')
            continue
        joueur = int(joueur) - 1
        ennemie = randint(0,2)
        print(f'Tu as choisi {tabChoice[joueur]}\033[1;37m')
        if joueur == ennemie - 1 or joueur == ennemie + 2:
            print(f'\033[1;31mTu as perdu la manche {i}', end=' ')
            bot += 1
        elif joueur == ennemie - 2 or joueur == ennemie + 1:
            print(f'\033[1;32mTu as gagné la manche {i}', end=' ')
            score += 1
        elif joueur == ennemie:
            print(f'Egalité a la manche {i}', end=' ')
            manche += 1
        i += 1
    if score >= bot:
        print(f'\n\033[1;37;42mVictoire !\033[0m')
        ennemieTab.pop(ennemie_num)
    else:
        print(f'\n\033[1;37;41mPerdu !\033[0m')
        sys.exit(0)
def lb_unlock(lieu):
    j = 0
    while j < len(salleTab):
        if salleTab[j]['name'] == lieu['name']:
            salleTab[j]['lock'] = False
            salleOpen = salleTab[j]['name']
            return f'\033[1;33m\'{salleOpen}\' est ouvert'
        j += 1
    return
def lb_set_ennemie(nbr_ennemie):
    k = 0
    while k < nbr_ennemie:
        randomEnnemie = randint(0, len(salleTab) - 1)
        if randomEnnemie == randomPlayer:
            randomEnnemie = randint(0, len(salleTab) - 1)
            continue
        ennemieTab.append({'name': f'{k}', 'salle': salleTab[randomEnnemie]['name'], 'xy': salleTab[randomEnnemie]['xy']})
        k += 1
    return
def lb_info_salle(salle):
    information = salle['info']
    if information == '':
        print('\033[1;36mRien a signalé ici !')
    else:
        print(f'\033[1;36mInfo sur la salle : {information}')

lb_set_ennemie(randint(2, 5))
while True:
    the_map = lb_set_map(player['salle'])
    action = input('\033[1;34m')
    if action == 'q' or action == 'quit' or action == 'exit':
        print('\033[1;36mAu revoir !\033[0m')
        break
    elif action == 'n':
        salle = lb_mouvement(10)
    elif action == 'e':
        salle = lb_mouvement(1)
    elif action == 'o':
        salle = lb_mouvement(-1)
    elif action == 's':
        salle = lb_mouvement(-10)
    elif action == 'm':
        lb_position()
    elif action == 'map':
        print(the_map)
    elif action == '!':
        lb_info_salle(player['salle'])
    elif action == 'h' or action == 'help':
        print("""\033[1;32m
----------------------------------------------------------------------------------------
              'q' pour quitter le jeu
              'n' pour aller au nord
              's' pour aller au sud
              'e' pour aller a l'est
              'o' pour aller a l'ouest
              'm' pour localiser la piece dans laquelle vous êtes
              'map' pour afficher la carte
              '!' pour afficher les informations sur la salle
              'h' pour avoir de l'aide
----------------------------------------------------------------------------------------
              """)
    elif action == 'nnssoeoeba':
        if salle == 'toilettes':
            print(lb_unlock(salleTab[6]))
        else:
            print('\033[1;33mTu n\'es pas au bonne endroit')
    else:
        print('\033[1;31mSa veut rien dire')
