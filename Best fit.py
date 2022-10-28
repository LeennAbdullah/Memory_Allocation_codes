#The Best fit 
#wich is the best algorithm used 
J=int(input("Please enter the number of jobs: ")) #input the number of Jobs
H=int(input("Please enter the number of Holes (Memory space): ")) #input the number of Holes 
Jobs=list() #created list for the size of jobs 
Holes=list() #created list for the capacity of the Holes
print("Please enter the size of each job: ") #Print the size of each job and store inside Jobs list 
for i in range(J):
    print("Job %d: "%(i+1))
    Jobs.append(int(input()))
print("Please enter the capacity of each hole: ") #Print the size of each hole and store inside Holes list 
for i in range(H):
    print("Hole %d: "%(i+1))
    Holes.append(int(input()))
##########################################################
s2=list(Holes)
s2.sort()
s1=list(Holes)
s1.sort()
Ans=list() #to allocate the jobs 
Size=list(Jobs) #because the job list will be converted to N 
for i in range(H):
    Ans.append("")

for i in range(J):
    flag=True
    for j in range(H):
        if(Jobs[i]==s2[j]):
            c=""
            c=Ans[j]
            Ans.pop(j)
            s2.pop(j)
            s2.insert(j, 0)
            c+="Job"+str(i+1)+" "
            Ans.insert(j, c)
            Jobs.pop(i)
            Jobs.insert(i,"N")
            flag=False
            break
    for k in range(H):
        if(flag):
            if(Jobs[i]<s2[k]):
                c=""
                c=Ans[k]
                Ans.pop(k) #to update the value 
                val=s2[k]-Jobs[i]
                s2.pop(k)
                s2.insert(k, val)
                c+="Job"+str(i+1)+" "
                Ans.insert(k, c)
                Jobs.pop(i)
                Jobs.insert(i,"N")
                break 
final=list()
A=list()
for i in range(H):
    ind=s1.index(Holes[i])
    A.insert(i, s2[ind])
    s2.pop(ind)
    s2.insert(ind, "N")
    s1.pop(ind)
    s1.insert(ind, "N")
    final.insert(i, Ans[ind])
#################################################
print("Welcome to the Best fit code :)")  
print("Here are the informations: ")
for i in range(J):
    print("Job %d with size = %d"%(i+1,Size[i]))
for i in range(H):
    print("Hole %d with size = %d"%(i+1,Holes[i]))
#################################################
print("This is how the memory looks Before allocating: ")
print("-------")
for i in range(H):
    print("|%dk"%(Holes[i]))
    print("-------------")
print("This is how the memory looks After allocating: ")
print("-------")
for i in range(H):
    if(final[i]==""):
         print("|%dk No jobs allocated"%(A[i]))
    else:
        print("|%dK  %s"%(A[i],final[i]))
    print("-------------")
for i in range(len(Jobs)):
    if(Jobs[i]=='N'):
        continue
    else:
        print("job ",i+1," was not allocated")
