#!/usr/bin/python
def total_value(items, max_weight):
    return sum([x[2]
                for x in items]) if sum([x[1]
                                         for x in items]) < max_weight else 0



cache = {}


def solve(items, max_weight):
    if not items:
        return ()
    if (items, max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head, ) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        
        if total_value(include, max_weight) > total_value(
                dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items, max_weight)] = answer
    return cache[(items, max_weight)]


items = (
    ("block 1", 2000, 13000),
    ("block 2", 6000, 9000),
    ("block 3", 800, 2000),
    ("block 4", 700, 1500),
    ("block 5", 1200, 3500),
    ("block 6", 1000, 2800),
    ("block 7", 1300, 5000),
    ("block 8", 600, 1500),
)
max_weight = 6000

solution = solve(items, max_weight)
print("Liste :")
for x in solution:
    print(x[0], "\nTaille : ", x[1], "octets et son pourboire : ", x[2],
          " en satoshis")

print("Pourboire Total :", total_value(solution, max_weight))
print("Taille en satoshis :", sum([x[1] for x in solution]))