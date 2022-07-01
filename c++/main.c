#include <stdio.h>
#include <math.h>

void main()
{
    int firstNumber, secondNumber;
    char operation;
    while(1)
    {
    printf("Enter operation:\n");
    scanf("%c", &operation);
    
    switch(operation)
    {
    case '+' :
        printf("Введите первое число:\n");
        scanf("%d", &firstNumber);
        printf("Введите второе число:\n");
        scanf("%d",&secondNumber);
        printf("Result: ");
        printf("%d", firstNumber + secondNumber);
        printf("\n");
        break;
    case '-' :
        printf("Введите первое число:\n");
        scanf("%d", &firstNumber);
        printf("Введите второе число:\n");
        scanf("%d",&secondNumber);
        printf("Result: ");
        printf("%d", firstNumber - secondNumber);
        printf("\n");
        break;
    case '*' :
        printf("Введите первое число:\n");
        scanf("%d", &firstNumber);
        printf("Введите второе число:\n");
        scanf("%d",&secondNumber);
        printf("Result: ");
        printf("%d", firstNumber * secondNumber);
        printf("\n");
        break;
    case '/' :
        printf("Введите первое число:\n");
        scanf("%d", &firstNumber);
        printf("Введите второе число:\n");
        scanf("%d", &secondNumber);
        printf("Result: ");
        printf("%d", firstNumber / secondNumber);
        printf("\n");
        break;
    case '_':
        printf("%s", "Введите число:\n");
        scanf("%d", &firstNumber);
        printf("Результат: ");
        printf("%f", sqrt(firstNumber));
        printf("\n");
        break;
    default:
        printf("err");
    }
    getchar();
    }
}