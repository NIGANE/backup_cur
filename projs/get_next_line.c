
#include "get_next_line.h"

static char *free_some(char *s)
{
    int size;
    char *bf;
    char *tp;

    if (!s)
        return (NULL);
    size = 0;
    while (s[size])
    {
        if (s[size++] == '\n')
            break;
    }
    bf = malloc(ft_strlen(s) - size + 1);
    if (!bf)
    {
        free(s);
        return (NULL);
    }
    tp = bf;
    while (s[size]) 
        *tp++ = s[size++];
    *tp = '\0';
    free(s);
    return (bf);
}

static char *nothing(char *s)
{
    if (s)
        free(s);
    return (NULL);
}

static char *get_line(char *s, int fd)
{
    int size;
    char *bf;
    char *tp;

    bf = malloc(BUFFER_SIZE + 1);
    if (!bf)
        return (NULL);
    size = 1;
    while (size >= 1 && !ft_strchr(s, '\n'))
    {
        size = read(fd, bf, BUFFER_SIZE);
        if (size == -1)
            return (nothing(bf));
        else if (size == 0)
            break ;
        bf[size] = '\0';
        tp = s;
        s = ft_strjoin(s, bf);
        if (!s)
            return (nothing(tp));
        free(tp);
    }
    free(bf);
    return (s);
}

char    *get_next_line(int fd)
{
    static char *temp;
    char *re;

    if (fd <= 2)
        return (NULL);
    
    temp = get_line(temp, fd);
    if (!temp)
        return (NULL);
    re = ft_strdup(temp);
    if (!re)
    {
        free(temp);
        return (NULL);
    }
    temp = free_some(temp);
    if (!temp)
    {
        free(re);
        return (NULL);
    }
    return (re);
}
