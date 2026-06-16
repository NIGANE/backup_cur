
FILE="./maps/easy/01_linear_path.txt"

run:
	uv run -m src $(FILE)


clean:
	@echo "Cleaning up..."
	@rm -rf data/output/*
	@rm -rf */__pycache__/
	@rm -rf __pycache__
	@rm -rf */*/__pycache__/

clean-all: clean
	@rm -rf .venv
