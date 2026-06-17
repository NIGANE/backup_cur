
FILE="./maps/challenger/01_the_impossible_dream.txt"

run:
	@uv run python3 -m src $(FILE)

test:
	@uv run python3 -m main $(FILE)

clean:
	@echo "Cleaning up..."
	@rm -rf data/output/*
	@rm -rf */__pycache__/
	@rm -rf __pycache__
	@rm -rf */*/__pycache__/

clean-all: clean
	@rm -rf .venv
