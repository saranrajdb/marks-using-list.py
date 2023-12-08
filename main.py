n=int(input())
l=list(map(int,input().split()))
t=[]
for i in range(n):
  if l[i] not in t:
    t.append(l[i])
  else:
    l[i]=l[i-1]+1
    t.append(l[i])
print(l)
print(sum(l))

# ip:
# 7
# 1 2 3 2 3 4 5

# op:
# [1, 2, 3, 4, 5, 6, 7]
# 28