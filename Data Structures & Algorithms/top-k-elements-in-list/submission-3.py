class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        heap = []

        for num, value in count.items():
            #CASE 1: if heap size is greater than k then we need to pop and push to stay under k size
            if len(heap) >= k:
                if heap[0][0] < value:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [value,num])
            #CASE 2: if heap < k just push 
            else:
                heapq.heappush(heap,[value, num])
            
        output = []

        for node in heap:
            output.append(node[1])

        return output      