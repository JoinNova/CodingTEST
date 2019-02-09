def con(num,jin):
    pettern='0123456789ABCDEF'
    result=''
    if num==0:result='0'
    else:
        while num:
            result+=str(pettern[num%jin])
            num=num//jin
            #print(num)
    return result[::-1]
'''
for k in range(16*16+1):       
    #print(con(k,2),bin(k)[2:])#,sep='\n')
    if con(k,2)==bin(k)[2:]:
        print(True)
'''

n,t,m,p=map(int,input().split())
i=0;j=0;fin=0;tube=''
while 1:
    chk=con(i,n)
    #print(chk)
    for _ in chk:
        #print(_,end='')
        if j%m+1==p:
            tube+=_
            #print(_)
        if len(tube)==t:fin=1;break
        j+=1
    if fin==1:break
    i+=1
print(tube)
