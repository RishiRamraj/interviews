'''
Problem:
For the numbers 1 to 100, print fizz if divisible by 3, bang if
divisible by 5.
'''

print(', '.join(('fizz bang' if ii % 15 == 0 else 'fizz' if ii % 3 == 0 else 'bang' if ii % 5 == 0 else str(ii) for ii in range(1, 101))))
