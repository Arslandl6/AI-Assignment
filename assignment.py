# 1. FizzBuzz
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 2. Leap Year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Leap Year 2024:", is_leap(2024))

# 3. Identity vs Equality
L1 = [1,2,3]
L2 = [1,2,3]
print("L1 == L2:", L1 == L2)   # True (values same)
print("L1 is L2:", L1 is L2)   # False (different memory)

# 4. Bitwise Swap
a = 5
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap:", a, b)

# 5. First 10 Prime Numbers
count = 0
num = 2
while count < 10:
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

# 6. Loop Breaker
for i in range(1, 21):
    if i % 4 == 0:
        pass
    if i == 13:
        continue
    if i == 18:
        break
    print(i)

# 7. Grade System
marks = 85
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("Fail")

# 8. Reverse Integer
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed:", rev)

# 9. Runner-Up Score
scores = [2, 3, 6, 6, 5]
max_score = max(scores)
runner_up = max([x for x in scores if x != max_score])
print("Runner-up:", runner_up)

# 10. Remove Duplicates
lst = [1,2,2,3,4,4]
unique = list(set(lst))
print("Unique:", unique)

# 11. List Intersection
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common = [x for x in list1 if x in list2]
print("Common:", common)

# 12. Tuple Immutability
t = (1,2,3)
try:
    t[1] = 10
except TypeError as e:
    print("Error:", e)

# 13. Character Frequency
text = "hello"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# 14. Squares of Even Numbers
squares = [x*x for x in range(1,21) if x % 2 == 0]
print(squares)

# 15. Dictionary Comprehension
d = {'a':1, 'b':2, 'c':3, 'd':4}
new_d = {k:v for k,v in d.items() if v > 2}
print(new_d)