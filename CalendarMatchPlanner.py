teams = ["A", "B", "C", "D", "E"] #create teams
match = [] #initiat match

#delete duplicates element in match[]
for i in range(len(teams)):
    for j in range(len(teams)):
        if teams[i] != teams[j] and teams[j] + teams[i] not in match:
            match.append(teams[i] + teams[j])

#variable set definition
new_match = []
counter = 0
last_match = []

#verification of consecutive element present in match and adding new matches to a new_list[]
while counter < 10:
    for sublist in match:
        match_string = ''.join(sublist)
        if any(element in last_match for element in sublist):
            continue

        if match_string not in new_match:
            new_match.append(match_string)
            counter += 1
            last_match = sublist

#print new_match
for item in new_match:
    print(item)
