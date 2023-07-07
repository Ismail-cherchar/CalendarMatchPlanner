from datetime import datetime, timedelta

teams = [chr(k) for k in range(ord("A"), ord("T") + 1)]

poules = [teams[i:i+5] for i in range(0, len(teams), 5)]

matches = [[(team1, team2) for i, team1 in enumerate(poule) for team2 in poule[i+1:]] for poule in poules]

start_date = datetime.now()
current_date = start_date

def schedule_match(team, opponent):
    global current_date
    print(f"  {current_date.strftime('%d-%m-%Y')}: {opponent}")
    current_date += timedelta(days=1)

def schedule_last_match(team, opponent):
    global current_date
    print(f"  {current_date.strftime('%d-%m-%Y')}: {opponent} ")
    current_date += timedelta(days=1)

for i, poule in enumerate(poules):
    print(f"Poule {i + 1}: {', '.join(poule)}")
    for j, team in enumerate(poule):
        opponents = [opponent for opponent in poule if opponent != team]
        print(f"{team} contre :")
        
        if team == 'B' and 'A' in opponents:
            opponents.remove('A')
            opponents.append('A')

        
        if team == 'G' and 'F' in opponents:
            opponents.remove('F')
            opponents.append('F')
        
        if team == 'L' and 'K' in opponents:
            opponents.remove('K')
            opponents.append('K')
        
        if team == 'Q' and 'P' in opponents:
            opponents.remove('P')
            opponents.append('P')
        
        for opponent in opponents[:-1]:
            schedule_match(team, opponent)
        
        if team == 'B':
            schedule_last_match(team, opponents[-1])
        else:
            schedule_match(team, opponents[-1])
    
    print()
