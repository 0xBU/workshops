/******************************************
* 0night @ BU Jan 2016
******************************************/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* I take a char ptr and a num and print out as much data as you ask for from that ptr! */
void myprint(char* str, int num) {
    for (int i = 0; i < num; i++) {
        printf("%c", str[i]);
    }
    return;
}
        
int main(int argc, char*  argv[], char* envp[]) {
    int first_int = 0xdeadbeef;
    int second_int = 0xc001c0de;
    
    char * first_str = "Hello world!";
    
    printf("%s\n", first_str);
    
    myprint(first_str, atoi(argv[1]));

    return 0;
}
