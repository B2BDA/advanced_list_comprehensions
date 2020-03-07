l=[1,2,3,4]
#simple list comprehension	
[i for i in l if i!=1]
#conditional list comprehension
['even' if i%2==0 else 'odd' for i in l]
#nested list comprehension
l=[(1,2,3), (4,5,6)]

['even' if x %2==0 else 'odd' for i in l for x in i ]
#set comprehension
{'even' if x %2==0 else 'odd' for i in l for x in i }
#dict comprehension
l=['a','b','c','c','a','d','a']

{x: len(x) for x in l}

from collections import Counter

Counter(l)