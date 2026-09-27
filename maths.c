#include<stdio.h>
#include<math.h>
int main()
{
    
    double principle= 0.0;
    double rate= 0.0;
    int years= 0;
    int timescompounded= 0;
    double totalamount= 0.0;

    printf("Enter the principal amount: ");
    scanf(" %lf", &principle);

    printf("Enter the annual interest rate (in decimal): ");
    scanf(" %lf", &rate);
    rate= rate/100;

    printf("Enter the number of years: ");
    scanf(" %d", &years);

    printf("Enter the number of times interest is compounded per year: ");
    scanf(" %d", &timescompounded);

    totalamount= principle * pow(1 + (rate / timescompounded), timescompounded * years);

    printf("after %d years, the total amount will be: %.2lf$ \n", years, totalamount);

    return 0;
}

