LIB = libftprintf.a
SRCS = src/ft_calloc.c \
	   src/ft_printf.c \
	   src/ft_putchar.c \
	   src/ft_putstr.c \
	   src/ft_strchr.c \
	   src/ft_putnbr.c \
	   src/ft_hexabase.c \
	   src/ft_strlen.c \
	   src/char_count.c

OBJS = $(SRCS:.c=.o)
CC = gcc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f
INCLUDES = include/libftprintf.h

all: $(LIB)

$(LIB): $(OBJS)
	$(AR) $(LIB) $(OBJS)

%.o: %.c $(INCLUDES)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(LIB)

re: fclean all

.PHONY: all clean fclean re
.SECCONDARY: $(OBJS) ${SRCS}