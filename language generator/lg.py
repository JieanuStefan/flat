# $ = empty word
# In the file the 'variables' are in the folloing order
# Non-terminals
# Terminals
# Starting point
# Production rules

non_terminals = []
terminals = []
starting_point = []
production_rules = {}

language_tree = []

with open('grammar2.txt', 'r') as f:
    non_terminals = f.readline().strip().split(' ')
    terminals = f.readline().strip().split(' ')
    starting_point = f.readline()
    # read the production rules into a list and then make a dict from it
    temp = f.readline().split(',')
    for rule in temp:
        # if the rule is an empty strin, skip it
        if len(rule) == 0:
            continue

        p = rule.split(' ')
        production_rules[p[0]] = []
        for d in p[1:]:
            production_rules[p[0]].append(d)

def generate_tree(ex, tree):
    found_non_terminal = False
    for non_term in non_terminals:
        if non_term in ex:
            found_non_terminal = True
            break

    if found_non_terminal:
        tree = []
        for i in range(0, len(ex)):
            if ex[i] in non_terminals:
                for rule in production_rules[ex[i]]:
                    if len(rule) % 2 == 0:
                        print(ex[:i] + rule + ex[(i-1+len(rule)):])
                    else:
                        print(ex[:i] + rule + ex[(i+len(rule)):])
    else:
        return ex

print(generate_tree(starting_point, []))
