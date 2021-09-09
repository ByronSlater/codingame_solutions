import sys
import math

w, h, t1, t2, t3 = [int(i) for i in input().split()]

class Asteroid:
    def __init__(self, c, t1=None, x1=None, y1=None, t2=None, x2=None, y2=None):
        self.c = c
        self.t1 = t1
        self.x1 = x1
        self.y1 = y1
        self.t2 = t2
        self.x2 = x2
        self.y2 = y2
    
    def get_x(self, t):
        return ((self.x2 - self.x1)/(self.t2 - self.t1)) * (t - self.t1)


    def get_y(self, t):
        return ((self.y2 - self.y1)/(self.t2 - self.t1)) * (t - self.t1)


    def __str__(self): 
        return self.c


    def __repr__(self): 
        return self.c



map_1 = []
map_2 = []

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    map_1.append(first_picture_row)
    map_2.append(second_picture_row)

print('\n'.join(map_1), file=sys.stderr)
print('-' * w, file=sys.stderr)
print('\n'.join(map_2), file=sys.stderr)

asteroids = {}

for x in range(w):
    for y in range(h):
        c = map_1[y][x]

        if c != '.':
            a = asteroids.get(c, Asteroid(c))
            a.t1 = t1
            a.x1 = x
            a.y1 = y
            asteroids[c] = a

        c = map_2[y][x]

        if c != '.':
            a = asteroids.get(c, Asteroid(c))
            a.t2 = t2
            a.x2 = x
            a.y2 = y
            asteroids[c] = a

end_grid = [['.' for x in range(w)] for y in range(h)]


for k, v in sorted(asteroids.items()):
    x3 = math.floor(v.get_x(t3))
    y3 = math.floor(v.get_x(y3))

    if end_grid[y3][x3] == '.':
        end_grid[y3][x3] = k


print('\n'.join(''.join(line) for line in end_grid))
