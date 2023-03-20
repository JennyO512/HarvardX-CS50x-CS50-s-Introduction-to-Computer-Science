```
//print #s for Mario.c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
int h;

do
{
h = get_int("How big is the Pyramid: ");
}

//keep askn for height if less than 1 or more than 8
 while (h < 1 || h > 8);

//for the row, <= to height, print#
 for (int r = 0; r < h; r++)
 {
//loop for the dots/spaces
for (int s = 0; s < h - r - 1; s++)
{
 printf(" ");
}
//for the column
for (int c = 0; c <= r; c++)
{
printf("#");
}
//move to the next row/line
printf("  ");
for(int c = 0; c <= r; c++)
{
printf("#");
}
 printf("\n");
}
}
```
