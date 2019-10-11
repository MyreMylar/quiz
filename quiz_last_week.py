# this is one possible version of the code we worked on last week

score = 0

# Question 1
print("What is the capital city of France?")
print("A: Paris")
print("B: London")
print("C: Berlin")

answer = input()
answer = answer.lower()

if answer == 'a':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("Who is the prime minister of the UK?")
print("A: Donald Trump")
print("B: David Cameron")
print("C: Teresa May")

answer = input()
answer = answer.lower()

if answer == 'c':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
print("When was the battle of Hastings fought?")
print("A: 1066")
print("B: 1776")
print("C: 1966")

answer = input()
answer = answer.lower()

if answer == 'a':
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Final Score: " + str(score) + "/3")
