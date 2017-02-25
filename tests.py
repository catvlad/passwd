def mirroring(name):
    text=""
    for i in name:
        text+=name[len(name)-int(name.find(i))-1]
    return text

print(mirroring("Lena"))
