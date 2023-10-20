# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def flatten(self, nested_list) -> list:
        l = []
        for n in nested_list:
            if n.isInteger():
                l.append(n.getInteger())
            else:
                l.extend(self.flatten(n.getList()))
                
        return l
    
    
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.l = self.flatten(nestedList)
    
    def next(self) -> int:
        res = self.l[self.idx]
        self.idx += 1
        return res
    
    def hasNext(self) -> bool:
         return self.idx < len(self.l)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())