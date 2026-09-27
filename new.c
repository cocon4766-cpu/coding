#include<stdio.h>
#include<string.h>

void poem(char*name, char* name1)
{
    printf("roses are red, violets are blue,\n");
    printf("%s met %s, and suddenly skies turned blue.\n",name ,name1);
    printf("roses may fade, but my feelings stay true,\n");
    printf("if love hade a name, it would be you two.\n");
}
int main()
{
    char name[50];
    char name1[50];

    printf("Enter your name: ");
    fgets(name, sizeof(name),stdin);
    name[strlen(name) -1]='\0';

    printf("Enter your name1: ");
    fgets(name1, sizeof(name1), stdin);
    name1[strlen(name1) - 1] = '\0'; // Remove the newline character

    poem(name,name1);

    return 0;
}