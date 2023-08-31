end=300000
v=299999
for i in range(2,int(v**0.5)+1,1):
    if v%i==0:
        print(v,"소수아님")
        break
N=end
prime=[0 for i in range(N)]
for i in range(2,N):
    if (i*i>=N):
        break
    if prime[i-1]==0: #만약 소수면
        for k in range(i*i,N+1,i):
            prime[k-1]=1
for i in range(end):
    if prime[i]==0:
        print(i+1)