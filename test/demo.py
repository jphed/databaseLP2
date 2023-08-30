filetext = open("names.txt", "r")
new_filetext = open("names2.txt", "a")
txtlist = []

for row in filetext:
    split = row.split()
    txtlist.append(split)




