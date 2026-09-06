class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for n in nums:
            if n in hMap:
                hMap[n] += 1
            else:
                hMap[n] = 1
        
       
        sortedMap = dict(sorted(hMap.items(), key = lambda x:x[1], reverse = True))  
        k_keys = list(sortedMap.keys())[:k] 
        return k_keys
        