```
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string s);
char rotate(char c, int k);

int k, flag = 0;

int main(int argc, string argv[])
{

// only take in 2 arguments
    if (argc != 2)
    {
      printf("Usage: ./caesar key--line20\n");
     return 1;
    }

else if (only_digits(argv[1]))

{
k = atoi(argv[1]);
flag = 1;
}
else
{
    printf("Usage: ./caesar\n");
    return 1;
}

if (flag == 1)
{
    string input = get_string("plaintext: ");

//covert to ciphertext
printf("ciphertext: ");

for (int i =0; i <=strlen(input); i++)
{
    printf("%c", rotate(input[i], k));
}
printf("\n");
}


bool only_digits(string s)
{
int flag2 = 0;
for (int i = 0; i < strlen(s); i++)
    {
        if (!isdigit(s[i]))
        {
         flag2 =1;
        }
        {
            if(flag2 == 1)
            {
                return false;
            }
            else
            {
                return true;
}
}
}


char rotate(char c, int key)
{
    char cout;
        if(isupper(c))
            {
                cout = (c + key - 65) % 26 + 65;
            }
    else if(islower(c))
            {
                cout = (c + key - 97) % 26 + 97;
            }
    else
            {
                cout = c;
            }
    return cout;
}



/*
            printf("%s", argv[1]);
            //return false;
        }
    }
}
}


// key
char *key = (argv[1]);
int size = strlen(key);

for (int = 0; i < size; i++)
{
    if(isdigit(k[i]) == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

int kn = (argv[1]);


int isize = strlen(input);


bool only_digits(key) == 1)
{
    printf("key: %s\n", argv[1]);
    return 0;
}
else
{
    printf("Usage: ./caesar key\n");
    return 1;
}

bool only_digits(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    return true;
    }
}
}

    if(argv[1] == false)
    {
        printf("Usage: ./caesar key--line22\n");
        return 1;
    }
    else
    {
    return 0;
    }*/
```
