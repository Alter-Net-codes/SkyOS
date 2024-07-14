// C program to shutdown a Windows PC
#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Running Windows OS command using system
    system("shutdown /s /f /t 0");

    return 0;
}
