answer_dataset:
	uv run python3 -m src answer_dataset \
	--student_search_results_path "data/output/dataset_docs_public.json" \
	--save_directory "data/output/student_res&answer/answer_dataset_docs_public.json"


search_dataset:
	uv run python3 -m src search_dataset \
	--dataset_path data/datasets/UnansweredQuestions/dataset_code_public.json \
	--k 2 \
	--save_directory data/output

search:
	uv run python3 -m src search "error on class" --k 1

index:
	uv run python3 -m src index --max_chunk_size 2000

answer:
	uv run python3 -m src answer \
	"What types are supported as containers in vLLM's JSONTree type definition?" \
	--k 1

clean:
	@rm -rf src/__pycache__

clean-all: clean
# 	@rm -rf data/process -rf