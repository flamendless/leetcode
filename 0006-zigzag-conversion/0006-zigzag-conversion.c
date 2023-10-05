char* convert(char* s, int numRows)
{
    if (numRows <= 1)
        return s;
    
    char** array = malloc(numRows * sizeof(char*));
    
    int len = strlen(s)/(numRows - 1);
    for (int i = 0; i < numRows; i++)
    {
        array[i] = (char*)malloc(len + 2);
        strcpy(array[i], "");
    }
    
    int current_row = 0;
    int direction = 1;
    
    for (int i = 0; i < strlen(s); i++)
    {
        char ch = s[i];       
        int cur_len = strlen(array[current_row]);
        array[current_row][cur_len] = ch;
        array[current_row][cur_len + 1] = '\0';
        //printf("%i = %s\n", current_row, array[current_row]);
        
        if (direction == 1 && current_row >= numRows - 1)
            direction = -1;   
        else if (direction == -1 && current_row <= 0)
            direction = 1;
        current_row += 1 * direction;
    }
    
    char* res = malloc((strlen(s) + 1) * sizeof(char));
    strcpy(res, array[0]);
    for (int i = 1; i < numRows; i++)
        strcat(res, array[i]);
    
    return res;
}