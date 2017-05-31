#Exercise 39: Dictionaries, Oh Lovely Dictionaries

#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

#print out some cities
print ("-" * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

#print out some states
print ("-" * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print ("-" * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print ("-" * 10)
for state, abbrev in list(states.items()):
    print ("{st} is abbreviated {ab}".format(st = state, ab = abbrev))

#print every city in state
print ("-" * 10)
for abbrev, city in list(cities.items()):
    print ("{ab} has the city {ci}".format(ab = abbrev, ci = city))

#now do both at the same time
print ("-" * 10)
for state, abbrev in list(states.items()):
    print ("{st} state is abbreviated {ab}".format(st = state, ab = abbrev))
    print ("and has city {ci_ab}".format(ci_ab = cities[abbrev]))

print ("-" * 10)
#safely get a abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print ("Sorry, no Texas.")

#get a city with a default value
city = cities.get("TX", "Does not exist")
print ("The city for the state 'TX' is: {city}".format(city = city))


#Structure: states - abbreviation - cities
