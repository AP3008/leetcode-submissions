class Solution:
    def canAliceWin(self, n: int) -> bool:
        # We have a ctr = 10, which we decrement. each turn, we have a flag alternate between true and false starting on False. If we can subtract ctr from n then we switch the flag. So if it ends on bobs turn alice wins, and vice versa. Space is O(1) and Time is (10(10+1))/2=110/2=52 is gaurenteed loss, so we get 10 operations at max O(10) => O(n)

        flag = False
        ctr = 10
        while n >= ctr:
            n-=ctr
            ctr-=1
            flag = not flag
        return flag 

