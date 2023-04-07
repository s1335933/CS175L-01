#Aidan Moxham
#CS-175L-01
#World_Series

with open("WorldSeriesWinners.txt") as f:
    data = f.read().splitlines()

win_count = {}
for team in data:
    if team not in win_count:
        win_count[team] = 0
    win_count[team] += 1

alternate_names = {
    "Americans": "Boston Americans",
    "Giants": "New York Giants",
    "White Sox": "Chicago White Sox",
    "Cubs": "Chicago Cubs",
    "Pirates": "Pittsburgh Pirates",
    "Red Sox": "Boston Red Sox",
    "Reds": "Cincinnati Reds",
    "Indians": "Cleveland Indians",
    "Yankees": "New York Yankees",
    "Senators": "Washington Senators",
    "Cardinals": "St. Louis Cardinals",
    "Tigers": "Detroit Tigers",
    "Orioles": "Baltimore Orioles",
    "Mets": "New York Mets",
    "Phillies": "Philadelphia Phillies",
    "Royals": "Kansas City Royals",
    "Twins": "Minnesota Twins",
    "Blue Jays": "Toronto Blue Jays",
    "Marlins": "Florda Marlins",
    "Diamondbakcs": "Arizona Diamondbacks",
    "Angels": "Anaheim Angels",
}

while True:
    team = input("Enter the name of a team (or 'Quit' to exit): ")
    if team == "Quit":
        break
    
    if team in win_count:
        count = win_count[team]
        print(f"The {team} won the World Series {count} times between 1903 and 2009.")
    elif team in alternate_names:
        standard_name = alternate_names[team]
        count = win_count[standard_name]
        print(f"The {team} won the World Series {count} times between 1903 and 2009.")
    else:
        print(f"The {team} did not win the World Series between 1903 and 2009.")
