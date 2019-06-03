class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=1
        flag=0
        zero=0
        for i in nums:
            if i==0:
                zero+=1
            else:
                flag=1
                count*=i
        if zero>=2:
            return [0*i for i in nums]
        elif zero==1:
            L=[0*i for i in nums]
            L[nums.index(0)]=count
            return L
        
        L=[]
        for i in nums:
            if flag==1:
                if i!=0:
                    num=count/i
                    L.append(num)
                elif i==0:
                    L.append(count)
            else:
                L.append(0)
        return L
