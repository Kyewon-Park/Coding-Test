# Defining main function 

def one(X):
    a,b,c,d = X[0][0],X[0][1],X[1][0],X[1][1]
    return [[a, -a+b],[c, -c+d]]
    
def zero(X):
    a,b,c,d = X[0][0],X[0][1],X[1][0],X[1][1]
    return [[a-b, b], [c-d, d]]

def main(): 
    ans=[]
    x = list(input().split(';'))
    X=[]
    for i in x:
        X.append(list(map(int,i.split())))
    
    Done= False
    while(not Done):
        tempX=zero(X)
        for i in tempX:
            for j in i:
                if i<0:
                    X=one(X)
                    ans.append(1)
                else:
                    X=tempX
                    ans.append(0)
        
        if(X[0][0]==1 and X[0][1]==0 and X[1][0]==0 and X[1][1]==1):
            Done=True
    
    print (str(ans))

if __name__=="__main__": 
    main()
    