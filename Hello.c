# include<stdio.h>
#include<string.h>
int main()
{
    char item[20]= " ";
    float price= 0.0f;
    int quantity= 0;

    printf("Enter the item name: ");
    fgets(item, sizeof(item), stdin);
    item[strcspn(item, "\n")] = '\0';  // Remove newline character from item name

    printf("Enter the price of the item: ");
    scanf(" %f", &price);

    printf("Enter the quantity of the item: ");
    scanf(" %d", &quantity);

    float total_price = price * quantity;

    printf("\nyou have bought %d %s at a price of %.2f each.\n", quantity, item, price);
    printf("your Total price is: $%.2f\n", total_price);

    return 0;
}