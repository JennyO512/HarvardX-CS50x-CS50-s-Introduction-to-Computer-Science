```
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{

//accept exactly one command-line argument
 if (argc != 2)
{
//else print usage
printf("Usage: ./recover IMAGE\n");
return 1;
}
//open files
FILE *file = fopen(argv[1], "r");
if (file == NULL)
{
//else don't open
printf("Could not open.\n");
return 1;
}
//create array
unsigned char buffer[512];
//how many images
int count_image = 0;
//pointer for recovered images
FILE *output_file = NULL;
//char filename[0]
char *filename = malloc(8 * sizeof(char));
//read block of 512
while (fread(buffer, sizeof(char), 512, file))
{
if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
{
//create the jpeg filenames
sprintf(filename, "%03i.jpg", count_image);
//open output to write to
output_file = fopen(filename, "w");
//count images and update
count_image++;
}
if(output_file != NULL)
{
fwrite(buffer, sizeof(char), 512, output_file);
}
}
free(filename);
fclose(output_file);
fclose(file);
return 0;
}
```
