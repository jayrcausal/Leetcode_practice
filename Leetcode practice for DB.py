#leetcode practice memo:
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

#add two sums


l1 = [9,9,9,9,9,9,9,9]
l2 = [9,9,9,9]
n1=len(l1)
n2 = len(l2)
answer = 0

for i in range(n1):
    answer = answer + l1[i]*10**i+l2[i]*10**i

print(answer)

string = "abcdkel"
print(string[5] == string[6])

#longest substring without repeated characters.

class Solution7:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dic = {}
        res = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            res = max(res, r - l + 1) # why do we need this?
            dic[s[r]] = r
        return res
    

#Review the ListNode: how they are structured and how they should be accessed. 
# Merge SOrt:
class SolutionMergeSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a,b,write_index = m-1, n-1, m+n-1
        while b>=0:
            if a>=0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a-=1
            else:
                nums1[write_index] = nums2[b]
                b-=1
            write_index -=1

# let break down the cases;
#else part include all cases for a <0, all cases for a >=0 but nums1[a]<=nums2[b]
#if a becomes less 0, which means all elements in nums1 (index <=m-1) have been sorted in the entire array.
#just imagine : nums1 [3,5,9,0,0,0,0] nums2 [1,5,6,7] a = 3-1=2, b =4-1=3 , index = 3+4-1=6
#iteration1 : [3,5,9,0,0,0,9], update a =1, b=3, index 5
#interation2 : [3,5,9,0,0,7,9] update a=0, b=2 index =4
#iteration 3 : [3,5,9,0,6,7,9] update a =0, b=1, index =3
#iteration 4 : [3,5,9,5,6,7,9] update a =0 b=0, index =2
#interation 5 [3,5,5,5,6,7,9] update a= 0 b=-1
#interation 6 [3,3,5,5,6,7,9] a=-1,b =0
# when a <0, else part executes and num1[0] was correctly replaced by num2[0]
#results = [1,3,5,5,6,7,9]

#Remove elements
class SolutionRemove1:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = len(nums)
        i=0
        while i <= l-1:
            if nums[i] == val:
                nums.remove(nums[i])
                l-=1
            else:
                i+=1
                k+=1
        return k

#break down cases:
#nums =[3,2,2,3], val = 3,l=4, i =0,k=0
#s1: 3==3. remove, nums = [2,2,3] i = 0 l=3
#s2 : 2 !=3,not remove nums = [2,2,3], i=1 ,l=3 k=1
#s3 : 2!= 3, not remove, nums= [2,2,3], i =2 l=3, k=2
#s4: 3==3, remove, sums = [2,2], 
class SolutionRemove2:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)
        
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i
#this is more efficient



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

#add two sums


l1 = [9,9,9,9,9,9,9,9]
l2 = [9,9,9,9]
n1=len(l1)
n2 = len(l2)
answer = 0

for i in range(n1):
    answer = answer + l1[i]*10**i+l2[i]*10**i

print(answer)

string = "abcdkel"
print(string[5] == string[6])

#longest substring without repeated characters.

class Solution7:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        dic = {}
        res = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            res = max(res, r - l + 1) # why do we need this?
            dic[s[r]] = r
        return res
    

#Review the ListNode: how they are structured and how they should be accessed. 
# Merge SOrt:
class SolutionMergeSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a,b,write_index = m-1, n-1, m+n-1
        while b>=0:
            if a>=0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a-=1
            else:
                nums1[write_index] = nums2[b]
                b-=1
            write_index -=1

# let break down the cases;
#else part include all cases for a <0, all cases for a >=0 but nums1[a]<=nums2[b]
#if a becomes less 0, which means all elements in nums1 (index <=m-1) have been sorted in the entire array.
#just imagine : nums1 [3,5,9,0,0,0,0] nums2 [1,5,6,7] a = 3-1=2, b =4-1=3 , index = 3+4-1=6
#iteration1 : [3,5,9,0,0,0,9], update a =1, b=3, index 5
#interation2 : [3,5,9,0,0,7,9] update a=0, b=2 index =4
#iteration 3 : [3,5,9,0,6,7,9] update a =0, b=1, index =3
#iteration 4 : [3,5,9,5,6,7,9] update a =0 b=0, index =2
#interation 5 [3,5,5,5,6,7,9] update a= 0 b=-1
#interation 6 [3,3,5,5,6,7,9] a=-1,b =0
# when a <0, else part executes and num1[0] was correctly replaced by num2[0]
#results = [1,3,5,5,6,7,9]

#Remove elements
class SolutionRemove1:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = len(nums)
        i=0
        while i <= l-1:
            if nums[i] == val:
                nums.remove(nums[i])
                l-=1
            else:
                i+=1
                k+=1
        return k

#break down cases:
#nums =[3,2,2,3], val = 3,l=4, i =0,k=0
#s1: 3==3. remove, nums = [2,2,3] i = 0 l=3
#s2 : 2 !=3,not remove nums = [2,2,3], i=1 ,l=3 k=1
#s3 : 2!= 3, not remove, nums= [2,2,3], i =2 l=3, k=2
#s4: 3==3, remove, sums = [2,2], 
class SolutionRemove2:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)
        
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i
#this is more efficient