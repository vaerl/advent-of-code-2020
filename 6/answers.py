from collections import Counter

with open("6/answers.txt") as f:
    answers = f.readlines()
# 1
sum = 0
given_answers = []

for answer in answers:
    if answer == '\n':
        unique_answers = set(given_answers)
        num = len(unique_answers)
        sum += num
        given_answers = []
    else:
        answer = answer.strip()
        for char in answer:
            given_answers.append(char)

print("Result: ", sum)

# this works - for some reason, the last entry was not being counted!

# 2
sum = 0
given_answers = []
lines = 0

for answer in answers:
    if answer == '\n':
        num_answer = Counter(given_answers)
        num_answer = [x for x, count in num_answer.items() if count >=
                      lines]

        num = len(num_answer)
        print("num of answers: ", num)
        print("Set: ", num_answer)
        sum += num
        given_answers = []
        lines = 0
    else:
        lines += 1
        answer = answer.strip()
        previous_line = answer
        for char in answer:
            given_answers.append(char)

print("Result: ", sum)
