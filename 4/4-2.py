import os
import re

class Passport:
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

    def byrisvalid(self):
        if 1920 <= int(self.byr) <= 2002:
            return True
        return False
        
    def iyrisvalid(self):
        if 2010 <= int(self.iyr) <= 2020:
            return True
        return False

    def eyrisvalid(self):
        if 2020 <= int(self.eyr) <= 2030:
            return True
        return False

    def hgtisvalid(self):
        if self.hgt[-2:] == 'cm' and 150 <= int(self.hgt[:-2]) <= 193:
            return True
        elif self.hgt[-2:] == 'in' and 59 <= int(self.hgt[:-2]) <= 76:
            return True
        return False

    def hclisvalid(self):
        if len(self.hcl) == 7 and self.hcl[0] == '#':
            if re.fullmatch(r'[0-9a-f]{6}', self.hcl[1:]):
                return True
        return False

    def eclisvalid(self):
        eyec = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if self.ecl in eyec:
            return True
        return False

    def pidisvalid(self):
        if len(self.pid) == 9 and re.fullmatch(r'[0-9]{9}', self.pid):
            return True
        return False

    def isvalid(self):
        if (self.byr and 
            self.iyr and 
            self.eyr and 
            self.hgt and 
            self.hcl and 
            self.ecl and 
            self.pid and 
            self.byrisvalid() and 
            self.iyrisvalid() and 
            self.eyrisvalid() and 
            self.hgtisvalid() and 
            self.hclisvalid() and 
            self.eclisvalid() and 
            self.pidisvalid()):
            return True 
        return False


def extract_passports(text):
    passport_list = []
    passports_strings = text.split('\n\n')

    for passport_string in passports_strings:
        passport = Passport()
        passport_values = re.split('\n| ' , passport_string)
        for passport_value in passport_values:
            if not passport_value: # empty string
                continue
            variable, value = passport_value.split(':')
            setattr(passport, variable, value)
        passport_list.append(passport)
    return passport_list

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/' + 'input.txt') as f:
    text = f.read()

passport_list = extract_passports(text)

valid_count = 0
for passport in passport_list:
    if passport.isvalid():
        valid_count += 1

print(f'# of valid passports: {valid_count}')
