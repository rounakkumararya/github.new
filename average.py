total = 0
count = 0
while True:
    inp = input('enter a no.:')
    if inp == 'done':
        break
    value = float(inp)
    total = total+value
    count = count+1
average = total/count
print('average:', average)
