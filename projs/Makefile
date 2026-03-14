CC = cc -Wall -Wextra -Werror
OUT = tt
SRC = main.c ./heap/*.c
run:
	@$(CC) $(SRC) -o $(OUT)
	@./$(OUT)
cc:
	@cc $(SRC) -o $(OUT)
	@./$(OUT)

gdb:
	@$(CC) $(SRC) -o $(OUT) -g
	@gdb ./$(OUT)
clean:
	@rm -rf $(OUT)


