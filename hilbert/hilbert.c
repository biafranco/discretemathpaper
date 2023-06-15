#include <stdio.h>
#include <string.h>

int calculateRecurrence(int reps) {
    if (reps == 1) {
        return 11;
    } else {
        return ((4 * calculateRecurrence(reps - 1)) + 7);
    }
}

int main() {
    FILE* file;
    int reps = 6;
    char ruleX[] = "-YF+XFX+FY-";
    char ruleY[] = "+XF-YFY-FX+";

    char current[calculateRecurrence(reps)+1];
    char result[calculateRecurrence(reps)+1];
    current[0] = 'X';    
    char filter[100000];

    file = fopen("hilbert.txt", "w+t");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    memset(result, '\0', sizeof(result));

    for (int i = 1; i <= reps; i++) {
            fprintf(file, "%d: ", i);
            for (int j = 0; j < strlen(current); j++) {         
            if (current[j] == 'X') {
                strcat(result, ruleX);
                fprintf(file, "%s", ruleX);
            } else if (current[j] == 'Y') {
                strcat(result, ruleY);
                fprintf(file, "%s", ruleY);
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
            if (current[i] == 'X' || current[i] == 'Y')
            continue;
            char c[2] = {current[i], '\0'};
            strcat(filter, c);
            }
        fprintf(file, "Filter: %s\n\n", filter);
    }

    fclose(file);
    return 0;
}