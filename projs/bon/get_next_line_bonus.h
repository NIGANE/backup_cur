/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.h                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amerkht <amerkht@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 15:53:02 by amerkht           #+#    #+#             */
/*   Updated: 2025/11/15 11:15:40 by amerkht          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_BONUS_H
# define GET_NEXT_LINE_BONUS_H

# include <fcntl.h>
# include <stddef.h>
# include <stdint.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 1000000
# endif
#  define MAX_FD 60556

size_t	ft_strlen(char *s);
int		ft_strchr(char *s, int c);
char	*extract_line(const char *s);
char	*ft_strjoin(char *s, char *b);
char	*get_next_line(int fd);

#endif