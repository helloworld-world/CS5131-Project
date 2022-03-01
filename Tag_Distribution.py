import json

data = json.load(open("problemset.problems.json"))
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

for count, tag in sorted_tags:
    print(tag, count)