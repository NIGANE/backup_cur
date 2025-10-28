LIB = libprintf.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f
INCLUDES = .

SRC =	ft_calloc.c \
		ft_printf.c \
		ft_putchar.c \
		ft_putstr.c \
		ft_putnbr.c \
		ft_hexabase.c \
		ft_printf.c \
		ft_strlen.c

OBJ = $(SRC:.c=.o)

all: $(LIB)

${LIB}: ${OBJ}
	${AR} ${LIB} ${OBJ} 
	$(MAKE) clean

%.o: %.c 
	$(CC) $(CFLAGS) -I ${INCLUDES} -c $< -o $@


clean:
	$(RM) $(OBJ)

fclean: clean
	$(RM) $(LIB)

re: fclean all

.PHONY: all clean fclean re bonus
.SECONDARY: ${OBJ}