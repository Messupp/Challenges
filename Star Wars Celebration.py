import urllib.request
import urllib.parse
import json

film = 'The Force Awakens'
filmURL = film.replace(' ','%20')
character = 'Poggle the Lesser'


urlFilm = "https://challenges.hackajob.co/swapi/api/films/?search={filmURL}".format(filmURL=filmURL)
f = urllib.request.urlopen(urlFilm)
data = json.loads(f.read().decode(f.info().get_param('charset') or 'utf-8'))

characterURLList = []

try:
	for result in data['results']:
		characterURLList.append(result['characters'])
except:
	numberOfFilms = 0

characterList = []
for characterURL in characterURLList[0]:
	g = urllib.request.urlopen(characterURL)
	data = json.loads(g.read().decode(g.info().get_param('charset') or 'utf-8'))
	characterList.append(data['name'])

charactersFilmsList = []

characterParse = character.replace(' ','%20')
urlCharacter = "https://challenges.hackajob.co/swapi/api/people/?search={characterParse}".format(characterParse=characterParse)
h = urllib.request.urlopen(urlCharacter)
data = json.loads(h.read().decode(h.info().get_param('charset') or 'utf-8'))
for result in data['results']:
	if character == result['name']:

		for filmName in result['films']:
			j = urllib.request.urlopen(filmName)
			data = json.loads(j.read().decode(j.info().get_param('charset') or 'utf-8'))
			charactersFilmsList.append(data['title'])

if character not in characterList:
	if len(charactersFilmsList) <= 1:
		charactersFilmsList.append('none')

characterList = sorted(characterList)
charactersFilmsList = sorted(charactersFilmsList)
characterList = ', '.join(characterList)
charactersFilmsList = ', '.join(charactersFilmsList)
output = '{film}: {characterList}; {character}: {charactersFilmsList}'.format(film=film, characterList=characterList, character=character, charactersFilmsList=charactersFilmsList)

print(output)
