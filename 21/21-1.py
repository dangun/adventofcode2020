
with open('input.txt') as f:
    data = f.readlines()

allergens = {}
ingredient_count = {}

for line in data:
    line = line.strip().split(' (contains ')
    ingredients = line[0].split(' ')
    for ingredient in ingredients:
        if ingredient not in ingredient_count:
            ingredient_count[ingredient] = 1
        else: 
            ingredient_count[ingredient] += 1

    for allergen in line[1][:-1].split(', '):
        if allergen not in allergens:
            allergens[allergen] = set(ingredients)
        else: 
            allergens[allergen] = allergens[allergen] & set(ingredients)
possible_allergens = set().union(*allergens.values())
non_allergen_count = sum([ingredient_count[key] for key in set(ingredient_count).difference(possible_allergens)])

print(f'Answer {non_allergen_count}')