# PASSWORD ATTACKER
top100 = ["123456","123","321", "password","12345678","qwerty","123456789","12345","1234","111111","1234567","123123","abc123","football","monkey","letmein","696969","shadow","master","666666","qwertyuiop","123321","mustang","1234567890","michael","654321","pussy","superman","1qaz2wsx","7777777","fuckyou","121212","000000","qazwsx","123qwe","trustno1","jordan","jennifer","zxcvbnm","asdfgh","hunter","buster","soccer","harley","batman","andrew","sunshine","iloveyou","fuckme","2000","robert","thomas","hockey","starwars","112233","george","computer","michelle","jessica","1111","zxcvbn","555555","11111111","131313","freedom","777777","pass","fuck","maggie","159753","aaaaaa","princess","cheese","summer","love","6969","chelsea","access","yankees","987654321","matrix", "!@#", "#@!", "!@#$", "$#@!", "!!!"]
name = input("Name: ")
lastname = input("Last name: ")
years = input("Years of Birds: ")
month = input("Month of birth: ")
day = input("Day of birth: ")
top100_support = input("Add support top100 in passwd? ")

# translite method. return text
def translit(name):
    eng = ["q", 'w', "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c",
           "v", "b", "n", "m", ]
    rus = ["ю", "в", 'е', "р", "т", "й", "у", "и", "о", "п", "а", "с", "д", "ф", "г", "х", "ж", "к", "л", "з", "ъ", "ц",
           "в", "б", "н", "м", ]
    for i in name:
        for j in eng:
            if (i == j):
                name = name.replace(name[name.find(i)], rus[eng.index(j)])
            if (i == j.upper()):
                name = name.replace(name[name.find(i)], rus[eng.index(j)].upper())

    return name
# probros method. return text
def mapping(name, lang):
    eng = ["q", 'w', "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "<", ">"]
    rus = ["й","ц", 'у', "к", "е", "н", "г", "ш", "щ", "з", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю"]
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

def mirroring(name):
    text=""
    for i in name:
        text+=name[len(name)-int(name.find(i))-1]
    return text

def dispersion(name):
    name = str(name)
    allname = [name.lower(), name.upper(), name.capitalize(), name.swapcase(), translit(name), mapping(name, "rus"), mapping(translit(name), "eng"), mapping(translit(name.lower()), "eng"), mirroring(name)]
    return allname

def withtop100(name):
    for i in top100:
        print(str(name) + str(i))
        print(str(i) + str(name))

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
            str(name)+str(day)+str(year),
            str(name)+str(day)+str(int(year)%100)]

def attac_by_alldate(name):
    for year in range(1920, 2018):

        fyear(name,year)

        for month in range(1,13):
            for day in range(1,32):
                print(str(name)+str(day)+str(month)+str(year))

def attac_by_year(name, year):
    fyear(name,year)

if (top100_support=="1"):
    for i in top100:
        print(i)

for names in dispersion(name):
    print(names * 3)
    print(names * 2)
    if (top100_support == "1"):
        withtop100(names)
    for i in yearsvar(names,lastname,years):
        print(i)
        if (top100_support=="1"):
            withtop100(i)