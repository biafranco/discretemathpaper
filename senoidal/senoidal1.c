#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int calculateRecurrence(int reps) {
    if (reps == 1) {
        return 12;
    } else {
        return ((6 * calculateRecurrence(reps - 1)) + 6);
    }
}

int main() {
    FILE* file;
    int reps = 6;
    char rule[] = "F-F++FF--F+F";
    char current[calculateRecurrence(reps) + 1];
    char result[calculateRecurrence(reps) + 1];
    current[0] = 'F';

    file = fopen("senoidal.txt", "w+t");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    memset(result, '\0', sizeof(result));

    for (int i = 1; i <= reps; i++) {
        fprintf(file, "%d: ", i);
        for (size_t j = 0; j < strlen(current); j++) {
            if(current[j] == 'F')  {
                strcat(result, rule);
                fprintf(file, "%s", rule);
            }  else  {
                char c[2] = {current[j], '\0'};
                strcat(result, c);
                fprintf(file, "%s", c);
                }
        }

        memset(current, '\0', sizeof(current));
        strcpy(current, result);
        memset(result, '\0', sizeof(result));
        fprintf(file, "\n");

    }

    fclose(file);
    return 0;
}