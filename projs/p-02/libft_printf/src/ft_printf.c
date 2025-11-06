/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 15:42:21 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/05 16:49:17 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/ft_printf.h"

static void	print_pointer(unsigned long n, int *count, char *hex)
{
	if (n == 0)
		*count += ft_putstr("(nil)");
	else
	{
		*count += ft_putstr("0x");
		ft_hexabase(n, hex, count);
	}
}

static void	print_hexa(unsigned long n, int *count, char *hex)
{
	if (n == 0)
		*count += ft_putchar('0');
	else
		ft_hexabase(n, hex, count);
}

static void	check(const char *s, va_list args, int *cnt)
{
	if (*(s + 1) == '%')
		*cnt += ft_putchar('%');
	else if (*(s + 1) == 's')
		*cnt += ft_putstr(va_arg(args, char *));
	else if (*(s + 1) == 'c')
		*cnt += ft_putchar(va_arg(args, unsigned int));
	else if (*(s + 1) == 'd' || *(s + 1) == 'i')
		ft_putnbr(va_arg(args, int), cnt);
	else if (*(s + 1) == 'u')
		ft_putnbr(va_arg(args, unsigned int), cnt);
	else if (*(s + 1) == 'x')
		print_hexa((unsigned int)va_arg(args, unsigned int), cnt,
			"0123456789abcdef");
	else if (*(s + 1) == 'X')
		print_hexa((unsigned int)va_arg(args, unsigned int), cnt,
			"0123456789ABCDEF");
	else if (*(s + 1) == 'p')
		print_pointer((unsigned long int)va_arg(args, void *), cnt,
			"0123456789abcdef");
}

int	ft_printf(const char *s, ...)
{
	int		count;
	va_list	args;
	int i;

	count = 0;
	i = 0;
	if (!s)
		return (-1);
	va_start(args, s);
	while (s[i])
	{
		if (s[i] == '%' && s[i + 1] && ft_strchr("cspdiuxX%", s[i + 1]))
		{
				check(s, args, &count);
				i++;
		}
		else if (s[i] == '%' && !s[i + 1] && char_count((char *)s, '%') == 1)
			return (-1);
		else
			count += ft_putchar(s[i]);
		i++;
	}
	va_end(args);
	return (count);
}
