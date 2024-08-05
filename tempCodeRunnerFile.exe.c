#include <stdio.h> 
int main() { 
double a[3]={20.0, 25.0,30.0}, *p, *q; 
p = a; 
q = p + 2; 
printf("%d,%d", (int)(q - p), (int)(*q - *p)); 
return 0;}