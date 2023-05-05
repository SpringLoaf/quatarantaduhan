import csv
import random
game_q = {}
answer_key_1 = ""
answer_key_2 = ""
answer_key_3 = ""


with open('questions.csv') as csvfile:
	questions = csv.reader(csvfile, delimiter=',')
	compiled = {}
	for row in questions:
		compiled.update({row[0]: {row[1]: True, row[2]: False, row[3]: False, row[4]: False}})
	keys = list(compiled.keys())
	random.shuffle(keys)
	for x in range(3):
		answers = {}
		ans_keys = list(compiled[keys[x]].keys())
		random.shuffle(ans_keys)
		for y in ans_keys:
			answers[y] = compiled[keys[x]][y]
		game_q[keys[x]] = answers
	for ans in range(0, 3):
		print(ans)
		for c, d in enumerate(game_q[list(game_q.keys())[ans]].values()):
			print(c, d)
			if d == True:
				if ans == 0:
					if c == 0:
						answer_key_1 = 'a'
					elif c == 1:
						answer_key_1 = 'b'
					elif c == 2:
						answer_key_1 = 'c'
					elif c == 3:
						answer_key_1 = 'd'
				elif ans == 1:
					if c == 0:
						answer_key_2 = 'a'
					elif c == 1:
						answer_key_2 = 'b'
					elif c == 2:
						answer_key_2 = 'c'
					elif c == 3:
						answer_key_2 = 'd'
				elif ans == 2:
					if c == 0:
						answer_key_3 = 'a'
					elif c == 1:
						answer_key_3 = 'b'
					elif c == 2:
						answer_key_3 = 'c'
					elif c == 3:
						answer_key_3 = 'd'
					



print(game_q)
print(list(game_q[list(game_q.keys())[0]].keys())[0])

print(answer_key_1)
print(answer_key_2)
print(answer_key_3)