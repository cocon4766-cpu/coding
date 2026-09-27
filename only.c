#include <stdio.h>

int Addnumbers(int number1, int number2)
{
    return number1 + number2;
}

int main(void)
{
    int sum = Addnumbers(6, 7);
    printf("result = %d\n", sum);

    return 0;
}