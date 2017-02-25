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

translit("Vlad")