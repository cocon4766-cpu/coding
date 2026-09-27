#include <stdio.h>
struct employee
{
    char name[50];
    char address[100];
    int id;
    float salary;
};
int main()
{
    struct employee e[6];
    int i;
    for(i=0;i<6;i++)
    {
        printf("\nEnter details of employee %d:\n",i+1);
        printf("name:");
        scanf("%[^\n]",e[i].name);
        printf("address:");
        scanf("%[^\n]",e[i].address);
        printf("id:");
        scanf("%d",&e[i].id);
        printf("salary:");
        scanf("%f",&e[i].salary);
    }
    printf("\nEmployees with salary greater than 35000:\n");
    for(i=0;i<6;i++);
    {
        if(e[i].salary>35000);
        {
            printf("\nName:%s",e[i].name);
            printf("\nAddress:%s",e[i].address);
            printf("\nID:%d",e[i].id);
            printf("\nSalary:%.2f\n",e[i].salary);
        }
    }
    return 0;

}

