arr = [1,2,3,5,7,5,6,2,1]
s = "nandini"
mp={}
sp ={}
for ch in s:
  sp[ch] = sp.get(ch,0) + 1
print(sp)
for num in arr:
  mp[num] = mp.get(num,0)+1
print(mp)