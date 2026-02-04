context = 'Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X'

group = context.strip().split(';')

dictionary = {}

for i in group:
    tmp = i.strip().split(':')
    dictionary[tmp[0]] = tmp[1]

# Coords
coords = str(dictionary['Coords'])
coords = tuple(coords.strip("()").split(","))

# items
items = str(dictionary['Items'])
items = set(items.split(","))

# mission
mission = str(dictionary['Mission'])
mission = mission[5:]

# put information back
dictionary['Coords'] = coords
dictionary['Items'] = items
dictionary['Mission'] = mission

print(dictionary)