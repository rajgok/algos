class solution(object):
    def lengthOfLongestSubstring(self, s):
        sz = len(s)
        if sz <= 1:
            return sz
        ml = 0
        mml = ml
        reg = dict()        
        for c in s:
            if c in reg:                
                ml = 1
                print ('-' + str(ml))
            else:                
                ml +=1
                print ('*' + str(ml))
                reg[c] = 1
                if mml < ml:
                    mml = ml
        return mml
s = solution()
st = 'dvdf'
l = s.lengthOfLongestSubstring(st)
print('s: ' + st + ', ml: ' + str(l))
        