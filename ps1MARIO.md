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
 for (int r = 0; r < h; r++) // print a gap and then
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
      printf("\n");
}
}

------------------------------------------------pseudocode.txt--------------------------------------------

Ask user to input a number of blocks they want mario to jump up on H = x
User puts 1 - 8
if number is less than 1 or greater than 8 reprompt user
loop 1 through user input (height)
    print a #(block) on each iteration

```
