import os

from Problem import Problem

PROBLEM_DIR = 'problems/'

tag_count = {}

for dir in os.listdir(PROBLEM_DIR):
    problem = Problem(PROBLEM_DIR + dir)
    for tag in problem.tags:
        if tag in tag_count:
            tag_count[tag] += 1
        else:
            tag_count[tag] = 1

sorted_tags = []

for tag, count in tag_count.items():
    sorted_tags.append((count, tag))

sorted_tags.sort(reverse=True)

for count, tag in sorted_tags:
    print(tag, count)
