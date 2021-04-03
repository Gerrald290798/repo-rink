food = ['rice','beans']
food.append('brocoli')
food.extend(['bread','pizza'])
print(food[:2])
print(food[-1])
breakfast = "eggs,fruit,orang juice".split(',')
print(len(breakfast))
nums = [0]
while(True):
    cmd = input()
    if(cmd == 'stop'):
        break
    nums.append(float(cmd))
print(sum(nums)/len(nums),min(nums),max(nums))