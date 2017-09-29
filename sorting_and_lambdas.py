# functional programming

people = {"john": 10000, "cath": 10000, "paul":30000, "heather":40000, "matt":60000, "alex":60000, "phil":70000, "jamie":80000, "jacob":90000, "zoe":100000}

print('unsorted dict %s' % people)
print('********************************************')
print('print the dict in order of names')

key_list = []
for key in people:
    key_list.append(key)

key_list.sort()
for key in key_list:
    print("name %s wages %s" % (key, people[key]))


print('********************************************')

print('print the dict in order of salaries - my answer')

dict_with_salary_as_key = {}
for key in people:
    dict_with_salary_as_key[people[key]] = key

salary_list = []
for key in people:
    salary_list.append(people[key])

# sort salaries
sorted_salary_list = sorted(salary_list, cmp = lambda a,b: a-b)

for key in sorted_salary_list:
    print("wages %s name %s" % (key, dict_with_salary_as_key[key]))

# My answer above will NOT work if there are duplicate salary values.
# The book answer works directly on the dictionary like this:
print('Ordered by salary - book answer:')
names_list = people.keys() # so they are unsorted again
names_list.sort(cmp = lambda a,b: cmp(people[a], people[b]))
for name in names_list:
    print("%s earns %d" % (name,people[name]))
# So the above isn't sorting the dict, but because it sorts the names_list
# by salary, you can use the names list to refer to the orignal dict,
# not the salary dict as in my buggy solution.

# This is the code for sorting by salary, then name from the book.  The
# Or looks weird, but works from demonstrating this in the interpreter:
# >>> 1 or -1
# 1
# >>> 1 or 2
# 1
# >>> 0 or 1
# 1
# >>> -1 or 0
# -1
# >>> 0 or -1
# -1
# >>>
# So you can see that if the first value is anything other than 0, then the
# lazy evaluation pushing to evaluate the next thing - but only then!!

print('Ordered by salary then name:')
names_list = people.keys() # so they are unsorted again
# provide a custom 'cmp' function:
names_list.sort(cmp = \
                    lambda a,b: cmp(people[a],people[b]) or cmp(a,b))
# note could use cmp((salaries[a],a),(salaries[b],b))
# as cmp works on tuples
for name in names_list:
    print("%s earns %d" % (name, people[name]))

#Still loads of functional programming exercises to do.

print('done')