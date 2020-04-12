import urllib.request
import urllib.parse
import json

team = "arsenal"
team = team.lower()

JSONFile = 'https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json'
h = urllib.request.urlopen(JSONFile)
data = json.loads(h.read().decode(h.info().get_param('charset') or 'utf-8'))
goals = 0
teamNumber = 0

for result in data["rounds"]:
	for i in result["matches"]:
		if i["team1"]["key"].lower() == team:
			goals += i["score1"]
		if i["team2"]["key"].lower() == team:
			goals += i["score2"]

print(goals)
			
			
