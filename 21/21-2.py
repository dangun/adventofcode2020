
with open('input.txt') as f:
    data = f.readlines()

allergens = {}

for line in data:
    line = line.strip().split(' (contains ')
    ingredients = line[0].split(' ')
    for allergen in line[1][:-1].split(', '):
        if allergen not in allergens:
            allergens[allergen] = set(ingredients)
        else: 
            allergens[allergen] = allergens[allergen] & set(ingredients)

remove_list = set([list(v)[0] for k,v in allergens.items() if len(v) == 1])
while any([len(x) > 1 for x in allergens.values()]):
    for k,v in allergens.items():
        if len(v) > 1: 
            allergens[k] = v.difference(remove_list)
            if len(allergens[k]) == 1:
                remove_list.add(list(allergens[k])[0])

print(f'Answer: {",".join([value[1].pop() for value in sorted(allergens.items())])}')

