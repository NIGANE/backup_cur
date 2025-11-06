/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 13:19:02 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/06 13:20:13 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <stddef.h>
# include <stdint.h>
# include <stdlib.h>
# include <unistd.h>

void	ft_hexabase(unsigned long int nb, char *hex, int *count);
size_t	ft_strlen(char *s);
int		ft_putstr(char *s);
void	*ft_calloc(size_t nmemb, size_t size);
int		ft_putchar(char c);
void	ft_putnbr(long long n, int *count);
int		ft_printf(const char *format, ...);
char	*ft_strchr(const char *s, int c);
int		char_count(char *s, char a);

#endif
