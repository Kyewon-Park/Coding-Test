# Defining main function 
def main(): 
    nums =list(map(int,input().split()))
    n = len(nums)
    stack=[] #작은수 저장소
    stackI=[]
    answer=[0]*n
    maxNum=nums[-1]
    maxI=n-1
    added=False
    for i in range(n-1,0,-1):
        added=False
        presentNum = nums[i]
        if presentNum >= maxNum:
            maxNum=presentNum
            maxI=i
            answer[i]=-1
            stack=[]
            stackI=[]
        else: #presentNum < maxNum
            tempAnswer=-2
            for j in range(len(stack)):
                if presentNum<stack[j]:  
                    tempAnswer=stackI[j]
                    added=True
            if(added):
                answer[i]=tempAnswer
                stack.append(presentNum)
                stackI.append(i)
                continue
            

            answer[i]=maxI

            stack.append(presentNum)
            stackI.append(i)
    print(answer[1:])
    

if __name__=="__main__": 
    main()
    