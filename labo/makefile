search_dataset:
	uv run python3 -m src search_dataset --dataset_path data/datasets/UnansweredQuestions/dataset_code_public.json --k 4 --save_directory out

search:
	uv run python3 -m src search "error on class" --k 1

index:
	uv run python3 -m src index --max_chunk_size 2000

clean:
	@rm -rf src/__pycache__

clean-all: clean
	@rm -rf data/process -rf