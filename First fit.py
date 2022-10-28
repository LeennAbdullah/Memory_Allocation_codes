#First Fit algorithm 
J=int(input("Please enter the number of Jobs: ")) #input the number of Jobs 
H=int(input("Please enter the number of holes: ")) #input the number of Holes
jobs=list() #empty list for the size of the jobs 
Holes=list() #empty list for the capacity of the holes
print("Please  enter the size of each Job: ") #to input the size of each job and store it inside jobs list 
for i in range(J):
    print("Job %d: "%(i+1))
    jobs.append(int(input()))
print("Please  enter the size of each Hole: ") #to input the capacity of each hole and store it inside Holes list 
for i in range(H):
    print("Hole %d: "%(i+1))
    Holes.append(int(input()))
##############################################################
ANS=list() #to store the jobs 
space=list(Holes) #Because Holes will be modified
JJ=list(jobs)  #Because jobs will be modified
index=0 #To continue from the holes without reapeating them 
for i in range(H): 
    c=""
    if(len(jobs)>0):
        while(jobs[0]<=Holes[i]):
                val=Holes[i]-jobs[0]
                Holes.pop(i)
                Holes.insert(i, val)
                jobs.pop(0)
                c+="Job"+str(index+1)+" "
                index+=1
                if(index==J):
                    break
    ANS.insert(index,c)
print(ANS)
##############################################################
print("Welcome to the First fit code:)")
print("Here is the informations: ")
for i in range(J):
    print("Job %d size is %d"%(i+1,JJ[i]))
for i in range(H):
    print("Hole %d capacity is %d"%(i+1,space[i]))
##############################################################
print("This is How the memory looks like Before allocating: ")
print("--------")
for i in range(H):
    print("|%dk  "%(space[i]))
    print("--------")
##############################################################3
print("This is How the memory looks like After allocating: ")
print("--------")
for i in range(len(Holes)):
    if(ANS[i]==""):
        print("|%dk No Jobs allocated "%(Holes[i]))
    else:
        print("|%dk %s"%(Holes[i],ANS[i]))
    print("--------")