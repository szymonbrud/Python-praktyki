import random

print('Losowanie drużyn \n')
numberOfTeams = int(input('Ilośc drużyn: '))
playersStr = input('Podaj zawodników po przecinkach: ')

arrOfPlayers = playersStr.split(',')

teams = []

for i in range(0, numberOfTeams):
    teams.append([])


index = 0

random.shuffle(arrOfPlayers)

for player in arrOfPlayers:
    teams[index].append(player)

    if index == numberOfTeams - 1:
        index = 0
    else:
        index += 1

for index, team in enumerate(teams):

    teammates = ",".join(team)

    print(f'Drużyna {index + 1} to: {teammates}')
