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

#individual box check for possible ele
def boxcheck(mat,i,j,res_lis):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if(mat[x][y] in res_lis) and (len(mat[x][y])==1):
                res_lis.pop(res_lis.index(mat[x][y]))
    return res_lis
                
        
#possible element for box unit
def box(mat,i,j,rc_result_list):
    #box1
    if(i<3 and j<3):
        return boxcheck(mat,0,0,rc_result_list)
    #box2
    elif(i<3 and j>2 and j<6):
        return boxcheck(mat,0,3,rc_result_list)
    #box3
    elif(i<3 and j>5):
        return boxcheck(mat,0,6,rc_result_list)
    #box4
    elif(i>2 and i<6 and j<3):
        return boxcheck(mat,3,0,rc_result_list)
    #box5
    elif(i>2 and i<6 and j>2 and j<6):
        return boxcheck(mat,3,3,rc_result_list)
    #box6
    elif(i>2 and i<6 and j>5):
        return boxcheck(mat,3,6,rc_result_list)
    #box7
    elif(i>5 and j<3):
        return boxcheck(mat,6,0,rc_result_list)
    #box8
    elif(i>5 and j>2 and j<6):
        return boxcheck(mat,6,3,rc_result_list)
    #box9
    elif(i>5 and j>5):
        return boxcheck(mat,6,6,rc_result_list)
        
    


#Possible elements for row and col units
def Pele():
    for i in range(r):
        for j in range(c):
            el=[str(i) for i in range(1,10)]
            if(mat[i][j]==" "):
                for k in range(r):
                    if (mat[k][j] in el) and len(mat[k][j])==1:
                        #print(mat[k][j])
                        el.pop(el.index(mat[k][j]))
                for k in range(c):
                    if (mat[i][k] in el) and len(mat[k][j])==1:
                        #print(mat[i][k])
                        el.pop(el.index(mat[i][k]))
                ress=box(mat,i,j,el)
                mat[i][j]="".join(ress)
                

r=9
c=9

#Read input
s="53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
#s=input()
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
