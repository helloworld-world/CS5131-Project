import os

from Problem import Problem

PROBLEM_DIR = 'problems/'

tag_count = {}

for dir_name in os.listdir(PROBLEM_DIR):
    try:
        problem = Problem(PROBLEM_DIR + dir_name)
    except:
        # Some problems are in russian or has pdf statement, so we will delete those
        print(dir_name)
        os.remove(PROBLEM_DIR + dir_name)
        continue
    at_least = False
    for i in range(len(problem.has_tags)):
        if problem.has_tags[i]:
            at_least = True
            if problem.TAGS[i] in tag_count:
                tag_count[problem.TAGS[i]] += 1
            else:
                tag_count[problem.TAGS[i]] = 1
    # remove problems without any relevant tags / rating
    if not at_least or problem.rating == 0:
        print(dir_name)
        os.remove(PROBLEM_DIR + dir_name)

sorted_tags = []

for tag, count in tag_count.items():
    sorted_tags.append((count, tag))

sorted_tags.sort(reverse=True)

for count, tag in sorted_tags:
    print(tag, count)
