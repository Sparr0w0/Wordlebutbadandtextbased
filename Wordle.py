import random

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

wordstxt = open(".\words.txt", "r")


words = []

for line in wordstxt:

  stripped_line = line.strip()

  line_list = stripped_line.split()

  words.append(line_list)

answerstxt = open(".\answers.txt", "r")


answers = []

for line in answerstxt:

  stripped_line = line.strip()

  line_list = stripped_line.split()

  answers.append(line_list)


answerstxt.close()

lettersleft = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",]
lettersleft2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
lettersleft3 = ["z", "x", "c", "v", "b", "n", "m"]
correctletters = []
rongplace = []
word = random.choice(answers)
word = str(word[0])
letters = list(word)
lettersgessed = []
lettersguessedright = ["?","?","?","?","?"]
x = 0

#print (word)
#print (letters)

print ("Welcome To Wordle!")
print ("------------------\n")

while x == 0:
    choice = input("Please Enter A Guess\n")
    choice = choice.lower()
    #print (choice)
    if any(choice in i for i in words):
        choiceletters = list(choice)

        if word == choice:
            print ("You Won")
            break

        if choiceletters[0] == letters[0]:
            print ("Letter 1 is correct")
            lettersguessedright[0] = letters[0]
            correctletters.append(letters[0])

        if choiceletters[1] == letters[1]:
            print ("Letter 2 is correct")
            lettersguessedright[1] = letters[1]
            correctletters.append(letters[1])

        if choiceletters[2] == letters[2]:
            print ("Letter 3 is correct")
            lettersguessedright[2] = letters[2]
            correctletters.append(letters[2])

        if choiceletters[3] == letters[3]:
            print ("Letter 4 is correct")
            lettersguessedright[3] = letters[3]
            correctletters.append(letters[3])

        if choiceletters[4] == letters[4]:
            print ("Letter 5 is correct")
            lettersguessedright[4] = letters[4]
            correctletters.append(letters[4])

        #print(correctletters)

        lettersguessedrightuser = lettersguessedright[0] + lettersguessedright[1] + lettersguessedright[2] + lettersguessedright[3] + lettersguessedright[4]

        if choiceletters[0] in letters and letters[0] != choiceletters[0] and choiceletters[0] not in correctletters:
            print(choiceletters[0], "is in the word but in the wrong place")
            correctletters.append(letters[0])

        if choiceletters[1] in letters and letters[1] != choiceletters[1] and choiceletters[1] not in correctletters:
            print(choiceletters[1], "is in the word but in the wrong place")
            correctletters.append(letters[0])

        if choiceletters[2] in letters and letters[2] != choiceletters[2] and choiceletters[2] not in correctletters:
            print(choiceletters[2], "is in the word but in the wrong place")
            correctletters.append(letters[0])

        if choiceletters[3] in letters and letters[3] != choiceletters[3] and choiceletters[3] not in correctletters:
            print(choiceletters[3], "is in the word but in the wrong place")
            correctletters.append(letters[0])

        if choiceletters[4] in letters and letters[4] != choiceletters[4] and choiceletters[4] not in correctletters:
            print(choiceletters[4], "is in the word but in the wrong place")
            correctletters.append(letters[0])

        print(lettersguessedrightuser)
        
        for i in range(len(lettersleft)):
            if lettersleft[i] == choiceletters[0] and lettersleft[i] not in word:
                lettersleft[i] = ' '
        for i in range(len(lettersleft)):
            if lettersleft[i] == choiceletters[1] and lettersleft[i] not in word:
                lettersleft[i] = ' '
        for i in range(len(lettersleft)):
            if lettersleft[i] == choiceletters[2] and lettersleft[i] not in word:
                lettersleft[i] = ' '
        for i in range(len(lettersleft)):
            if lettersleft[i] == choiceletters[3] and lettersleft[i] not in word:
                lettersleft[i] = ' '
        for i in range(len(lettersleft)):
            if lettersleft[i] == choiceletters[4] and lettersleft[i] not in word:
                lettersleft[i] = ' '
        for i in range(len(lettersleft2)):
            if lettersleft2[i] == choiceletters[0] and lettersleft2[i] not in word:
                lettersleft2[i] = ' '
        for i in range(len(lettersleft2)):
            if lettersleft2[i] == choiceletters[1] and lettersleft2[i] not in word:
                lettersleft2[i] = ' '
        for i in range(len(lettersleft2)):
            if lettersleft2[i] == choiceletters[2] and lettersleft2[i] not in word:
                lettersleft2[i] = ' '
        for i in range(len(lettersleft2)):
            if lettersleft2[i] == choiceletters[3] and lettersleft2[i] not in word:
                lettersleft2[i] = ' '
        for i in range(len(lettersleft2)):
            if lettersleft2[i] == choiceletters[4] and lettersleft2[i] not in word:
                lettersleft2[i] = ' '
        for i in range(len(lettersleft3)):
            if lettersleft3[i] == choiceletters[0] and lettersleft3[i] not in word:
                lettersleft3[i] = ' '
        for i in range(len(lettersleft3)):
            if lettersleft3[i] == choiceletters[1] and lettersleft3[i] not in word:
                lettersleft3[i] = ' '
        for i in range(len(lettersleft3)):
            if lettersleft3[i] == choiceletters[2] and lettersleft3[i] not in word:
                lettersleft3[i] = ' '
        for i in range(len(lettersleft3)):
            if lettersleft3[i] == choiceletters[3] and lettersleft3[i] not in word:
                lettersleft3[i] = ' '
        for i in range(len(lettersleft3)):
            if lettersleft3[i] == choiceletters[4] and lettersleft3[i] not in word:
                lettersleft3[i] = ' '

        print (lettersleft)
        print (lettersleft2)
        print (lettersleft3)
    else:
        continue
