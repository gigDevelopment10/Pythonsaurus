<h1>Python shortcuts</h1>

**Split a string in k equal parts** <br>
output = ['aaa', 'bba', 'csa']; string = 'aaabbacsa'; k = 3 
```
list(map(''.join, zip(*[iter(string)]*k)))

```
