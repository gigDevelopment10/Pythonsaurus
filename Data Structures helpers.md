**1.Target Sum in an Array**
* Which two elements give the target sum ; return the indices? <br>
  Approaches -> Brute Force O(n^3) <br>
             -> Optimize Brute force O(n^2) <br>
             -> Two Pointer Method O(n) Needs Sorted array <br>
             ``` diff
             -> Hashing O(n) Works on ordered list <br>
             ```
             <br>
             -> Remainder Hashing O(n+x) <br>

Pseudocode 
```
# Hashing  : 
d = {}
if index,value in enumerate(nums):
   return (d[target-value], index)   
else: 
   d[value] = index
```
 
**2.Maximum subarray**
* find the subarray with the largest sum, and return its sum <br>
  Approaches -> Brute Force O(n^3) <br>
             -> Optimized Brute Force O(n^3) <br>
             -> Divide and conquer -> Merge Sort O(nlogn) <br>
             -> Dynamic Programming T: O(n) S:O(n) <br>
             ``` diff
             -> Kandane's Algorithm T: O(n) S:O(1) <br>
             ```
            
Pseudocode 
```
# Kandanes algo : 
sum = 0
max_sum = maxsize

for i in range(len(nums)):
    sum += nums[i]
    max_sum = max(sum,max_sum)
    if sum < 0 : sum = 0
return max_sum
```

**3.Intersection of two arrays**

Two pointer approach<br>
T: O(nlogn) + O (n+m)<br>

Pseudocode:
```
# Two pointer approach
nums1.sort()
nums2.sort()
m = 0
n = 0 
lists = []

while(m<=(len(nums1)-1) and n<=(len(nums2)-1)):
    if nums1[m] == nums2[n]: 
        lists.append(nums1[m])
        m+=1
        n+=1
    else:
        if nums1[m]<nums2[n]:
            m+=1 
        else :
            n+=1
return lists
```

**4.Best time to buy and sell stocks** <br>
Incremental array approach <br>
maximize the profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock <br>
Pseudocode:
```
# Incremental array approach
min = prices[0]
profit = 0 

for i in prices:
    # [7,1,5,3,6,4]
    if  i < min : 
        min = i 
    pft = i - min 
    if profit < pft : 
        profit = pft

return profit
```


