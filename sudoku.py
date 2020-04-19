
        


#print output logic
def prin():
    for i in range(r):
        for j in range(c):
            if((j+1)%3==0 and (j+1)!=9):
                print(""+str(mat[i][j]),end="         |")

            else:
                print(mat[i][j],end="         ")
        print()
        if(i!=8):
            print("-------------------------")

#Possible elements
def Pele():
    for i in range(r):
        for j in range(c):
            el="123456789"
            el=[i for i in el]
            if(mat[i][j]==" "):
                for k in range(r):
                    if mat[k][j] in el and len(mat[k][j])==1:
                        #print(mat[k][j])
                        el.pop(el.index(mat[k][j]))
                for k in range(c):
                    if mat[i][k] in el and len(mat[k][j])==1:
                        #print(mat[i][k])
                        el.pop(el.index(mat[i][k]))
                mat[i][j]="".join(el)
    


r=9
c=9

#Read input
#s="53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
s=input()
#Generate matrix mat
mat=[]
k=0
for i in range(0,len(s),9):
    mat.append([])
    for j in range(i,i+9):
        if(s[j]!='.'):
            mat[k].append(s[j])
        else:
            mat[k].append(" ")
    k+=1
Pele()
prin()
