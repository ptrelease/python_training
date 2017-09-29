from random import randint



input = raw_input()
print(input)


list = [1,2,3,4,5]

print(list)

print(max(list))
print(min(list))

sum = 0
for num in list:
    sum += num
print(sum)

mean = 0
count = 0
for num in list:
    sum += num
    count += 1


print(sum/count)


results = {}
print('national lottery')
for x in range(1,6):
    results[x] = randint(1,99)
print(results)
