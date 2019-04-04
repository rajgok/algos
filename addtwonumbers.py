class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class SolutionObject(object):
    def LL2L(self,ll):
        l = list()        
        while ll != None:
            l.append(ll.val)
            ll = ll.next
        l.reverse()
        return l

    def printLL(self, ll):
        if ll == None :                        
            print('Done...')            
            return ''
        print(str(ll.val) + '->' )
        return self.printLL(ll.next) 
        

    def L2LL(self,l):        
        ll = ListNode(l[0])       
        l.pop(0)
        llc = ll
        for s in l:            
            llc.next = ListNode(s)
            llc = llc.next
        return ll

    def add2numbers1(self, l1,l2):
        lres = list()
        i1 = self.LL2L(l1)
        i2 = self.LL2L(l2)
        len1 = len(i1)
        len2 = len(i2)
        if len1 == 0:
            return i2
        if len2 == 0:
            return i1            
        if len1 >= len2:
            diff = len1 - len2
            cnt = len2-1
            cf = 0
            rem = 0
            while cnt >= 0:
                s = i2[cnt]+ i1[cnt+diff] + cf
                rem = s % 10                
                lres.append(rem)
                cf = int(s / 10)
                cnt-=1                          
            while diff-1 >=0:
                s = i1[diff-1] + cf
                rem = s %10
                lres.append(rem)
                cf = int(s/10)
                diff-=1               
            if cf > 0:
                    lres.append(cf)
        if len1 < len2:
            diff = len2 - len1
            cnt = len1 -1
            cf = 0
            rem = 0
            while cnt >= 0:
                s = i1[cnt]+ i2[cnt+diff] + cf
                rem = s % 10                
                lres.append(rem)
                cf = int(s / 10)
                cnt-=1                       
            while diff-1 >=0:
                s = i2[diff-1] + cf
                rem = s %10
                lres.append(rem)
                cf = int(s/10)
                diff-=1
            if cf > 0:
                    lres.append(cf)                
        print('i1 : %s' % (lres,))
        return self.L2LL(lres)

    def add2numbers(self, l1,l2):
        lres = list()
        i1 = list(l1)
        i2 = list(l2)
        len1 = len(i1)
        len2 = len(i2)
        if len1 == 0:
            return i2
        if len2 == 0:
            return i1            
        if len1 >= len2:
            diff = len1 - len2
            cnt = len2-1
            cf = 0
            rem = 0
            while cnt >= 0:
                s = i2[cnt]+ i1[cnt+diff] + cf
                rem = s % 10                
                lres.append(rem)
                cf = int(s / 10)
                cnt-=1            
            while diff-1 >=0:
                s = i1[diff-1] + cf
                rem = s %10
                lres.append(rem)
                cf = int(s/10)
                diff-=1

        if len1 < len2:
            diff = len2 - len1
            cnt = len1 -1
            cf = 0
            rem = 0
            while cnt >= 0:
                s = i1[cnt]+ i2[cnt+diff] + cf
                rem = s % 10                
                lres.append(rem)
                cf = int(s / 10)
                cnt-=1         
            while diff-1 >=0:
                s = i2[diff-1] + cf
                rem = s %10
                lres.append(rem)
                cf = int(s/10)
                diff-=1
        return lres

    def add2numbers2(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if carry != 0:
                return ListNode(carry) 
            return None
        if l1 != None and l2 == None:
            s = (l1.val + carry) % 10
            carry = (l1.val + carry) / 10
            sum = ListNode(int(s))
            sum.next = self.add2numbers2(l1.next, l2,int(carry))            
        if l1 == None and l2 != None:
            s = (l2.val + carry) % 10
            carry = (l2.val + carry) / 10
            sum = ListNode(int(s))
            sum.next = self.add2numbers2(l1, l2.next,int(carry))            
        if l1 != None and l2 != None:
            s = (l1.val + l2.val + carry ) % 10
            carry = (l1.val + l2.val + carry) / 10
            sum = ListNode(int(s))
            sum.next = self.add2numbers2(l1.next, l2.next, int(carry))
        return sum
s = SolutionObject()
#l1 = ListNode(5)
l1 = ListNode(3)
l1.next = ListNode(7)

l2 = ListNode(9)
l2.next = ListNode(2)

# l1 = ListNode(1)
# l1.next = ListNode(8)
#l1.next.next= ListNode(3)

# l2 = ListNode(0)
# l2.next = ListNode(6)
# l2.next.next =ListNode(4)

# l1 = [1,2,3,4]
# l2 = [3,4,5,6,7]
res = s.add2numbers2(l1,l2,0)
# print('i1 : %s' % (l1,))
# print('i1 : %s' % (l2,))
s.printLL(l1)
s.printLL(l2)
print('Result Sum2 : ')
print(s.printLL(res))

