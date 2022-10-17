from random import choice, shuffle, randint
from time import time


def generate_simple_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(randint(1, code_max))
        rule = {
            'if': {
                log_oper: items
            },
            'then': code_max + j
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_stairway_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(i + j)
        rule = {
            'if': {
                log_oper: items
            },
            'then': i + j + 1
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_ring_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = generate_stairway_rules(code_max, n_max, n_generate - 1, log_oper_choice)
    log_oper = choice(log_oper_choice)  # not means and-not (neither)
    if n_max < 2:
        n_max = 2
    n_items = randint(2, n_max)
    items = []
    for i in range(0, n_items):
        items.append(code_max - i)
    rule = {
        'if': {
            log_oper: items
        },
        'then': 0
    }
    rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_random_rules(code_max, n_max, n_generate, log_oper_choice=["and", "or", "not"]):
    rules = []
    for j in range(0, n_generate):

        log_oper = choice(log_oper_choice)  # not means and-not (neither)
        if n_max < 2:
            n_max = 2
        n_items = randint(2, n_max)
        items = []
        for i in range(0, n_items):
            items.append(randint(1, code_max))
        rule = {
            'if': {
                log_oper: items
            },
            'then': randint(1, code_max)
        }
        rules.append(rule)
    shuffle(rules)
    return (rules)


def generate_seq_facts(M):
    facts = list(range(0, M))
    shuffle(facts)
    return facts


def generate_rand_facts(code_max, M):
    facts = []
    for i in range(0, M):
        facts.append(randint(0, code_max))
    return facts


# samples:
print(generate_simple_rules(100, 4, 10))
print(generate_random_rules(100, 4, 10))
print(generate_stairway_rules(100, 4, 10, ["or"]))
print(generate_ring_rules(100, 4, 10, ["or"]))

# generate rules and facts and check time
time_start = time()
N = 100000
M = 1000
rules = generate_simple_rules(100, 4, N)
facts = generate_rand_facts(100, M)
print("%d rules generated in %f seconds" % (N, time() - time_start))


# load and validate rules
# YOUR CODE HERE


def rule_is_valid(rule,facts):
    new_rule = [rule[0]]
    flag = True
    for i in rule:
        flag = True
        for j in new_rule:
            if j['if'] == i['if']:
                flag = False
                break
            if 'not' in i['if'] and 'or' in j['if']:
                if i['if']['not'] == j['if']['or']:
                    flag = False
                    break
            if 'not' in i['if'] and 'and' in j['if']:
                if i['if']['not'] == j['if']['and']:
                    flag = False
                    break
            if 'not' in j['if'] and 'or' in i['if']:
                if j['if']['not'] == i['if']['or']:
                    flag = False
                    break
            if 'not' in j['if'] and 'and' in i['if']:
                if j['if']['not'] == i['if']['and']:
                    flag = False
                    break
        if i['then'] in facts:
            flag=False
        if flag:
            new_rule.append(i)
            
    print(f'rules before {len(rule)}')
    print(f'rules after {len(new_rule)}')
    return new_rule


#rule=rule_is_valid(rules, facts)

# check facts vs rules

time_start = time()
#print(facts)
# YOUR CODE HERE
facts = list(set(facts))
#print(facts)


def rule_check(rule, fact):
    ans = []
    for i in rule:
        if 'not' in i['if']:
            if (set(i['if']['not']) & set(fact)) is None:
                ans.append(i['then'])
        elif 'or' in i['if']:
            if (set(i['if']['or']) & set(fact)) is not None:
                ans.append(i['then'])
        elif 'and' in i['if']:
            if (set(i['if']['and']) & set(fact)) == set(i['if']['and']):
                ans.append(i['then'])
    return ans


print((rule_check(rules, facts)))

print("%d facts validated vs %d rules in %f seconds" % (M, N, time() - time_start))
