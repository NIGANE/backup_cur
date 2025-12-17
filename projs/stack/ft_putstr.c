#include "../includes/sta1.h"

int	ft_putstr(char *s)
{
	if (s == NULL)
		return ((int)write(1, "(null)", 6));
	return ((int)write(1, s, ft_strlen(s)));
}