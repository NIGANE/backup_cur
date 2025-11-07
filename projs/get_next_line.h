
# ifndef GET_NEXT_LINE_H
#define GET_NEXT_LINE_H

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <fcntl.h>
#include <unistd.h>

# ifndef BUFFER_SIZE
#define BUFFER_SIZE 42
#endif

size_t	ft_strlen(char *s);
int		ft_strchr(char *s, int c);
char	*ft_strdup(const char *s);
char	*ft_strjoin(char *s, char *b);
char    *get_next_line(int fd);


#endif