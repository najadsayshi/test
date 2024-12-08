#program for two sum

nums=[2,7,11,15]
target=9

prevEle={}
for index,value in enumerate(nums):
    diff=target-value
    if diff in prevEle:
        print([index,prevEle[diff]])
    prevEle[value]=index
