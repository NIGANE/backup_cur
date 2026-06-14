import sys
from src.parse import error_usage_func
from src.parse import parse
from src.Agent import Agent, Prompt
from src.parse import dump_json
from src.models.ErrorHandler import MyError
from src.models.ValidData import ValidData

from typing import List
from llm_sdk import Small_LLM_Model


def main() -> None:
    try:
        if (len(sys.argv) < 7):
            error_usage_func()
        print("|-> Validating Prompts and Functions definitions...")
        valid_data: ValidData = parse()
        if not valid_data:
            raise MyError("invalid input")

        #  instantiate the Model with Prompts and Functions
        print("|-> Downloading The Model LLM",
              (valid_data.model if valid_data.model else "Qwen/Qwen3-0.6B"))
        model: Small_LLM_Model = (
            Small_LLM_Model(valid_data.model) if valid_data.model
            else Small_LLM_Model())
        agent = Agent(
            model,
            [pt.prompt for pt in valid_data.prompts],
            valid_data.funcs
            )
        print("|-> Generating output file...")
        results: List[Prompt] = agent.resolve_prompts()
        dump_json(
            [
                {
                    "prompt": ptt.prompt, "name": ptt.name,
                    "parameters": ptt.parameters
                }
                for ptt in results],
            valid_data.output_file)
    except MyError as e:
        print(f"# {e}")
    except BaseException as e:
        print(f"External ERROR catched: {e}")


if __name__ == "__main__":
    main()
