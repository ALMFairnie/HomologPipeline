import sys #brining in the sys function

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "python " + sys.argv[0] + " GenomeCDS oufile.fa" + " genename"
		sys.exit(0)

 
f = sys.argv[1] #take in at argument space 1 whatever has been typed. Make this a variable named f 
file  = open(f, "r")  #open the f and make it something readable 

g = sys.argv[2]
out= open(g, "w") #w means to write not to read (there is also append "a")  


h = sys.argv[3]


 
count = 0 
bHLH = "false"


for line in file: #x is everysingle line in the file. 
	line = line.rstrip('\n')
	if line[0] == ">":
		bHLH = "false" 
		if h in line:
			bHLH = "true"
			count += 1
	if bHLH == "true":
		out.write(line+"\n") 
		
		
		
print "count of seqs is: " + str(count)

'''
for line in file: 
	line = line.rstrip('\n')
	if line[0] == ">":
		if "bHLH" in line:
			count += 1
			print line 
			'''
			
			
