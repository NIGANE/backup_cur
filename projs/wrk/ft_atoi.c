int	ft_atoi(char *s)
{
	int		sign;
	long	re;

	sign = 1;
	re = 0;
	if (!s)
		return (0);
	while (*s == ' ')
		s++;
	if (*s == '-' || *s == '+')
	{
		if (*s == '-')
			sign *= -1;
		s++;
	}
	while (*s >= '0' && *s <= '9')
	{
		re = re * 10 + (*s - '0');
		s++;
	}
	return (re * sign);
}
