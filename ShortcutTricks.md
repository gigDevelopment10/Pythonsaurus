<h1>Split a string in n equal parts </h1>

```
#String = 'AAAABCDSA'
#k = 3
list(map(''.join, zip(*[iter(string)]*k)))
```
