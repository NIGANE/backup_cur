#include <stddef.h>
#include <stdlib.h>

void	*ft_calloc(size_t nmumb, size_t size)
{
	unsigned char	*re;
	size_t			byt;
	unsigned char	*buf;

	if (nmumb <= 0 || size <= 0)
		return (malloc(0));
	byt = nmumb * size;
	re = malloc(byt);
	if (!re)
		return (NULL);
	buf = re;
	while (byt-- > 0)
		*buf++ = 0;
	return (re);
}
