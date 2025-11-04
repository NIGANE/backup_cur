#ifndef PRINTF_H
#define PRINTF_H

#include <unistd.h>
#include <stdarg.h>
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>


void ft_hexabase(unsigned long int nb, char *hex, int *count);
size_t    ft_strlen(char *s);
int    ft_putstr(char *s);
void	*ft_calloc(size_t nmemb, size_t size);
int	ft_putchar(char c);
void	ft_putnbr(long long n, int *count);
int	ft_printf(const char *format, ...);
char	*ft_strchr(const char *s, int c);

#endif
