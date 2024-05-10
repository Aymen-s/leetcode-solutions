class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -= 1
        N = len(arr)
        ans = []
        for i in range(N-1,-1,-1):
            maximum = i
            for j in range(i,-1,-1):
                if arr[j] > arr[maximum]:
                    maximum = j
            if maximum != i:
                flip(maximum)
                flip(i)
                ans.append(maximum + 1)
                ans.append(i+1)
        return ans

        