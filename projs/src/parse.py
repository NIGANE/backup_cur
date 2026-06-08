import sys
import os
from json import JSONDecodeError, load as json_load, dump
from typing import Dict, List, Optional

from src.Agent import Prompt
from src.models.FunctionDefinition import FunctionDefinition
from src.models.PromptValidation import PromptValidation
from src.models.ValidData import ValidData


def error_usage_func():
    print("Error: Missing required arguments.", file=sys.stderr)
    print(
        "Usage: python main.py --functions_definition "
        "<fn_definitions_file> --input <input_file> "
        "--output <output_file>",
        file=sys.stderr
    )
    sys.exit(1)


def load_inputs(s: str) -> Optional[List[Dict]]:
    data = []
    try:
        with open(s, 'r') as f:
            data = json_load(f)
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
        return None
    except JSONDecodeError as e:
        print(f"Error: {e} not vald json format")
        return None
    except Exception as e:
        print(f"Error: {e.__class__.__name__}")
        return None
    else:
        return data


def parse():
    func_definitions = "--functions_definition"
    input = "--input"
    output = "--output"
    fn_definition_file = (
        sys.argv[sys.argv.index(func_definitions) + 1]
        if func_definitions in sys.argv else None
                         )
    input_file = (
        sys.argv[sys.argv.index(input) + 1] if input in sys.argv else None)
    output_file = (
        sys.argv[sys.argv.index(output) + 1] if output in sys.argv else None)
    outupt_folder = os.path.basename(os.path.dirname(output_file))
    input_folder = os.path.basename(os.path.dirname(input_file))
    if (
        (input_file is None) or
        (fn_definition_file is None) or
        (output_file is None)

    ):
        error_usage_func()
        return

    fn_definitions = load_inputs(fn_definition_file)
    input_prompts = load_inputs(input_file)
    if (fn_definitions is None) or (input_prompts is None):
        print("Error: Failed to load input files.")
        sys.exit(1)
    validated_functions = []
    validated_prompts = []
    try:
        for row_data in fn_definitions:
            validated_functions.append(FunctionDefinition(**row_data))
        for row_data in input_prompts:
            validated_prompts.append(PromptValidation(**row_data))
    except Exception as e:
        print(f"Validation failed: {e}")
        return None
    filtered_functions = []

    pomp = {}
    for fn in validated_functions:
        pomp["name"] = fn.name
        pomp["description"] = fn.description
        if fn.__dict__.get("parameters") is not None:
            params = {}
            for param in fn.__dict__["parameters"]:
                params[param] = fn.__dict__["parameters"][param].type
            pomp["parameters"] = params
        else:
            pomp["parameters"] = None
        pomp["returns"] = fn.returns.type
        filtered_functions.append(pomp)
        pomp = {}

    return ValidData(filtered_functions, validated_prompts, output_file)


def dump_json(outs: List[Prompt], out_file: str):
    try:
        with open(out_file, "w") as file:
            dump(outs, file, indent=4)
        print("Output file is ready.")
    except BaseException:
        print("error while dump into json output file")
