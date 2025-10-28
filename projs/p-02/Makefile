LIB_N = printf
LIB_L = libft_printf
CC = cc 
LIB_I = libft_printf
all:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out
	./exec.out

lbsd:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -lbsd -o exec.out
	./exec.out
gdb:
	@$(CC) main.c -I ${LIB_I} -L ${LIB_L} -l${LIB_N} -o exec.out -g
	gdb ./exec.out