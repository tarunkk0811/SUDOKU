import tkinter as tk
from flask import Flask,render_template

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 9,9)
        t.pack(side="top", fill="x")

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=9, columns=9):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for i in range(rows):
            current_row = []
            for j in range(columns):
                label = tk.Label(self, text="%s" % (mat[i][j]), 
                                 borderwidth=0, width=15)
                label.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)



def del_Eles(mat,i,j):
    #for deleting fixed elements in rows
    for k in range(c):  #to traverse through rows
        if(j!=k):
            if(len(mat[i][k])>1):
                ele=mat[i][k]
                if(mat[i][j] in ele):
                    l=[x for x in ele]
                    l.pop(l.index(mat[i][j]))
                    if(len(l)==1):
                        mat[i][k]="".join(l)
                        del_Eles(mat,i,k)
                    else:
                        mat[i][k]="".join(l)
     #for deleting fixed elements in columns           
    for y in range(r):
        if(i!=y): #ignore ele which we are searching for
            if(len(mat[y][j])>1):
                ele=mat[y][j]
                if(mat[i][j] in ele):
                    l=[x for x in ele]
                    l.pop(l.index(mat[i][j]))
                    if(len(l)==1):
                        mat[y][j]="".join(l)
                        del_Eles(mat,y,j)
                    else:
                        mat[y][j]="".join(l)
                        
    #for deleting fixed elements in the box unit
    box(mat,i,j,[],boxDel)
    #Here for this approach i ve given many parameters to resuse the box function code
    #This step deletes the fixed eles from the respective box unit
                        
    
            

#individual box check for possible ele
def boxcheck(mat,i,j,l,o,res_lis):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if(mat[x][y] in res_lis) and (len(mat[x][y])==1):
                res_lis.pop(res_lis.index(mat[x][y]))
    return res_lis

#Box removal function                
def boxDel(mat,i,j,x,y,l):
    for a in range(i,i+3):
        for b in range(j,j+3):
            if(mat[x][y] in mat[a][b]) and (x!=a or y!=b):
                ele=mat[a][b]
                ele=[m for m in ele]
                ele.pop(ele.index(mat[x][y]))
                if(len(ele)==1):
                    mat[a][b]="".join(ele)
                    del_Eles(mat,a,b)
                else:
                    mat[a][b]="".join(ele)
                

        
#possible element for box unit
def box(mat,i,j,rc_result_list,fun):
    #box1
    if(i<3 and j<3):
        return fun(mat,0,0,i,j,rc_result_list)
    #box2
    elif(i<3 and j>2 and j<6):
        return fun(mat,0,3,i,j,rc_result_list)
    #box3
    elif(i<3 and j>5):
        return fun(mat,0,6,i,j,rc_result_list)
    #box4
    elif(i>2 and i<6 and j<3):
        return fun(mat,3,0,i,j,rc_result_list)
    #box5
    elif(i>2 and i<6 and j>2 and j<6):
        return fun(mat,3,3,i,j,rc_result_list)
    #box6
    elif(i>2 and i<6 and j>5):
        return fun(mat,3,6,i,j,rc_result_list)
    #box7
    elif(i>5 and j<3):
        return fun(mat,6,0,i,j,rc_result_list)
    #box8
    elif(i>5 and j>2 and j<6):
        return fun(mat,6,3,i,j,rc_result_list)
    #box9
    elif(i>5 and j>5):
        return fun(mat,6,6,i,j,rc_result_list)
        
    


#Possible elements for row and col units
def Pele(mat,r,c):
    for i in range(r):
        for j in range(c):
            el=[str(i) for i in range(1,10)]
            if(mat[i][j]==" "):
                for k in range(r):
                    #keep the column constant and traverse through different rows
                    if (mat[k][j] in el) and len(mat[k][j])==1: 
                        #print(mat[k][j])
                        el.pop(el.index(mat[k][j]))
                for k in range(c):
                    #keep the row constant and traverse through different columns
                    if (mat[i][k] in el) and len(mat[k][j])==1:
                        #print(mat[i][k])
                        el.pop(el.index(mat[i][k]))
                ress=box(mat,i,j,el,boxcheck)
                if(len(ress)==1):
                    mat[i][j]="".join(ress)+"z"
                else:
                    mat[i][j]="".join(ress)
        


#Rows and Coloumns
r=9
c=9
#Read input
#EASY LEVEL
#s=""
s="..1..2..4..75.96..4..83..5794...7.32...396..5.73.8.1..734......8..7..429.924.53.."
#s=".94.3.1..8127...963..19.....3.9.46....8613.49..62....14.35....85...2.7...6...8415"
#s="53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
#INTERMEDIATE LEVEL
#s=".2.6.8...58...97......4....37....5..6.......4..8....13....2......98...36...3.6.9."
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

Pele(mat,r,c)
for i in range(r):
    for j in range(c):
        if('z' in mat[i][j]):
            l=[x for x in mat[i][j]]
            l.pop(1)
            mat[i][j]=l[0]
            del_Eles(mat,i,j)

for i in range(r):
    for j in range(c):
        if(len(mat[i][j])==1):
            del_Eles(mat,i,j)

#app = ExampleApp()
#app.mainloop()

final={}
k="c0"
m=0
for i in range(9):
    for j in range(9):
        final[eval('k')]=mat[i][j]
        k="c"+str(m+1)
        m+=1



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html',c0=final['c0'],c1=final['c1'],c2=final['c2'],c3=final['c3'],c4=final['c4'],c5=final['c5'],c6=final['c6'],c7=final['c7'],c8=final['c8'],c9=final['c9'],c10=final['c10'],c11=final['c11'],c12=final['c12'],c13=final['c13'],c14=final['c14'],c15=final['c15'],c16=final['c16'],c17=final['c17'],c18=final['c18'],c19=final['c19'],c20=final['c20'],c21=final['c21'],c22=final['c22'],c23=final['c23'],c24=final['c24'],c25=final['c25'],c26=final['c26'],c27=final['c27'],c28=final['c28'],c29=final['c29'],c30=final['c30'],c31=final['c31'],c32=final['c32'],c33=final['c33'],c34=final['c34'],c35=final['c35'],c36=final['c36'],c37=final['c37'],c38=final['c38'],c39=final['c39'],c40=final['c40'],c41=final['c41'],c42=final['c42'],c43=final['c43'],c44=final['c44'],c45=final['c45'],c46=final['c46'],c47=final['c47'],c48=final['c48'],c49=final['c49'],c50=final['c50'],c51=final['c51'],c52=final['c52'],c53=final['c53'],c54=final['c54'],c55=final['c55'],c56=final['c56'],c57=final['c57'],c58=final['c58'],c59=final['c59'],c60=final['c60'],c61=final['c61'],c62=final['c62'],c63=final['c63'],c64=final['c64'],c65=final['c65'],c66=final['c66'],c67=final['c67'],c68=final['c68'],c69=final['c69'],c70=final['c70'],c71=final['c71'],c72=final['c72'],c73=final['c73'],c74=final['c74'],c75=final['c75'],c76=final['c76'],c77=final['c77'],c78=final['c78'],c79=final['c79'],c80=final['c80'])

if __name__ == "__main__":
    app.run(debug=True)

