#include <stdio.h>
#include <string.h>

int calculateRecurrence(int reps) {
    if (reps == 1) {
        return 21;
    } else {
        return ((7 * calculateRecurrence(reps - 1)) + 14);
    }
}

int main() {
    FILE* file;
    int reps = 6;
    char ruleA[] = "A+BF++BF-FA--FAFA-BF+";
    char ruleB[] = "-FA+BFBF++BF+FA--FA-B";
    
    char current[calculateRecurrence(reps)+1];
    char result[calculateRecurrence(reps)+1];
    char filter[100000];


    current[0] = 'A';
    
    file = fopen("gosper.txt", "w+t");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    memset(result, '\0', sizeof(result));

    for (int i = 1; i <= reps; i++) {
            fprintf(file, "%d: ", i);
            for (int j = 0; j < strlen(current); j++) {
            if (current[j] == 'A') {
                strcat(result, ruleA);
                fprintf(file, "%s", ruleA);
            } else if (current[j] == 'B') {
                strcat(result, ruleB);
                fprintf(file, "%s", ruleB);
            } else {
                char c[2] = {current[j], '\0'};
                strcat(result, c);
                fprintf(file, "%s", c);
            }
        }

        fprintf(file, "\n\n");  
        memset(current, '\0', sizeof(current));

        strcpy(current, result);
        memset(result, '\0', sizeof(result));

        
        memset(filter, '\0', sizeof(filter));
        for (int i = 0; i < strlen(current); i++) {
            if (current[i] == 'A' || current[i] == 'B')
            continue;
            char c[2] = {current[i], '\0'};
            strcat(filter, c);
            }
        fprintf(file, "Filter: %s\n\n", filter);
    }

    fclose(file);
    return 0;
}