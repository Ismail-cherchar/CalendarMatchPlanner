teams = ["A", "B", "C", "D", "E"]

match = []

for i in range(len(teams)):
    for j in range(len(teams)):
        if teams[i] != teams[j] and teams[j] + teams[i] not in match:
            match.append(teams[i] + teams[j])

new_match = []
counter = 0
last_match = None

while counter < 10:
    for sublist in match:
        match_string = ''.join(sublist)
        if last_match is not None and any(element in last_match for element in sublist):
            continue

        if match_string not in new_match:
            new_match.append(match_string)
            counter += 1
            last_match = sublist

        if counter == 10:
            break

    if counter == 10:
        break

# Afficher new_match
for item in new_match:
    print(item)
