import sys #brining in the sys function

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print "python " + sys.argv[0] + " GenomeCDS blastfile outputfilename" 
		sys.exit(0)


f = sys.argv[1]
file  = open(f, "r")

g = sys.argv[2]
file2  = open(g, "r")

h = sys.argv[3]
file3 = open(h, "w")

list = []
list_of_all = []
HASH = {}
FastaHash = {}
seq = ""
GoAhead = "False"
name = ""
#Create a loop that makes a dictionary out of fastas

for line in file: 
	line = line.rstrip('\n')
	
	
	if line[0] == ">":
	
		if GoAhead == "True":
			FastaHash[name] = seq
		
		list = line.split(" ")
		name = list[0][1:]
		seq = ""
		
	else:
		seq = seq + line;
	
	
	
	GoAhead = "True"
	
FastaHash[name] = seq
#print FastaHash


for line in file2: 
	line = line.rstrip('\n')
	list = line.split("\t")
	#print list[2]
	HASH[list[0]] = list[2]
	HASH[list[2]] = list[0]
	
#print HASH
for x in HASH:

	print ">" + str(x) + "\n" + str(FastaHash[x]) 
	file3.write(">" + str(x) + "\n" + str(FastaHash[x]) + "\n" )
	
#	print FastaHash[WordOfInterest]
