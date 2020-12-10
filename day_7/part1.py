from collections import deque
with open('input.txt') as f:
    content = f.readlines()

bag_out = set()
traverse_q = deque()
dag_bag = {'root':['shiny gold']}
for line in content:
    mbag = " ".join(line.split(" ")[:2])
    contains = line[line.index("contain ")+8:-1]
    each_contain = contains.split(",")
    each_contain = [cnt.lstrip() for cnt in each_contain]
    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    each_contain = [" ".join(cont.split(" ")[1:]) for cont in each_contain]

    for bag in each_contain:
        if bag not in dag_bag:
            dag_bag[bag] = [mbag]
        else:
            dag_bag[bag].append(mbag)
traverse_q.append('shiny gold')
count = 0
while traverse_q:
    cur = traverse_q.popleft()
    if dag_bag.get(cur):
        for v in dag_bag[cur]:
            if v not in bag_out:
                traverse_q.append(v)
                bag_out.add(v)
                count+=1

print(count)