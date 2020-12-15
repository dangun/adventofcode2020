import re

def buildbagdict(rules):
    bags_dict = {}
    for rule in rules:
        bag, contain = rule.split(' contain ', 2)
        if contain == 'no other':
            continue
        contain = contain.split(', ')
        for bag_type in contain:
            if bag_type[2:] not in bags_dict:
                bags_dict[bag_type[2:]] = []
            bags_dict[bag_type[2:]].append(bag)
    return bags_dict

def recursivecount(bag_type, bags_set, bags_dict):
    for bag in bags_dict[bag_type]:
        bags_set.add(bag)
        if bag in bags_dict:
            recursivecount(bag, bags_set, bags_dict)

rules = []
with open('input.txt') as f:
    for rule in f:
        rules.append(re.sub(r' (bag)s?|\.$|\n', '', rule))

bags_dict = buildbagdict(rules)
bags_set = set()
recursivecount('shiny gold', bags_set, bags_dict)

print(f'# possible outermost bags for a \"shiny gold\" bag: {len(bags_set)}')