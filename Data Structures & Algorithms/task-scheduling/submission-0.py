# input: array of cpu tasks (which are strings), and an integer N
# output: the minimum numbe of cpu cycles to complete all tasks
# edge cases: empty array, n = 0, n larger than length of tasks

# match: priority queue, hash map?

# plan:
# brute force: go through every calue and calcauulte how long it would take to process that value
# once we process a value, we hvae to wait n iteratoins until we can process it again. 
# this means we probably wanna process the tasks with the highest frequency first
# the highest frequency items take "priority"
# build a frequency map.
# add the frequencies along with their character into the pririorty queue (
# have a queue to represent the cooldown period
# process a task from the prioroirty queue

# process all frequencies
# add these frequences into a min heap but do * -1 as we add it so it simulates a max heap
# initialize a queue data strucuture
# intiailzie a time vairable = 0
# while the pq is not empty and queue is not empty, we wnat to process tasks
# if pq is not empty, pop the top task and get its frquency. we add 1 bc its negative, and then add it into the queue, along with cur_time + n
# if pq is empty, then we check the queue. if no values in the queue are currently avaialble (the second value has to be = cur_time), then we simply move on and increment cur_time
# once both data strucutures are empty, retuen cur_time



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for task in tasks:
            if task in freq_map:
                freq_map[task] += 1
            else:
                freq_map[task] = 1
        max_heap = []
        for key in freq_map.keys():
            value = freq_map[key]
            heapq.heappush(max_heap, -value) # push -value to simulate max heap
        queue = deque()
        cur_time = 0
        while queue or max_heap:
            while queue and queue[0][1] <= cur_time:
                value, time = queue.popleft()
                heapq.heappush(max_heap, value)
            if max_heap:
                top_val = heapq.heappop(max_heap)
                top_val += 1
                if top_val != 0:
                    queue.append((top_val, cur_time + n + 1))
            cur_time += 1
     
        return cur_time
                    


        