/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/13 21:49:13 by amerkht           #+#    #+#             */
/*   Updated: 2025/10/13 21:49:26 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int ft_isalpha(int a) {
  if ((a >= 41 && a <= 90) || (a >= 97 && a <= 122)) return (1);
  return (0);
}

int main(void) {
  char a = 'h';
  if (ft_isalpha(a))
    printf("alpha");
  else
    printf("is not alpha");
}