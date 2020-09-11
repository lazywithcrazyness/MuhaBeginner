name = "who is Muhammad?"
print(name) 

name = "last prophet sent to humanity"
print(name)

age = "what was his age at time of death", 61 * 1
print(age)

born = "where was he born?", "Makkah"
print(born)

migrate = "where did he migrate to?", "Madinah"
print(migrate)

mother = "who was his mother?", "Yaye Ameenah"
print(mother)

father = "who was his father?", "Abdoullah"
print(father) 

value = 25 ** 5
print(value)

value = 25 // 5
print(value)

percent = 80 % 10 
print(percent)

value = ((50 / 4) + 1)
print(value) 

question = "how many python programmers you know"
print(question)

answer = "none"
print(answer)

#escape characters 
msg = "Hello\nHey" #if you want results to be in separate lines
print(msg)

msg = "hello    hey" #if you want hello and hey spaced out click tab key
print(msg)

#double quotes and single quotes work the same 
question = "what inspired you to learn python"
print(question)

answer = 'to understand code injection'
print(answer)

msg = 'she said "eww" '
print(msg)

msg = 'she said "eww" ' 
print(msg)

#Concatenation
msg = "you're a fast learner"
msg1 = "you would excel in this class sike" 
print(msg + "..." + msg1) 

msg = "what is steganography?"
msg2 = "the process of hiding text into pictures or other files fo it may not be retrieved by unauthorized actors"
full_message = msg + "..." + msg2
print(full_message) 

#Concatenation with literals
msg = ("Have you guys finish todays assignment..." "yes we did")  
print(msg)  

msg = "Hello"
print(msg + " there")

#Multi strings 
#with all lines combined
silentwars = ("You are stronger than you think "
"you wake up everyday fighting wars in you head..."
"wars you barely talk about"
" what are these silent wars they ask? "
" They would better stay silent in my head."
" For i would rather they fight in my head, than fight the world"
"these silent wars can make you feel like a deamon")
print(silentwars)

#multiples strings with each line printed separate
#To combine any two lines add a backslash at the end \ 
silentwars = """You are stronger than you think 
you wake up everyday fighting wars in you head...
wars you barely talk about
what are these silent wars they ask? 
They would better stay silent in my head.
For i would rather they fight in my head, than fight the world
these silent wars can make you feel like a deamon"""
print(silentwars)

#Indexes
#To grab a particular location of a character use indexes
#If you write an index that goes beyond the number of characters you'd get a syntax error
location = "Show me the location of a character in this statement"
print(location[22])

#String slicing
#Allows you to slice a part of a string so when you print it removes a part of the string
#Whatever side you put the colon is where it will print
order = "Let me get a beefy crunch taco"
print(order[9]) 

order = "Let me get a beefy crunch taco"
print(order[11:]) 

order = "Let me get a beefy crunch taco"
print(order[:11]) 

#Negative indexes 
#Negatives with string slicing 
goal = "Who scored the goal of the season?"
print(goal[-1])

goal = "Who scored the goal of the season?"
print(goal[-9:])

goal = "Who scored the goal of the season?"
print(goal[:-9])

#Slicing with two numbers
goal = "Who scored the goal of the season?"
print(goal[11: -20:])

goal = "Who scored the goal of the season?"
print(goal[11:14])

#Strings are immutable
#Once you create a string you cannot change that string
drive = "CX9"
print(id(drive))

drive = "Mazda"
print(id(drive))

#Len() function
ihome = "How much does your mouse cost"
len(ihome)
print(ihome)

