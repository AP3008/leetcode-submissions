class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        # Has to be a DP based on 10^5 being max length. 
        # Apparently uses binary search 
        # Not my solution: O(nlogn)

        # The idea is to instead of hashing, to give our subarrays id's, so on matching subarrays we have the same ID. Since we do this we can combine arrays on different IDs to create a new greater array which is a pair of ID's. We can do this until we create a subarray too large to be recreated in the rest of the array. That is best case but we record the largest combination we have. So at most we need to repeat the merge log2(n) times to represent all power of two lengths we need. 

        #n = len(nums)
        #names = [nums]
        #for k in range(n.bit_length()-1): # We use bit length because we only need to iterate log2(n) times. Since binary is representative of powers of 2 this works out like this. 
            #ids = {}
            #names.append([ids.setdefault(pair, len(ids)) for pair in zip(names[k], names[k][2**k:])])
        
        #def found(length):
            #k = length.bit_length()-1
            # return 1 in Counter(zip(names[k], names[k][length-2**k:])).values()
        # bisect_left is just a binary search where we give the first arg a sorted list, and second the target, with the key being a function that we tell it to apply before comparing them to the target.  
        #return bisect_left(range(1,n), True, key=found)+1

        # Readable solution 
        n = len(nums)

        # names[k][i] represents the ID of a subarray
        # starting at i with length 2**k.
        names = [nums]

        # Precompute IDs for all power-of-two lengths.
        for k in range(n.bit_length() - 1):
            ids = {}
            new_names = []
            block_size = 2**k
            previous = names[k]

            # Combine two adjacent blocks of size 2**k.
            for i in range(len(previous) - block_size):
                pair = (
                    previous[i],
                    previous[i + block_size]
                )
                # Assign an ID to each distinct pair.
                if pair not in ids:
                    ids[pair] = len(ids)
                new_names.append(ids[pair])
            names.append(new_names)

        # Check if a unique subarray of this length exists.
        def found(length):

            # Largest power of two that fits inside length.
            k = length.bit_length() - 1
            block_size = 2**k

            # Distance between the first and last block.
            offset = length - block_size
            count = Counter()
            for i in range(n - length + 1):
                # Two potentially overlapping blocks
                # represent the entire subarray.
                pair = (
                    names[k][i],
                    names[k][i + offset]
                )
                count[pair] += 1
            return 1 in count.values()

        # Binary search for the smallest valid length.
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if found(m):
                r = m
            else:
                l = m + 1
        return l