import sys
# import os
from json import JSONDecodeError, load as json_load, dump
from typing import Dict, List, Optional, Any

from src.models.FunctionDefinition import FunctionDefinition
from src.models.PromptValidation import PromptValidation
from src.models.ValidData import ValidData
from src.models.ErrorHandler import MyError
from pydantic import ValidationError


def error_usage_func() -> str:
    return ("Usage: uv run python -m src --functions_definition."
            + " <fn_definitions_file>.json --input <input_file>.json "
            + "--output <output_file>.json")


def load_inputs(s: str) -> List[Dict[str, Any]]:
    data: List[Dict[str, Any]] = []
    try:
        with open(s, 'r') as f:
            data = json_load(f)
    except FileNotFoundError as e:
        raise MyError(f"FileNotFoundError: {e.filename} not found.")
    except JSONDecodeError as e:
        raise MyError(f"JsonError: {e} not valid json format")
    else:
        return data


def ends_with(src: Optional[str], sub: str) -> bool:
    i: int = 0
    if not src:
        return False
    while i < len(sub):
        if (sub[len(sub) - i - 1] != src[len(src) - i - 1]):
            return False
        i += 1
    return True


def parse() -> ValidData:
    func_definitions: str = "--functions_definition"
    input: str = "--input"
    output: str = "--output"
    model_flag: str = "--model"
    if len(sys.argv) < 7:
        raise MyError(f"Invalid arguments: {error_usage_func()}")

    fn_definition_file: Optional[str] = (
        sys.argv[sys.argv.index(func_definitions) + 1]
        if func_definitions in sys.argv else None
                         )
    input_file: Optional[str] = (
        sys.argv[sys.argv.index(input) + 1] if input in sys.argv else None)
    output_file: Optional[str] = (
        sys.argv[sys.argv.index(output) + 1] if output in sys.argv else None)
    model: Optional[str] = (
        sys.argv[sys.argv.index(model_flag) + 1] if model_flag in sys.argv
        else None
    )
    if (not ends_with(output_file, ".json") or
            not ends_with(input_file, ".json") or
            not ends_with(fn_definition_file, ".json")):
        raise MyError(f"Invalid arguments: {error_usage_func()}")
    if (
        (input_file is None) or
        (fn_definition_file is None) or
        (output_file is None)

    ):
        raise MyError(
            f"Error: Missing required arguments.\n{error_usage_func()}")

    fn_definitions: List[Dict[str, Any]] = load_inputs(fn_definition_file)
    input_prompts: List[Dict[str, Any]] = load_inputs(input_file)
    validated_functions: List[FunctionDefinition] = []
    validated_prompts: List[PromptValidation] = []
    try:
        for row_data in fn_definitions:
            validated_functions.append(FunctionDefinition(**row_data))
        for row_data in input_prompts:
            validated_prompts.append(PromptValidation(**row_data))
    except ValidationError as e:
        raise MyError(
            f"ValidationError ({e.errors()[0]['type']}, "
            f"'{e.errors()[0]['loc'][0]}'): {e.errors()[0]['msg']} ")
    except Exception as e:
        raise MyError(f"Error (validation): {e}")
    filtered_functions: List[Dict[str, Any]] = []

    pomp: Dict[str, Any] = {}
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

    return ValidData(filtered_functions, validated_prompts, output_file, model)


def dump_json(outs: List[Dict[str, Any]], out_file: str) -> None:
    try:
        with open(out_file, "w") as file:
            dump(outs, file, indent=4)
        print(" - Output file is ready.")
    except FileNotFoundError:
        raise MyError(f"Error: \"{out_file}\" is not a valid path")
