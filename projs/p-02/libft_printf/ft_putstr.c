#include "ft_printf.h"
#include <stddef.h>


int	ft_putstr(char *s)
{
	if (!s)
		return (0);
	return ((int)write(1, s, ft_strlen(s)));
}