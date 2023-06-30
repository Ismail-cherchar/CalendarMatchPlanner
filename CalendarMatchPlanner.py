# Author : Ismail CHERCHAR
# Name : CalendarMatchPlanner
# Description : Program that offers a solution for randomly dividing 5 teams into 4 pools and scheduling matches fairly over a specified calendar.
# Date : 27/06/2023

import random  # Importation du module random 
from datetime import datetime, timedelta  # importation du module datetime et timedelta

teams = [chr(k) for k in range(ord("A"), ord("T")+1)]  # Création d'une liste des équipes de l'alphabet A à T (20 équipes)
random.shuffle(teams)  # Mélange aléatoire des équipes dans la liste

poules = [teams[i:i+5] for i in range(0, len(teams), 5)]  # Création des poules en regroupant les équipes par groupe de 5

matches = [[(team1, team2) for i, team1 in enumerate(poule) for team2 in poule[i+1:]] for poule in poules]
# Création des paires de matchs pour chaque poule en combinant toutes les équipes entre elles

start_date = datetime.now()  # Récupération de la date et de l'heure 
current_date = start_date  # Initialisation de la date de départ pour les matchs

for i, poule in enumerate(poules):  # Parcours de chaque poule avec l'indice
    print(f"Poule {i + 1}: {', '.join(poule)}")  # Affichage du numéro de la poule et des équipes 
    for team in poule:  # Parcours de chaque équipe dans la poule
        opponents = [opponent for match in matches[i] for opponent in match if team in match and opponent != team]
        # Récupération des adversaires pour chaque équipe dans la poule
        print(f"{team} contre :")  # Affichage de l'équipe 
        for opponent in opponents:  # Parcours de chaque adversaire
            print(f"  {current_date.strftime('%d-%m-%Y')}: {opponent}")  # Affichage de la date et de l'adversaire
            current_date += timedelta(days=random.randint(1, 2))  # Incrémentation de la date actuelle avec un délai aléatoire de 1 ou 2 jours
    print()  # Affichage d'une ligne vide entre chaque poule
