class Solution:
    def pivotInteger(self, n: int) -> int:
        l=[]
        sum1=0
        for i in range(n):
            l.append(i+1)
        print(l)
        l2=[]
        l2.append(l[0])
        for j in range(1,n):
            l2.append(l[j]+l2[j-1])
        print(l2)
        for k in range(n-1,-1,-1):
            sum1=sum1+l[k]
            print(sum1)
            if l2[k]==sum1:
                return k+1

        return -1

        