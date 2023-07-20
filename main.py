def polindrome(a,s,e):
    if(s>=e):
        return 1
    if(a[s]!=a[e]):
        return 0
    return polindrome(a,s+1,e-1)
a=input()
print(polindrome(a,0,len(a)-1))
