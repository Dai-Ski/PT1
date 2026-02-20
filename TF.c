#include<stdio.h>
#include<stdbool.h>
enum BOOLEAN{
True,False,X=10,Y,Z};

int main(){
bool status=true;
enum BOOLEAN f= X;
printf("%i\n",status);
printf("%i\n", f);

//Dont use %d for the  sizeof() function
printf("Size of enum BOOLEAN is %llu\n",sizeof(f));
printf("Size of enum is %zu\n",sizeof(f));
return 0;
}