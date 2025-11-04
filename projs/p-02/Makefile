LIB_N = ftprintf
LIB_L = libft_printf
CC = cc 
CFLAGS = -Wall -Wextra -Werror
LIB_I = libft_printf
all:
	@$(CC) ${CFLAGS} main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out
	./exec.out

lbsd:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -lbsd -o exec.out
	./exec.out
gdb:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out -g
	gdb ./exec.out

nfl:
	@cc main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out
	./exec.out
clean:
	rm -f exec.out