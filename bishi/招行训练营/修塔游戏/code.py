n, k = list(map(int, input().strip().split(' ')))
nums = list(map(int, input().strip().split(' ')))
 
nums = sorted(nums)
total = sum(nums)
pre = [0]
 
for x in nums:
    pre.append(x+pre[-1])
 
res = float('inf')
 
for i in range(n-k+1):
    a = nums[i]
    ans = total - pre[i+1] - (a+1) * (n-i-1)
    res = min(res, ans+k-1)
 
for i in range(k-1, n):
    a = nums[i]
    ans = (a-1) * i - pre[i]
    res = min(res, ans+k-1)
     
print(res)




s=input().split()
n=int(s[0])
k=int(s[1])
s=input().split()
l = list(map(lambda x: int(x),s)  )
 
 
#NN=10001
NN=10001
haxi=[0]*NN
 
for num in l:
    haxi[num]+=1
 
     
 
left_count=[0]*NN
left_count[0]=haxi[0]
left_sum=[0]*NN
left_sum[0]=haxi[0]
 
right_count=[0]*NN
right_count[-1]=haxi[-1]
right_sum=[0]*NN
right_sum[-1]=haxi[-1]
for i in range(1,NN):
    left_sum[i]=left_sum[i-1]+haxi[i]
    left_count[i]=left_count[i-1]+left_sum[i]
    j=NN-1-i
    right_sum[j] = right_sum[j+1]+haxi[j]
    right_count[j]=right_count[j+1]+right_sum[j]
 
#print(left_sum)
#print(left_count)
#print(right_sum)
#print(right_count)
ans=-1
if k<=haxi[NN-1]+left_sum[NN-2]:
    ans=left_count[NN-2]+k-haxi[NN-1]-left_sum[NN-2]
    #print(ans)
if k<=haxi[0]+right_sum[1]:
    temp=right_count[1]+k-haxi[0]-right_sum[1]
    if ans!= -1:
        ans=min(ans, temp)
    else:
        ans=temp
    #print(temp)
 
for i in range(1,NN-1):
    c=left_count[i-1]+right_count[i+1]+k-haxi[i]-right_sum[i+1]-left_sum[i-1]
    temp=[ans,c]
    if k<=haxi[i]+left_sum[i-1]:
        a=left_count[i-1]+k-haxi[i]-left_sum[i-1]
        temp.append(a)
    if k<=haxi[i]+right_sum[i+1]:
        b=right_count[i+1]+k-haxi[i]-right_sum[i+1]
        temp.append(b)
    #print(temp)
    ans=min(temp)
print(ans)
