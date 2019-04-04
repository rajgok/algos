class solution(object):
    def twoSum(self, nums, target):
        sz = len(nums)
        if sz > 1:
            i = 0
            while i < sz-1:
                j = i + 1
                while j < sz:
                    if i!=j and nums[i] + nums[j] == target:
                        return (i, j)                    
                    j +=1
                i += 1
        return (-1, -1)

    def twoSum1(self, nums, target):
        # array to dictionary
        lookup = dict((v,i) for i, v in enumerate(nums))
        print(lookup)
        sz = len(nums)
        if sz > 1:
            i = 0 
            while i< sz :
                other = target - nums[i]
                if other  in lookup and lookup[other] !=i:
                    return (i, lookup[other])
                i+=1                
        return (-1,-1)

    def twoSum2(self, nums, target):
        lookup = list(nums)
        print(lookup)
        i=0
        for k in lookup:
            print(k)
            other = target - k            
            print(other, i)
            if other in lookup:
                t=lookup.index(other)
                if t != i:
                    return (t, i)
            i+=1
        return (-1,-1)

    def twoSum3(self, nums, target):
        lookup = dict()        
        i = 0
        for x in nums:
            print(lookup)
            diff = target - x            
            if diff in lookup: 
                if i != lookup[diff]:
                    return (i, lookup[diff])
            else:
                lookup[x] = nums.index(x)
            i+=1
        return(-1,-1)

s = solution()
ns = [3,4,5,3]
target=8
res =s.twoSum3(ns, target)
# res =s.twoSum2(ns, target)
# res=s.twoSum1(ns,target)
#res = s.twoSum(ns,8)
print('Result target ' + str(target) + ' based : %s' % (res,))