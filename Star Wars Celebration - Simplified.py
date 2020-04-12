'''
Types in Star Wars character and says how many films they've been in
'''

import urllib.request
import urllib.parse
import json


character = 'Luke Skywalker'
characterParse = character.replace(' ','%20')

urlCharacter = "https://challenges.hackajob.co/swapi/api/people/?search={characterParse}".format(characterParse=characterParse)
h = urllib.request.urlopen(urlCharacter)
data = json.loads(h.read().decode(h.info().get_param('charset') or 'utf-8'))
count = 0

for result in data['results']:
	if character == result['name']:

		for filmName in result['films']:
			count += 1

output = count
return output
