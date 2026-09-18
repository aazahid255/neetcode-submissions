# input: num courses, pre requisites
# output: a valid ordering of courses
# edge cases: no courses, cycle in our courses

# match: dfs, graph theory

# plan:
# exact same plan as course schedule 1, but as we build a dfs, we wanna store it in a list. once the len of this list reaches the same number as numcourses, then we can return it as a base case, otherweise we return
# plan to acc implement?
# create map of courses and their prereqs
# have a visitset
# have a dfs that takes crs and path
# if len(path) is eaual to numcourses, retyrn this path
# check if the current crs is in visited, which we return if it is
# check if prerequisites = 0

# for all the prereqs of this course, run a dfs
# add it to visit set before the call, remove it after
# after this loop, we run dfs on all the prereqs
# return false if any point a prereq is in the visitset
# on the dfs loop, if not dfs(crs, path), return false


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.preMap = {i:[] for i in range(numCourses)}
        self.output = []
        self.completedSet = set()
        for crs, pre in prerequisites:
            self.preMap[crs].append(pre)

        self.visitSet = set()

        def dfs(crs):
            if crs in self.visitSet:
                return False
            if crs in self.completedSet:
                return True
            
            self.visitSet.add(crs)
            for pre in self.preMap[crs]:
                if not dfs(pre): return False
            self.visitSet.remove(crs)

            self.completedSet.add(crs)
            self.output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i): 
                return []

        return self.output
            



        