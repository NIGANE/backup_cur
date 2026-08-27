NAME		= codexion
CC			= cc
CFLAGS		= -Wall -Wextra -Werror -pthread
SRCS = burn_out_protocol.c clean.c coder_actions.c fifo.c heap2.c heap.c helpers.c \
		init.c main.c parsing.c resources_management.c schedular_management.c \
		simulation.c time.c
OBJS		= $(SRCS:.c=.o)

ARGS = 1 3000 200 200 200 10 800 fifo
#	nb_coders  burn_out  compile_t  debug_t  refactor_t  req_compiles  cooldown  schedular

valgrind = valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS)

%.o: %.c header.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJS)

fclean: clean
	rm -rf $(NAME)
test:
	./$(NAME) $(ARGS)
leak_test:
	$(valgrind) ./$(NAME) $(ARGS)

re: fclean all

.PHONY: all clean fclean re

.SECONDARY: $(OBJS)
