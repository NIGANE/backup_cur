

class ValidData():
    def __init__(self, functions_definitions, input_prompts, out: str):
        self.funcs = functions_definitions
        self.prompts = input_prompts
        self.output_file = out


class InvalidData():
    def __init__(self):
        return None
