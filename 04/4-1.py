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

    def isvalid(self):
        if (self.byr is not None and 
            self.iyr is not None and 
            self.eyr is not None and 
            self.hgt is not None and 
            self.hcl is not None and 
            self.ecl is not None and 
            self.pid is not None):
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

with open('input.txt') as f:
    text = f.read()

passport_list = extract_passports(text)

valid_count = 0
for passport in passport_list:
    if passport.isvalid():
        valid_count += 1

print(f'# of valid passports: {valid_count}')
