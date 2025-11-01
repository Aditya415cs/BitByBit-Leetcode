class Solution(object):
    def countValidSelections(self, nums):
        n = 0  
        for start in range(len(nums)):  
            if nums[start] == 0:
                for direction in ["l", "r"]:  
                    arr = nums[:]  
                    curr = start
                    dir = direction
                    while 0 <= curr < len(arr):
                        if arr[curr] == 0:
                            if dir == "l":
                                curr -= 1
                            else:
                                curr += 1
                        else:
                            arr[curr] -= 1
                            if dir == "l":
                                dir = "r"
                            else: 
                                dir = "l" 
                            if dir == "r":
                                curr += 1
                            else:
                                curr -= 1
                    
                    zero = True
                    for x in arr:
                        if x != 0:
                            zero = False
                            break
                    if zero:
                        n += 1

        return n
