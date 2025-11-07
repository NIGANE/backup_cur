#include "get_next_line.h"

int main(void)
{
    int fd = open("../file_test.txt", O_RDONLY);
    if (fd == -1)
    {
        printf("err while opning file from main func.");
        return 0;
    }
    char *s = get_next_line(fd);
    printf("line: %s", s);
    free(s);

    s = get_next_line(fd);
    printf("line: %s", s);
    free(s);

    s = get_next_line(fd);
    printf("line: %s", s);
    free(s);

    s = get_next_line(fd);
    printf("line: %s", s);
    free(s);
    // s = get_next_line(fd);
    // while (s)
    // {
    //     printf("%s", s);
    //     free(s);
    //     s = get_next_line(fd);

    // }
    close(fd);

}