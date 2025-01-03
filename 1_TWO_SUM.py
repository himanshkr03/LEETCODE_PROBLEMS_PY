num= [2,7,11,15]
target=9
def twoSumArray(num,target):
    target_val={}

    for i,num in enumerate(num):
        if target-num in target_val:
            return [target_val[target-num],i]
        target_val[num]=i
    return []
print(twoSumArray(num,target))