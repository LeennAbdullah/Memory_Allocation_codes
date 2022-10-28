#The Worst Fit 
#DONEE
J=int(input("Please enter the number of jobs: ")) #input the number of jobs
Jobs=list() #created an empty list to store the size of jobs 
H=int(input("Please enter the number of Holes(Memory space): ")) #input the number of holes
Holes=list() #created an empty list for the memory space
print("Please enter the size of each Job: ") #printing the size of each job and store it inside Jobs list 
for i in range(J):
    print("The size of job %d: "%(i+1))
    Jobs.append(int(input()))
print("Please enter the size of each Hole: ") #printing the size of each hole and store it inside Holes list 
for i in range(H):
    print("The size of Hole %d: "%(i+1))
    Holes.append(int(input()))
Ans=list() #created and empty list to save the jobs 
Space=list(Holes) #To print the before and After  
for i in range(H): #To fill the list with empty string 
    Ans.append("")
for i in range(J):
    Max=max(Holes) #to get the max value 
    ind=Holes.index(Max) #to get the index of the max value 
    if(Jobs[i]<=Max):  
        c=""
        c=Ans[ind]
        Ans.pop(ind)
        val=Holes[ind]-Jobs[i]
        Holes.pop(ind)
        Holes.insert(ind, val)
        c+="Job"+str(i+1)+" "
        Ans.insert(ind, c)
#################################################   
print("Welcome to the Worst fit code :)")  
print("Here are the informations: ")
for i in range(J):
    print("Job %d with size = %d"%(i+1,Jobs[i]))
for i in range(H):
    print("Hole %d with size = %d"%(i+1,Space[i]))
#################################################
print("This is how the memory looks Before allocating: ")
print("-------")
for i in range(H):
    print("|%dk"%(Space[i]))
    print("-------------")
print("This is how the memory looks After allocating: ")
print("-------")
for i in range(H):
    if(Ans[i]==""):
         print("|%dk No jobs allocated"%(Holes[i]))
    else:
        print("|%dK  %s"%(Holes[i],Ans[i]))
    print("-------------")