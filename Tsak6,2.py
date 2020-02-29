keys = ['Банан','Яблуко','Апельсин','Груша']
a = [6,0,32,15]
b = [4,2,1.5,3]
c = [a*b for a,b in zip(a,b)]
dict = {keys:c for(keys,c) in zip(keys,c)}
print(dict)