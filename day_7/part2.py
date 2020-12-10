from collections import deque
with open('input.txt') as f:
    content = f.readlines()

weighted_dag_bag = dict()
traverse_q = deque()
for line in content:
    mbag = " ".join(line.split(" ")[:2])
    contains = line[line.index("contain ")+8:-1]
    each_contain = contains.split(",")
    each_contain = [cnt.lstrip() for cnt in each_contain]
    each_contain = [" ".join(cont.split(" ")[:-1]) for cont in each_contain]
    each_contain = {" ".join(cont.split(" ")[1:]):cont.split(" ")[0] for cont in each_contain}
    
    for bag, count in each_contain.items():
        try:
            if not weighted_dag_bag.get(mbag):
                weighted_dag_bag[mbag] = {bag:int(count)}
            else:
                weighted_dag_bag[mbag][bag] = int(count)
        except:
            pass

traverse_q.append('shiny gold')
count = 0
while traverse_q:
    cur = traverse_q.popleft()
    if weighted_dag_bag.get(cur):
        for k, v in weighted_dag_bag[cur].items():
            if isinstance(v, int):
                for i in range(1,v+1):
                    count+=1
                    traverse_q.append(k)

print(count)