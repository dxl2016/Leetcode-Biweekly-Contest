class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        if n == 1:
            return True
        
        root = [1 for _ in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                root[leftChild[i]] = 0
            if rightChild[i] != -1:
                root[rightChild[i]] = 0
                
        if sum(root) != 1:
            return False
        
        idx = root.index(1)

        seen = set()
        q = deque()
        seen.add(idx)
        if leftChild[idx] != -1:
            q.append(leftChild[idx])
        if rightChild[idx] != -1:
            q.append(rightChild[idx])
     
        while(q):
            tmp = q.pop()
            if tmp in seen:
                return False
            seen.add(tmp)
            if leftChild[tmp] != -1:
                q.append(leftChild[tmp])
            if rightChild[tmp] != -1:
                q.append(rightChild[tmp])

        if len(seen) != n:
            return False
    
        return True

