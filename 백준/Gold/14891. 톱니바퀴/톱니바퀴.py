
from collections import deque
gear = [deque(list(map(int, input()))) for _ in range(4)]

K = int(input())
turns = []
for _ in range(K):
    turns.append(list(map(int, input().split())))

def turngear(n, dir):
    if dir == 1: #clockwise
        gear[n] = [gear[n][-1]]+gear[n][:-1]
    else:
        gear[n] = gear[n][1:]+[gear[n][0]]
    return

def gearright(n,dir):
    #print("gearright: ", n, dir)
    if n>3:
        return
    if gear[n-1][2] != gear[n][6]:
        gearright(n+1,(-1)*dir)
        gear[n].rotate(dir)

def gearleft(n,dir):
    if n<0:
        return
    if gear[n][2] != gear[n+1][6]:
        gearleft(n-1,(-1)*dir)
        gear[n].rotate(dir)

for turn in turns:
    number = turn[0]-1
    direction = turn[1] #1 clockwise, -1 anticlockwise
    
    gearleft(number-1, (-1)*direction)
    gearright(number+1, (-1)*direction)
    
    gear[number].rotate(direction)
    
result = 0
if gear[0][0] == 1:
    result += 1
if gear[1][0] == 1:
    result += 2
if gear[2][0] == 1:
    result += 4
if gear[3][0] == 1:
    result += 8

print(result)
#print(gear)