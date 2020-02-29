import sys

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

grammar_file = sys.argv[1]
max_tree_level = int(sys.argv[2])

with open(grammar_file, 'r') as f:
    non_terminals = f.readline().strip().split(' ')
    terminals = f.readline().strip().split(' ')
    starting_point = f.readline()
    
    # read the production rules into a list and then make a dict from it
    temp = f.readline().strip().split(',')
    for rule in temp:
        # if the rule is an empty strin, skip it
        if rule == '':
            continue

        p = rule.split(' ')
        production_rules[p[0]] = []
        for d in p[1:]:
            if d == '':
                continue
            production_rules[p[0]].append(d)

def generate_words(ex, level):
    found_non_terminal = False
    for non_term in non_terminals:
        if non_term in ex:
            found_non_terminal = True
            break

    if (level >= max_tree_level):
        if found_non_terminal:
            return None
        return ex

    if found_non_terminal:
        for i in range(0, len(ex)):
            if ex[i] in non_terminals:
                for rule in production_rules[ex[i]]:
                    # if len(rule) % 2 == 0:
                    #     new_expression = ex[:i] + rule + ex[i+1:]
                    # else:
                    #     new_expression = ex[:i] + rule + ex[i+1:]
                    #     print(new_expression,  len(new_expression), len(ex))
                    new_expression = ex[:i] + rule + ex[i+1:]
                    res = generate_words(new_expression, level+1)
                    if res != None:
                        language_tree.append(res.strip())
    else:  
        return ex

# Generate the words
generate_words(starting_point, 0)
 
print(language_tree)
