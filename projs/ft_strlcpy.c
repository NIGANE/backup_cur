#include <stdio.h>
#include <string.h>
#include <stddef.h>

size_t	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	src_len;

	src_len = 0;
	while (src[src_len])
		src_len++;
	if (dstsize <= 0)
		return (src_len);
	dstsize -= 1;
	while (dstsize-- > 0)
		*dst++ = *src++;
	*dst = '\0';
	return (src_len);
}

int	main(void)
{
    char dest[20];
    char src[] = "Hello, World!";
    size_t result;
    result = ft_strlcpy(dest, src, sizeof(dest));
    printf("Copied string: %s\n", dest);
    printf("Length of source: %zu\n", result);
    return 0;
}
