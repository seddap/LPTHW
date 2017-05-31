#Exercise 39: Dictionaries, Oh Lovely Dictionaries

def things_list():
    things = ['a', 'b', 'c', 'd']
    print (things[1])
    things[1] = 'z'
    print (things[1])
    print (things)

things_list()
#OUTPUT:
# b
# z
# ['a', 'z', 'c', 'd']

def stuff_dic():
    stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
    print (stuff['name'])
    print (stuff['age'])
    print (stuff['height'])
    stuff['city'] = "SF"
    print (stuff['city'])

    stuff [1] = "Wow"
    stuff [2] = "Neat"
    print (stuff[1])
    print (stuff[2])
    print (stuff)

    del stuff['city']
    del stuff[1]
    del stuff[2]

    print (stuff)

stuff_dic()

#OUTPUT
# Zed
# 39
# 74
# SF
# Wow
# Neat
# {1: 'Wow', 2: 'Neat', 'height': 74, 'name': 'Zed', 'age': 39, 'city': 'SF'}
# {'height': 74, 'name': 'Zed', 'age': 39}
