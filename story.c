#include<stdio.h>
#include<math.h>
int main()
{
    float a= 0.0f;
    float b= 0.0f;

    printf("Enter the value of a: ");
    scanf(" %f", &a);

    printf("Enter the value of b: ");
    scanf(" %f", &b);

    printf("the sum of (square root of a) and (power of b) is: %.2f\n", sqrt(a) + pow(b, 3));
    printf("the log of (square root of a) and (power of b) is: %.2f\n", log(sqrt(a) + pow(b, 3)));
    printf("the sum of (cosine of a) and (sine of b) is: %.2f\n", cos(sqrt(a) + sin(b)));
    return 0;
}