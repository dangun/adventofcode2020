import os
import re

def buildbagdict(rules):
    bags_dict = {}
    for rule in rules:
        bag, contain = rule.split(' contain ', 2)
        bags_dict[bag.strip()] = {}
        if contain.strip() == 'no other':
            continue
        contain = contain.split(', ')
        for bag_type in contain:
            bag_type.strip()
            bags_dict[bag][bag_type[2:]] = int(bag_type[0])
    return bags_dict

def recursivecount(bag_type, bag_counter, bags_dict):
    sum = 0
    for bag in bags_dict[bag_type]:
        sum += bags_dict[bag_type][bag] * recursivecount(bag, bag_counter, bags_dict)
        sum += bags_dict[bag_type][bag]
    return bag_counter + sum

rules = []
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    for rule in f:
        rules.append(re.sub(r' (bag)s?|\.$|\n', '', rule))

bags_dict = buildbagdict(rules)
bag_counter = 0
bag_counter = recursivecount('shiny gold', bag_counter, bags_dict)

print(f'# of bags for one \"shiny gold\" bag: {bag_counter}')