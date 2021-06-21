#include <stdio.h>

int age;

int main(){

 printf("How old are you?");
 scanf("%d", &age);

    if(age >= 18){

        printf("You can buy a ticket.");

    }
    else
    {

        printf("You have not the age to buy a ticket :/");

    }

return 0;

}