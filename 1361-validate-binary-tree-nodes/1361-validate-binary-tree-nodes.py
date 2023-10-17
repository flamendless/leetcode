class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        s = set(leftChild)
        
        for i in rightChild:
            s.add(i)
            
        for i in range(n):
            if i not in s:
                root = i
                
        v = set()
        q = deque([root])
        
        while q:
            cur = q.popleft()
            if cur in v:
                return False
            
            v.add(cur)
            l, r = leftChild[cur], rightChild[cur]
            if l != -1:
                q.append(l)
            if r != -1:
                q.append(r)
                
        return len(v) == n