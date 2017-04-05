# PASSWORD ATTACKER
top = ["123456", "qwe", "123", "321", "147", "123456789", "qwerty", "111111", "1234", "4321", "12345678", "123321h", "000000", "123123", "7777777", "qwertyuiop", "666666", "123qwe", "555555", "zxcvbnm", "1q2w3e", "gfhjkm", "qazwsx", "1q2w3e4r", "654321", "987654321", "121212", "zxcvbn", "777777", "1q2w3e4r5t", "qazwsxedc", "123456a", "112233", "qwe123", "ghbdtn", "159753", "123456q", "asdfgh", "1111111", "samsung", "qweasdzxc", "qwertyu", "1234qwer", "11111111", "222222", "asdfghjkl", "1qaz2wsx", "qweqwe", "1111111111", "123654", "123123123", "987654321", "12345q", "999999", "qwerty123", "123456789a", "12345a"]
name = input("Name: ")
lastname = input("Last name: ")
years = input("Years of Birds: ")
month = input("Month of birth: ")
day = input("Day of birth: ")
phone = input("Mobile phone number: ")
top100_support = input("Add support top100 in passwd? ")
idiot = input("Жертва идиот? ")

# translite method. return text
def translit(name):
    eng = ["q", 'w', "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c",
           "v", "b", "n", "m", ]
    rus = ["ю", "в", 'е', "р", "т", "й", "у", "и", "о", "п", "а", "с", "д", "ф", "г", "х", "ж", "к", "л", "з", "кс", "ц",
           "в", "б", "н", "м", ]
    for i in name:
        for j in eng:
            if (i == j):
                name = name.replace(name[name.find(i)], rus[eng.index(j)])
            if (i == j.upper()):
                name = name.replace(name[name.find(i)], rus[eng.index(j)].upper())

    return name
# mapping method. return text
def mapping(name, lang):
    eng = ["q", 'w', "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "<", ">", "`"]
    rus = ["й","ц", 'у', "к", "е", "н", "г", "ш", "щ", "з", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", "ё"]
    if (lang=="eng"):
        for i in name:
            for j in rus:
                if (i==j):
                    name = name.replace(name[name.find(i)], eng[rus.index(j)])
                if (i == j.upper()):
                    name = name.replace(name[name.find(i)], eng[rus.index(j)].upper())
    elif (lang=="rus"):
        for i in name:
            for j in eng:
                if (i==j):
                    name = name.replace(name[name.find(i)], rus[eng.index(j)])
                if (i==j.upper()):
                    name = name.replace(name[name.find(i)], rus[eng.index(j)].upper())
    return name
# mirroring text
def mirroring(name):
    if (int(idiot)==1):
        text=""
        for i in name:
            text+=name[len(name)-int(name.find(i))-1]
        return text
# some variation of text
def dispersion(text):
    text = str(text)
    allname = ["", text, text.lower(), text.upper(), text.capitalize(), text.swapcase(), translit(text), mirroring(text), mapping(text, "rus"), mapping(translit(text), "eng"), mapping(translit(text.lower()), "eng")]
    return allname
# add top password
def withtop(text):
    for i in top:
        print(str(text) + str(i))
        print(str(text) + str(i) + str(text))
        print(str(i) + str(text))
        print(str(i) + str(text) + str(i))

def yearsvar(name,lastname,year):
    return [str(name)+str(year),
            str(name)+str(int(year)%100),
            str(year) + str(name),
            str(int(year) % 100) + str(name),
            str(name)+str(lastname),
            str(lastname)+str(name),
            str(lastname)+str(name)+str(year),
            str(name)+str(lastname)+str(year),
            str(name)+str(lastname)+str(int(year)%100),
            str(name)+str(day)+str(month)+str(year),
            str(name)+str(day)+str(month)+str(int(year)%100),
            str(name)+str(day)+str(year),
            str(name)+str(day)+str(int(year)%100)]

def with_year(name):
    return [str(name)+str(years),
            str(name)+str(day)+str(month)+str(years),
            str(name)+str(day)+str(month),
            str(name)+str(day)+str(years),
            str(name)+str(int(years)%100),
            str(name)+str(day)+str(month)+str(int(years)%100),
            str(name) + str(day) + str(int(years)%100),
            str(years)+str(name),
            str(int(years)%100)+str(name)]

def attac_by_alldate(name):
    for year in range(1920, 2018):

        for month in range(1,13):
            for day in range(1,32):
                print(str(name)+str(day)+str(month)+str(year))

def top100add(text):
    if (top100_support == "1"):
        withtop(text)

if (top100_support=="1"):
    for i in top:
        print(i)

for names in dispersion(name):
    if (str(names)!=""):
        print(str(names) * 3)
        print(str(names) * 2)
    for lastnames in dispersion(lastname):
        for i in with_year(names):
            print(i)
            top100add(i)

        for i in with_year(str(names)+str(lastnames)):
            print(i)
            top100add(i)

        for i in with_year(str(lastnames)+str(names)):
            print(i)
            top100add(i)

        top100add(names)
        top100add(lastname)