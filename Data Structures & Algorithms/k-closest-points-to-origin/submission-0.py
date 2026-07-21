# input: a 2d array points of integers, and k, which represnets the k closest pionts we need to the origin
# output: list of lists (so list of points) that are the k closest to the origin
# edge cases: no points in the array , negative numbers, only one point in the array

# match: priorirty queue, iterations

# plan:
# initialize a priority queue of size k, and make it a max heap. this way, we can check the largest of the k points at each iteration, and knock it if a smaller number appears.
# loop through points. at each iteraiton, calculate the euclidean distance. 
# if len(pq) < k, we can just push the value in
# otherwise, check if the current distacne is less than the top distance
# if its not, it wouldnt be any closer than any other point, and we're all good
# if it is, we pop the top because it was the least close of the k points, and we push in our distance
# at the end, we can return our max heap



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_pq = []
        for i in range(len(points)):
            cur_distance = math.sqrt((points[i][0] * points[i][0]) + (points[i][1] * points[i][1]))
            if len(max_pq) < k:
                heapq.heappush_max(max_pq, (cur_distance, i))
            else:
                if cur_distance < max_pq[0][0]:
                    heapq.heappop_max(max_pq)
                    heapq.heappush_max(max_pq, (cur_distance, i))
        closest_points = []
        while max_pq:
            current_point, index = heapq.heappop_max(max_pq)
            closest_points.append(points[index])
        return closest_points

        