Gryffindor = int()
Ravenclaw = int()
Hufflepuff = int()
Slytherin = int()



# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

Q1 = int(input('Do you like Dawn or Dusk (1 = Dawn, 2 = Dsuk) = '))
if Q1 == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif Q1 == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print('Wrong input')

# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

Q2 = int(input('When im dead, i want people to remember me as (1=The good, 2=The greet, 3=The wise, 4=The bold) = '))
if Q2 == 1:
    Hufflepuff = Hufflepuff + 2
elif Q2 == 2:
    Slytherin = Slytherin + 2
elif Q2 == 3:
    Ravenclaw = Ravenclaw + 2
elif Q2 == 4:
    Gryffindor = Gryffindor + 2
else:
    print('Wrong input')

# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

Q3 = int(input('Which kind of instrument most pleases your ear (1=Violin, 2=Trumpet, 3=Piano, 4=Drum) = '))
if Q3 == 1:
    Slytherin = Slytherin + 4
elif Q3 == 2:
    Hufflepuff = Hufflepuff + 4
elif Q3 == 3:
    Ravenclaw = Ravenclaw + 4
elif Q3 == 4:
    Gryffindor = Gryffindor + 4
else:
    print('Wrong input')
 
print('Gryffindor = ', Gryffindor) 
print('Ravenclaw = ', Ravenclaw) 
print('Slytherin = ', Slytherin) 
print('Hufflepuff = ', Hufflepuff) 


max = max(Gryffindor, Ravenclaw, Slytherin, Hufflepuff)
if max == Gryffindor:
    print(max,'Gryffindor')
elif max == Ravenclaw:
    print(max,'Ravenclaw')
elif max == Slytherin:
    print(max,'Slytherin')
else:
    print(max,'Hufflepuff')


          