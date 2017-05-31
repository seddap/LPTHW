#Exercise 39: Dictionaries, Oh Lovely Dictionaries

states = {
    'Rheinland-Pfalz': 'RLP',
    'Nordrhein-Westfalen': 'NRW',
    'Hamburg': 'HAM',
    'Bayern': 'BAY'
}

cities = {
    'RLP': 'Mainz',
    'NRW': 'Cologne',
    'HAM': 'Hamburg',
    'BAY': 'Munich'
}

print ("-" * 10)
print ("RLP State has: ", cities['RLP'])
print ("-" * 10)
print ("Bayerns abbreviation is: ", states['Bayern'])
print ("-" * 10)
print ("NRW has: ", cities[states['Nordrhein-Westfalen']])
print ("-" * 10)
for state, abbrev in list(states.items()):
    print ("{st} state is abbreviated {ab}".format(st = state, ab = abbrev))
    print ("and has the city {ci}.".format(ci = cities[abbrev]))


#pydoc list
#matches keys to values
#orderless, not possible to sort, no good for sequences
# class collections.OrderedDict([items])
    #Return an instance of a dict subclass, supporting the usual dict
    #methods. An OrderedDict is a dict that remembers the order that
    #keys were first inserted. If a new entry overwrites an existing
    #entry, the original insertion position is left unchanged.
    #Deleting an entry and reinserting it will move it to the end.
    #https://docs.python.org/3/library/collections.html#collections.OrderedDict
