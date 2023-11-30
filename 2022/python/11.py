from sys import stdin

MOD = 2*3*5*7*11*13*17*19*23
    
def make_monkey_functions(op, div, true_dst, false_dst):
    if op[-2] == '*': 
        if op[-1] == 'old':
            change = lambda n: n * n
        else:
            change = lambda n, x=int(op[-1]): n * x
    else:
        change = lambda n, x=int(op[-1]): n + x
    
    def fn_part1(val):
        new = change(val) // 3
        return new, (true_dst if new % div == 0 else false_dst)
        
    def fn_part2(val):
        new = change(val) % MOD
        return new, (true_dst if new % div == 0 else false_dst)

    return fn_part1, fn_part2


def parse_monkeys():
    items, fns1, fns2 = [], [], []
    for i, group in enumerate(stdin.read().split('\n\n')):
        lines = group.splitlines()
        for item in lines[1].split(': ')[1].split(','):
            items.append((int(item), i))
        
        op = lines[2].split(': ')[1].split()        
        div, true_dst, false_dst = [int(lines[i].split()[-1]) for i in (3, 4, 5)]
        assert MOD % div == 0
        
        fn1, fn2 = make_monkey_functions(op, div, true_dst, false_dst)
        fns1.append(fn1)
        fns2.append(fn2)
        
    return items, fns1, fns2


def count_item_handled(value, src, monkey_fns, num_rounds):
    counts = [0] * len(monkey_fns)
    rounds_moved = 0
    while rounds_moved < num_rounds:
        value, dst = monkey_fns[src](value)
        rounds_moved += dst < src 
        counts[src] += 1           
        src = dst
            
    return counts


def monkey_business_score(items, monkey_fns, num_rounds):
    counts_by_item = []
    for item in items:
        counts_by_item.append(count_item_handled(*item, monkey_fns, num_rounds))
    
    counts_by_monkey = [0] * len(monkey_fns)
    for i in range(len(counts_by_monkey)):
        counts_by_monkey[i] = sum(c[i] for c in counts_by_item)    
    
    a, b = sorted(counts_by_monkey)[-2:]
    return a * b


items, fns1, fns2 = parse_monkeys()
print(monkey_business_score(items, fns1, 20))
print(monkey_business_score(items, fns2, 10000))
