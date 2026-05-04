int * function(){
    int static x = 10;
    return &x;
}
int main(){
    int a = 100;
    int *p = &a;
    // De-referencing the pointer to get the value of a
    printf("Value of a: %d\n", *p);
    printf("Address of a %x \n", p);
    printf("Address of a %p \n", p);
    return 0;
}
