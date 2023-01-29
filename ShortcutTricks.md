<h1>Python shortcuts</h1>

Split a string in k equal parts
```
list(map(''.join, zip(*[iter(string)]*k)))
# output = ['aaa', 'bba', 'csa']; string = 'aaabbacsa'; k = 3 
```
