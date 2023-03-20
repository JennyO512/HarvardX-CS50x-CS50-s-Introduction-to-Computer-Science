```
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>


int main(void)
{
    string s = get_string("Text Here: ");//prompt user for text
    int l = 0; //letters
    int w = 1; //words
    int sent = 0; //sentences

int count_letters(string text);
   // TODO: count and return letters for string
  //int l = 0;
  for(int i = 0; i < strlen(s); i++)
  {
      if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
      {
      l++;
      }
  }
  //printf("%i letters\n", l);



  /*  while (s[l] != '\0')
    {
        l++;
    }
    printf("%i letters \n", l);*/

int count_words(string text);
//how many words are there
    for(int i = 1; i < strlen(s); i++)
    {
        if(s[i] == ' ')
        {
        w++;
        }
    }
//printf("%i words\n", w);

int count_sentences(string text);
//how many sentences
for (int i = 0; i < strlen(s); i++)
{
    if (s[i] == '.' || s[i] == '?' || s[i] == '!')
    {
    sent++;
    }
}
//printf("%i sentences\n", sent);

//calculate using the coleman formula - dam floats!!
float L = (float) l / (float) w * 100;
float S = (float) sent / (float) w * 100;

int index = round(0.0588 * L - 0.296 * S - 15.8);

 if (index < 1)
 {
    printf("Before Grade 1\n");
 }
    else if (index >=16)
{
 printf("Grade 16+\n");
}
 else
  {
    printf("Grade %i\n", index);
  }
}
```
