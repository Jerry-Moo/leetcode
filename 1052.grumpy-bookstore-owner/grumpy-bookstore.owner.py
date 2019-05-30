class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        
        maxSatisfied_customers = 0
        for n in range(0,len(customers)):
            if int(grumpy[n]) == 0:
                maxSatisfied_customers += customers[n]
                customers[n] = 0

        val = customers[0]
        maxval = customers[0]
        for n in range(1,len(customers)):
            if n < X:
                val = val + customers[n]
            else:
                val = val + customers[n] - customers[n-X]
            if val > maxval:
                maxval = val
                
        return int(maxSatisfied_customers) + int(maxval)