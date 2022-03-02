import json

data = json.load(open('problemset.problems.json', encoding='utf-8', errors='ignore'))
tag_count = {}
problems = data["result"]["problems"]
for problem in problems:
    if "tags" in problem:
        for tag in problem["tags"]:
            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1


sorted_tags = []

for tag, count in tag_count.items():
    sorted_tags.append((count, tag))

sorted_tags.sort(reverse=True)

'''

math 2000
greedy 1928
dp 1566
data structures 1248
brute force 1170
constructive algorithms 1160
graphs 828

'''

for count, tag in sorted_tags:
    print(tag, count)