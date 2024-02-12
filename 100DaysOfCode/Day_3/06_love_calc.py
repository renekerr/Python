print('The Love Calculator is calculating your score...')
name1 = input('What is her name? ')
name2 = input('What is his name? ')

two_names = name1.lower() + ' ' + name2.lower()

#TRUE count
t = two_names.count('t')
r = two_names.count('r')
u = two_names.count('u')
e = two_names.count('e')
true_total = t + r + u + e

#LOVE count
l = two_names.count('l')
o = two_names.count('o')
v = two_names.count('v')
x = two_names.count('e')
love_total = l + o + v + x

love_score = int(str(true_total) + str(love_total))


if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif (love_score > 40) and (love_score < 50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')












