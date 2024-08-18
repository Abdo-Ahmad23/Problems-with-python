class Solution:
    def get_all_subarrays2(arr):
        n = len(arr)
        subarrays = []

        # There are 2^n possible subsets
        for i in range(1 << n):  # 1 << n is 2^n
            subarray = []
            for j in range(n):
                # Check if the j-th bit in the integer i is set
                if i & (1 << j):
                    subarray.append(arr[j])
            subarrays.append(subarray)

        return subarrays

    def get_all_subarrays(arr):
        n = len(arr)
        subarrays = []

        # Iterate over all possible starting points
        for i in range(n):
            # Iterate over all possible ending points
            for j in range(i, n):
                # Extract the subarray from index i to j (inclusive)
                subarray = arr[i:j + 1]
                subarrays.append(subarray)

        return subarrays


    def sumOddLengthSubarrays(self, arr) :
        allSubs = Solution.get_all_subarrays(arr)
        sum1=0
        for i in allSubs:
            if len(i) % 2:
                sum1 += sum(i)
                print(i)
                print(sum1)
                print(sum(i))


sol=Solution()
sol.sumOddLengthSubarrays([1,4,2,5,3])
# print(sol.sumOddLengthSubarrays([1,2,3]))

