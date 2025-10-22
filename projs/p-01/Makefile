LIB_N = ft
LIB_L = libft
CC = cc -Wall -Wextra -Werror
LIB_I = libft
all:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out
	./exec.out

lbsd:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -lbsd -o exec.out
	./exec.out
