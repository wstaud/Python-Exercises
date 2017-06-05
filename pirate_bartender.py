import random

questions = {
	'strong': 'Do ye like yer drinks strong?',
	'salty': 'Do ye like it with a salty tang?',
	'bitter': 'Are ye a lubber who likes it bitter?',
	'sweet': 'Would ye like a bit of sweetness with your poison?',
	'fruity': 'Are ye one for a fruity finish?',
}
ingredients = {
	'strong': ["glug of rum", "slug of whisky", "splash of gin"],
	'salty': ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	'bitter': ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	'sweet': ["sugar cube", "spoonful of honey", "spash of cola"],
	'fruity': ["slice of orange", "dash of cassis", "cherry on top"],
}

# Prompts user for input on what they like
def promptUser():
	responses = {
		'strong': False,
		'salty': False,
		'bitter': False,
		'sweet': False,
		'fruity': False,
	}

	for key, question in questions.items():
		answer = input(question)

		if key == 'strong':
			if answer == 'yes' or answer == 'y':
				responses['strong'] = True
		if key == 'salty':
			if answer == 'yes' or answer == 'y':
				responses['salty'] = True
		if key == 'bitter':
			if answer == 'yes' or answer == 'y':
				responses['bitter'] = True
		if key == 'sweet':
			if answer == 'yes' or answer == 'y':
				responses['sweet'] = True
		if key == 'fruity':
			if answer == 'yes' or answer == 'y':
				responses['fruity'] = True

	return createRecipe(responses)

# Creates a random recipe
def createRecipe(responses):
	drink = []

	if responses['strong'] == True:
		drink.append(random.choice(ingredients['strong']))
	if responses['salty'] == True:
		drink.append(random.choice(ingredients['salty']))
	if responses['bitter'] == True:
		drink.append(random.choice(ingredients['bitter']))
	if responses['sweet'] == True:
		drink.append(random.choice(ingredients['sweet']))
	if responses['fruity'] == True:
		drink.append(random.choice(ingredients['fruity']))

	print('Here is your drink: \n', drink)

promptUser()

