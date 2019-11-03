import random,string, os



firstBlock = """#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> 

void printFlag() {printf("flag:"""

middleBlock = """\\n");
}


int main(int argc, char *argv[]) 
{ 
    char buffer[8];  
    if (argc < 2) 
    { 
        printf("strcpy() NOT executed....\\n"); 
        printf("Syntax: %s <characters>\\n", argv[0]); 
        exit(0); 
    } 
    memset(buffer, '\\0', sizeof(buffer));
    strncpy(buffer, argv[1], 7); 
    """

endBlock = """
    printf("buffer content= %s\\n", buffer); 
    if(0){
        printFlag();        
    } else {
        printf("YoU aRe A fAiLuRe\\n");
    }
    printf("strcpy() executed...\\n"); 

    return 0; 
}"""


def randomBlock() :
    return "".join(random.choices(string.ascii_letters+string.digits, k=4))
    
numFiles = 1337 
vuln = random.randint(0, numFiles)
for i in range(numFiles):
    if (vuln==i):
        buff = firstBlock+"0xBU"+middleBlock+"strcpy(buffer, argv[1]);"+endBlock 
    else:
        buff = firstBlock+randomBlock()+middleBlock+endBlock
     # write it to a file
    f = open("vuln"+str(i)+".c","w")
    f.write(buff)
    f.close()
    os.system("gcc -fno-stack-protector -z execstack -g -o vuln" +str(i)+" vuln"+str(i)+".c")
os.system("rm vuln*.c")










