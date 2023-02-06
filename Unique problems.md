Pascals Problem 
1. Print pascals problem 
2. Print the number at paticular index in a pascals table -> (r-1)C(c-1) combinatorials 
3. print Nth row of pascals table

Pascals table pseudo code
```
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        triangle = [[1]]
        for i in range(1,numRows):
            row =[1]*(i+1)
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
```
