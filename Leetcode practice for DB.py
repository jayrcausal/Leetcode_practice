#leetcode practice memo:
#create a rep matrix using input index:
matrix = [[6,3,5,9],
          [7,6,7,4],
          [5,0,3,7]]
matrix
#index of the given matrix/grid
m = len(matrix)
n = len(matrix[0])
#create a full rep
rep= [[1]*n for _ in range(m)]
rep
zip(*matrix)

# sort using sorted and lambda key

sort_matrix = sorted(matrix,key=lambda x: x[0])
print(sort_matrix)

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)


# sort using the second key:
class Solution4:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: [x.bit_count(), x]) 
# first key: order by the # of bits; second key: with two same bits,just order by its value

#Binary Search Practice and decomposition:
class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m=len(mat)
        n= len(mat[0])
        ind = -1
        ind_col = []
        for j in range(n):
            base=0
            for i in range(m):
                if mat[i][j]>base:
                    base = mat[i][j]# linear search to keep track the maximum element, else omitted because we do wanna do anything for non-maximum
                    ind = i 
            ind_col.append(ind)
        
        min,max = 0, n-1
        while min <= max:
            for k in ind_col:# wrong because we do not need to tranverse all columns
                mid = min + (max-min)//2
                left = mat[k][mid-1] if mid-1>=0 else -1 #check if the current position is the first one
                right = mat[k][mid+1] if mid+1 < n-1 else -1 # check if the current position is the last one

                if mat[k][mid] > left and mat[k][mid] > right:
                    return [k,mid]
                elif mat[k][mid]<left:
                    max = mid-1
                else:
                    min = mid+1
        return [-1,-1]
    
id = Solution()
idx = id.findPeakGrid([[45,35,27,15,29],[38,18,1,49,11],[45,28,22,18,10],[14,49,7,6,25],[7,23,39,17,3]])
print(idx)

#similar linear search:

class Solution3:
    def buyChoco(self, prices: list[int], money: int) -> int:
        n = len(prices)
        base= float("inf")
        for i in range(n):
            for j in range(i+1,n):
                if prices[i]+prices[j] < base : #access element[i] executes an extra step so it might be slower
                    base = prices[i]+prices[j]
        leftover = money-base

        return leftover if leftover >=0 else money

#loop practice: 
class Solution1:
    def countPoints(self, points: list[List[int]], queries: list[List[int]]) -> list[int]:
        answer = []
        for q in queries:
            i=0
            for p in points:
                if (p[0]-q[0])**2 + (p[1]-q[1])**2 <= q[2]**2:
                    i+=1
            answer.append(i)
        
        return answer
    
class EfficientSolution1:
    #
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        res = []
        for x,y,r in queries:
            count = 0
            for a,b in points:
                if (x-a)*(x-a) + (y-b)*(y-b) <= r*r:
                    count += 1
            res.append(count)
        return res
    
#In Code 1, you directly unpack the elements (x, y, r) from each query in the loop header, 
#while in Code 2, you first iterate over the queries as q and then access its elements using x, y, r = q.
    
#loop for lattice points: variation
class Solution2:
    def countLatticePoints(self, circles: list[list[int]]) -> int:
        answer = set()
        for x,y,r in circles: #iterate each (x,y,r)
            for i in range(x-r,x+r+1): # find all integer points for the point (x,y,r)
                for j in range(y-r,y+r+1):
                    if (x-i)**2 +(y-j)**2 <= r**2:
                        answer.add((i,j))
        return answer
    
Lattice = Solution2()
print(Lattice.countLatticePoints([[2,2,2],[3,4,1]]))



    
