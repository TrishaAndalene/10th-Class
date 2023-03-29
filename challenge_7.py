#import resource
from os import system

#checking answer
def check_questions(row):
	q = row[0]
	a = row[1]

	user_ans = input(f"{q}, answer : ")
	if user_ans == a:
		print("Correcto !")
		return True

	else:
		print("Try again later")
		return False

# Second step
def run_test(questions):
	if len(questions) == 0:
		print("No question were available")
	else:
		index = 0
		right = 0

		while index < len(questions):
			#print(questions[index])

			if check_questions(questions[index]):
				right += 1
				
			input("Press [ENTER] to continue to the next question")
			system('cls')
			index += 1
		print(f"So the result are {right} / {len(questions)} or {right/len(questions)*100:.1f} %")

#Storage
def get_question():

	return [
		["What color is the daytime sky on a clear day?", "blue"], #1
		["What is the answer to life, the universe and everything?", "42"], #2
		["What is a three letter word for mouse trap?", "cat"], #3
		["What's probably the color of a philosopher stone?", "red"], #4
		["I’m tall when I’m young, and I’m short when I’m old. What am I?", "a candle"], #5
		["You walk into a room that contains a match, a kerosene lamp, a candle and a fireplace. What would you light first?", "the match"], #6
		["People make me, save me, change me, raise me. What am I?", "money"], #7
		[" A man looks at a painting in a museum and says, “Brothers and sisters I have none, but that man’s father is my father’s son.” Who is in the painting?", "the man's son"], # 8
		["I have lakes with no water, mountains with no stone and cities with no buildings. What am I?", "a map"], # 9
		["If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I?", "a secret"] #10
	]

#First Step
run_test(get_question())