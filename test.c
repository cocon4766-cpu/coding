#include<stdio.h>
 int main()
{
    char operator='\0';
    float num1=0.0;
    float num2=0.0;
    float result=0.0;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two numbers: ");
    scanf(" %f %f", &num1, &num2);

    switch(operator)
    {
        case '+':
            result = num1 + num2;
            break;

        case '-':
            result = num1 - num2;
            break;

        case '*':
            result = num1 * num2;
            break;

        case '/':
            if(num2 != 0)
            {
                result = num1 / num2;
            }
            else
            {
                printf("Error: Division by zero is not allowed.\n");
            }
            break;

        default:
            printf("Error: Invalid operator.\n");
    }
    return 0;
}
