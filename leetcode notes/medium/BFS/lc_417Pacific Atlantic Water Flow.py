class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def bfs(starts: list[tuple[int,int]]):       #?用list不行吗   STARTS是变量名，：后面为该变量的类型
            q = deque(starts)   #bfs里一般优先用deque
            visited = set(starts)      #此处不需要定义starts吗  starts是输入变量
            while q:
                x,y = q.popleft()
                for nx,ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):  #上下左右    为什么坐标不用list表示？list 不使用 hash 值进行索引，故其对所存储元素没有可哈希的要求；set / dict 使用 hash 值进行索引，也即其要求欲存储的元素有可哈希的要求。Python不支持dict的key为list或dict类型，因为list和dict类型是unhashable（不可哈希）的。

                    if 0 <= nx <m and 0 <= ny <n and  heights[x][y] <= heights[nx][ny] and (nx,ny) not in visited:     #限定nx和ny的边界范围,以及题目的特殊条件，当前节点的值小于等于周围节点,以及不在当前list里
                        q.append((nx,ny))   #list和deque用append添加新元素
                        visited.add((nx,ny))     #set 用add添加新元素,添加重复的数进去，set不会更新
            return visited
        
        pacific = [(0,i) for i in range(n)] + [(j,0) for j in range(1,m)]    #上+左
        atlantic = [(m-1,i) for i in range(n)] + [(j,n-1) for j in range(m-1)]  #下+右
        return list(map(list,bfs(pacific)&bfs(atlantic)))   #set &是交集intersection |是并集 union


           

        
        
        




