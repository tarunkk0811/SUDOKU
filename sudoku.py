r=9
c=9
#Read input
s="53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"


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
        


#print output logic
for i in range(r):
    for j in range(c):
        if((j+1)%3==0 and (j+1)!=9):
            print(""+str(mat[i][j]),end="| ")

        else:
            print(mat[i][j],end="  ")
    print()
    if(i!=8):
        print("-------------------------")
#print("Sudoku sample")
