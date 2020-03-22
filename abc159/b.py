s = input()
l=int((len(s)-1)/2)
s1 = s[:l]
s2 = s[l+1:]
if(s==s[::-1] and s1==s1[::-1] and s2==s2[::-1]):
    print('Yes')
else:
    print('No')