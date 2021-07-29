# 🚨 Don't change the code below 👇
heights = input("Input a list of student heights ").split()
for n in range(0, len(heights)):
  heights[n] = int(heights[n])
# 🚨 Don't change the code above 👆
total = 0
elements = 0

for i in heights:
  elements += 1

for i in heights:
  total += i

print(round(total / elements))

#Write your code below this row 👇




