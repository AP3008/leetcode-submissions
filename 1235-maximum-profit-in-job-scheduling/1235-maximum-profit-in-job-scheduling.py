class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # We get a list that zips startTime, endTime and profit together and then we sort them by the endTime so we can see that at minimum for the first "time" duration we can at minimum make the profit associated with that number. 
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # We create a 2D dp which stores the maximum profit achievable by time t, dp[t]
        # dp = [[end_time, max_profit]]
        dp = [[0,0]]
        # s = start time
        # e = end time
        # p = profit for the job
        # At each iteration we have two choices take the job or skip it. If we skip the job our profit remains whatever the best profit from the previously considered jobs were. 
        # If we take the job we can combine it with the jobs that finish at or before s dp[s]. 
        # This means our recurrence relation becomes dp[e] = max(Best profit so far, dp[s]+p).
        # The reason we sort is because it assures that fact that we are looking at new jobs, meaning that all jobs that could have finished before the current one have already been processed. 
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s+1])-1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e,dp[i][1]+p])
        return dp[-1][1]