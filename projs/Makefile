CC = cc 
OUT = tt
SRC = clean.c main.c ./fifo/fifo.c helpers.c init.c parsing.c simulation.c \
		resources_management.c schedular_management.c coder_actions.c  time.c \
		heap.c burn_out_protocol.c

ARGS = 5 3000 200 200 200 10 800 fifo
#		nb_coders	burn_out  compile_t   debug_t  refactor_t  req_compiles  cooldown   schedular
#	801 fifo
#	


arg:run
	@./$(OUT) $(ARGS)

test:
	@cc test.c
	@./a.out


run:
	@$(CC) $(SRC) -o $(OUT)
cc:
	@cc $(SRC) -o $(OUT)

gdb:GG
	@gdb --args ./$(OUT) $(ARGS)
clean:
	@rm -rf ./$(OUT)
	@rm -rf ./a.out

GG:
	@$(CC) $(SRC) -o $(OUT) -g
tes:
	./$(OUT)

heapo:
	@$(CC) heap.c time.c
	@./a.out
