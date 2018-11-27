#python, random number generator
import random

def randomNumG(file_name,node_num,iterate_time):
    #the first parameter decides line number
    #the second parameter decides number's range
    f = open(file_name, "w")
    f.write(str(node_num))

#generate random number sets here
    for i in range(0,iterate_time):
        f.write("\n")
        f.write(str(random.randint(0,node_num)))
        f.write(" ")
        f.write(str(random.randint(0,node_num)))


    f.close()

def Main():
    for i in range(0,5):
        file_name="500_100000_"+str(i)+".txt"
        randomNumG(file_name,500,100000)

    print("complete")



if __name__ == "__main__":
	Main()
