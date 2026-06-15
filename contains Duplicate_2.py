nums =[1,2,3,1]
k=3
def removeDuplicates(nums,k):
    hashmap={}
    for i,num in enumerate(nums):
        if num in hashmap:
            if i-hashmap[num]<=k:
                return True
            hashmap[num]=i
    return False
print(removeDuplicates(nums,k))                 
