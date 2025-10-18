CC = cc -Wall -Werror -Wextra
AR = ar rcs
RM = rm -f
NAME = libft.a
SRCS = *.c
OBJS = $(SRCS:.c=.o)
INCLUDES = -I includes

all: $(NAME)
$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

${OBJS}: ${SRCS}
	${CC} -c ${SRCS}

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all