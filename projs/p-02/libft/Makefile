LIB = libft.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f
INCLUDES = .

SRC =	ft_isalpha.c ft_isdigit.c ft_isalnum.c ft_isascii.c ft_isprint.c ft_toupper.c ft_tolower.c ft_strlen.c ft_strchr.c ft_strrchr.c ft_strncmp.c ft_strlcpy.c ft_strlcat.c \
		ft_strnstr.c  ft_strdup.c  ft_memset.c  ft_bzero.c  ft_memcpy.c  ft_memmove.c  ft_memchr.c  ft_memcmp.c  ft_calloc.c  ft_atoi.c  ft_itoa.c \
		ft_substr.c  ft_strjoin.c  ft_strtrim.c  ft_split.c  ft_strmapi.c  ft_striteri.c  ft_putchar_fd.c  ft_putstr_fd.c  ft_putendl_fd.c  ft_putnbr_fd.c

SRC_B = ft_lstadd_back_bonus.c ft_lstadd_front_bonus.c ft_lstclear_bonus.c ft_lstdelone_bonus.c ft_lstiter_bonus.c ft_lstlast_bonus.c ft_lstmap_bonus.c ft_lstnew_bonus.c ft_lstsize_bonus.c

OBJ_B = $(SRC_B:.c=.o)
OBJ = $(SRC:.c=.o)

all: $(LIB)

${LIB}: ${OBJ}
	${AR} ${LIB} ${OBJ} 

%.o: %.c 
	$(CC) $(CFLAGS) -I ${INCLUDES} -c $< -o $@


clean:
	$(RM) $(OBJ) $(OBJ_B)

fclean: clean
	$(RM) $(LIB)

re: fclean all


bonus: ${OBJ_B}
	${AR} ${LIB} ${OBJ_B} 
	

.PHONY: all clean fclean re bonus
.SECONDARY: ${OBJ} ${OBJ_B}