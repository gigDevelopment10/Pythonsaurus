**1.Target Sum in an Array**
* Which two elements guve the target sum ? <br>
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

**2.Maximum subarray**
