/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   char_count.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 18:31:15 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/04 18:32:52 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include "../include/ft_printf.h"

int char_count(char *s, char a)
{
    int count;

    count = 0;
    if(!s)
        return (0);
    while (*s)
    {
        if (*s == a)
            count++;
        s++;
    }
    return (count);
}