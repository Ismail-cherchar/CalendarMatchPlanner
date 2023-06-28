# Author : Ismail CHERCHAR
# Name : CalendarMatchPlanner
# Description : Program that offers a solution for randomly dividing 5 teams into 4 pools and scheduling matches fairly over a specified calendar.
# Date : 27/06/2023

import random
import calendar
import datetime

#Calendar display with current date
current_date = datetime.datetime.now()
yy = current_date.year
mm = current_date.month

print(calendar.month(yy, mm))


#Function that distributes teams into pools
def distribution_team(teams):
    random.shuffle(teams)
    poules = [[], [], [], []]
    i = 0

    while i < len(teams):
        poule_index = i % 4
        poule = poules[poule_index]
        poule.append(teams[i])
        i += 1
    
    if len(poules[0]) > 1:
        random_team = poules[0].pop(1)
        random_poule_index = random.randint(1, 3)
        poules[random_poule_index].append(random_team)
    
    return poules

teams = ["A", "B", "C", "D", "E"]
poules = distribution_team(teams)

match_dates = calendar.Calendar().itermonthdates(yy, mm)
match_dates = [date for date in match_dates if date.month == mm]

for i, poule in enumerate(poules):
    match_date = random.choice(match_dates)
    match_dates.remove(match_date)
    print("Poule", i + 1, ":", poule, "- Date du match:", str(match_date))
