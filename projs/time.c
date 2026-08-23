#include "header.h"

long long	current_time_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return ((long long)tv.tv_sec * 1000 + tv.tv_usec / 1000);
}

long long	timestamp(long long start)
{
	if (!start)
		return (0);
	return (current_time_ms() - start);
}

void	suspend(long s)
{
	usleep(s * 1000);
}
