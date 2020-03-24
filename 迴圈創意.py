# 聖誕樹
height = 5
stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
print((' ' * height) + '|')

#%%
# turtle
import turtle
c = turtle.Turtle()
c.circle(100)
c.left(10)
c.circle(100)

for i in range(36):
    c.circle(100)
    c.left(10)
    i += 1
    
#%%
import turtle
c = turtle.Turtle()
i = 0
while i < 36:
    i += 1
    if i% 2 == 0:
        c.circle(100)
    c.left(10)
