# Initialising Dictionary
players = {}

# Enter number of Players
n = int(input("Enter Number of Players "))
for i in range(n): 
    name = input("Enter Full name of Player ")
    team = input("Team of the player ")

    # Using player name as key (unique)
    players[name] = team
print(players)

# Searching by team
s = input("Enter team to be searched : ")
for i in players:
    if s == players[i]:
        print(players[i],":",i)