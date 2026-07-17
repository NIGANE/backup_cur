CC = cc 
OUT = tt
SRC = main.c ./heap/*.c ./helpers/*.c ./simulation.c ./fifo/fifo.c

ARGS = 1 400 10 10 10 4 2 edf


arg:run
	@./$(OUT) $(ARGS)

test:
	@cc test.c
	@./a.out


run:
	@$(CC) $(SRC) -o $(OUT)
cc:
	@cc $(SRC) -o $(OUT)

gdb:
	@$(CC) $(SRC) -o $(OUT) -g
	@gdb --args ./$(OUT) $(ARGS)
clean:
	@rm -rf ./$(OUT)
	@rm -rf ./a.out

tes:
	./$(OUT)
