# %%
import csv
guests = ['frank', 'rose', 'jack', 'lucy']
guests.append('faramarz')
print(guests[3])

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
guests.append('faramarz')
print(guests[4])

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
guests.append('faramarz')
print(guests[-1])

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
guests.append('faramarz')
print(guests[-2])

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
for guest in guests:
    print(guest)

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
for guest in guests:
    guests.append('eli')
    print(guest)

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
guests.append('eli')
for guest in guests:

    print(guest)

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
index = 0
while index < len(guests):
    print(guests[index])
    index += 1


# %%
guests = ['frank', 'rose', 'jack', 'lucy']
guests.remove('frank')
print(guests)

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
del guests[0]
print(guests)

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
print(guests.index('rose'))

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
for guest in range(len(guests)):
    print(guests[guest])

# %%
guests = ['frank', 'rose', 'jack', 'lucy']
guests.sort()
for guest in guests:
    print([guest])

# %%
guests = input(
    "Enter the name of everyone attending the party (separated by commas): ")
guest_list = guests.split(", ")
guest_list.sort()
print("The list of party guests in alphabetical order is:")
print(guest_list)


# %%
guest_list = ["serena", "frank", "coillns", "ali"]
guest_list.sort()
print(guest_list)


# %%
guest_list = []
while True:
    guests = input("Enter the name of the guests (or 'done' to exit): ")
    if guests == 'done':
        break
    guest_list.append(guests)
    guest_list.sort()
print(guest_list)

# %%
guest_list = []
while True:
    guests = input("Enter the name of the guests (or 'done' to exit): ")
    if guests == 'done':
        break
    guest_list.append(guests)

guest_list.sort()
print("The sorted list of guests is:")
print(guest_list)


# %%
guest_list = []
while True:
    guests = input("Enter the name of the guests (or 'done' to exit): ")
    if guests == 'done':
        break
    guest_list.append(guests)

# This line is moved after the break statement.
guest_list.sort()

print("The sorted list of guests is:")
print(guest_list)


# %%
fileName = 'myFile.txt'
WRITE = 'w'

file = open(fileName, mode=WRITE)

# %%
fileName = 'myFile.txt'
WRITE = 'w'

file = open(fileName, mode=WRITE)

# %%
fileName = 'myFile.txt'
APPEND = 'a'

file = open(fileName, mode=APPEND)

# %%
fileName = 'myFile.txt'
APPEND = 'a'

file = open(fileName, mode=APPEND)

# %%
fileName = 'myFile.txt'
accesMode = 'w'
myfile = open(fileName, accesMode)
myfile.write('how is ..\n')
myfile.write('what the ..')


# %%
fileName = 'myFile.txt'
accessMode = 'w'
myfile = open(fileName, accessMode)
myfile.write('how is ..\n')
myfile.write('what the ..')


# %%
fileName = 'myFile.txt'
accessMode = 'w'
myfile = open(fileName, accessMode)
myfile.write('how is ..\n')
myfile.write('what the ..')


# %%
fileName = 'myFile.txt'
accessMode = 'w'
myfile = open(fileName, accessMode)
myfile.write('how is ..dd\n')
myfile.write('what the ..sss')


# %%
fileName = 'myFile.txt'
accessMode = 'w'
myfile = open(fileName, accessMode)
myfile.write('how is ..\n')
myfile.write('what the ..')
myfile.close()

# %%
fileName = 'myFile.txt'
accessMode = 'w'
myfile = open(fileName, accessMode)
myfile.write('how is ..\n')
myfile.write('what the fffff')
myfile.close()

# %%
fileName = 'myFile.txt'
WRITE = 'w'
APPEND = 'a'
myfile = open(fileName, mode=WRITE)
myfile.write('fara, 32\n')
myfile.write('masy 31')
myfile.close()
print('file done')

# %%
fileName = 'myFile.csv'
WRITE = 'w'
APPEND = 'a'
myfile = open(fileName, mode=WRITE)
myfile.write('fara, 32\n')
myfile.write('masy 31')
myfile.close()
print('file done')

# %%
fileName = 'myFile.txt'
WRITE = 'w'
APPEND = 'a'
data = input('write what you like')

myfile = open(fileName, mode=WRITE)
myfile.write(data)
myfile.close()
print('file done')

# %%
fileName = 'test.txt'
accessMode = 'r'
myfile = open(fileName, accessMode)

# %%
fileName = 'test.txt'
accessMode = 'r'
test = open(fileName, accessMode)
print(test)

# %%
myText = open('test.txt', 'r')
allTxt = myText.read()
print(allTxt)

# %%
myText = open('test.txt', 'r')
onLineRead = myText.readline()
print(onLineRead)

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)

# %%

with open('myFile.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
        for cvsreaderLine in csvreader:
            print(cvsreaderLine)

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
        for cvsreaderLine in csvreader:
            print(cvsreaderLine)

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for i, row in enumerate(csvreader):
        print(row)
        if i > 0:  # skip the header row
            name = row[0]
            print(name)

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        for value in row:
            print(value + "\n")

# %%

with open('myFile.csv', newline='') as file:
    csvreader = csv.reader(file)
    for i, row in enumerate(csvreader):
        print('/ '.join(row))
        if i > 0:  # skip the header row
            name = row[0]
            print(name)
