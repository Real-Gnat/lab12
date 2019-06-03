import re
def count (f):
    number = 0
    with open ('access_log.txt', 'rt') as myfile:
        for line in f:
            if re.compile("png"or"jpg"or"gif"or"jpeg", re.IGNORECASE).search(line) != None:
                if re.compile(':\d{2}?:\d{2}?:\d{2}').search(line) != None:
                    if re.compile(':03:{}:'.format(range(5,56)) or ':04:{}:'.format(range(0,61)) or ':05:{}:'.format(range(0,61)) or ':06:{}:'.format(range(0,56))):
                        number += 1
    return number
f = open("access_log.txt","rt")
print(count(f))
f.close()
