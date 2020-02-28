# $ = empty word

non_terminals = []
terminals = []
starting_point = []
production_rules = []


with open('grammar.txt', 'r') as f:
    non_terminals = f.readline()
    terminals = f.readline()
    starting_point = f.readline()
    # read the production rules into a list and then make a dict from it
    production_rules = f.readline()

