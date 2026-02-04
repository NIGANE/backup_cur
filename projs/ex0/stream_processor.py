from typing import Any, List, Union
from abc import ABCMeta, abstractmethod


def ne_sum(data: List[int]) -> int:
    re = 0
    try:
        for ele in data:
            re += int(ele)
    except ValueError as e:
        print(e)
    return re


def ne_len(data: Union[List[int], str, List[str]]) -> int:
    re = 0
    for ele in data:
        re += 1
    return re


def get_words(data: str) -> int:
    return ne_len(data.split(" "))


def remove(data: str, item: str) -> str:
    i = 0
    found = 0
    while (i < ne_len(data)):
        j = 0
        while (j < ne_len(item) and data[i + j] == item[j]):
            j += 1
        if j == ne_len(item):
            found = 1
            break
        i += 1
    if (found):
        return data[i + j:]
    else:
        return data


def in_string(item: str, data: str) -> bool:
    i = 0
    while (i < ne_len(data)):
        j = 0
        while (j < ne_len(item) and data[i + j] == item[j]):
            j += 1
        if j == ne_len(item):
            return True
        i += 1


class DataProcessor(metaclass=ABCMeta):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        if isinstance(data, int):
            return (
                f"Processed 1 "
                f"numeric value, sum={data}, avg={data}"
                )
        elif isinstance(data, list):
            try:
                sum = ne_sum(data)
                avg = sum / ne_len(data)
                return (
                    f"Processed {ne_len(data)} "
                    f"numeric values, sum={sum}, avg={avg}"
                    )
            except ValueError:
                return data
        else:
            raise ValueError("Error: incorect form for gived data")

    def validate(self, data: Any) -> bool:
        if isinstance(data, int):
            print("Validation: Numeric data verified")
            return True
        elif isinstance(data, list):
            try:
                for ele in data:
                    int(ele)
            except ValueError:
                print("Validation: Numeric data not verified")
                return False
            else:
                print("Validation: Numeric data verified")
                return True
        else:
            raise ValueError("Validation: Numeric data not verified")


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        words = get_words(data)
        count = ne_len(data)
        return (
            f"Processed text: {count} characters, {words} words"
            )

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, str):
                print("Validation: Text data verified")
                return True
            else:
                raise ValueError("Error: Text data Not verified")
        except ValueError as e:
            print(e)
            return False


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        template = {
            "ERROR: ": "[ALERT] ERROR level detected: ",
            "INFO: ": "[INFO] INFO level detected: ",
            "WARNING: ": "[ALERT] WARNING level deceted: ",
            }
        i = 0
        while i < ne_len(template):
            if (in_string([*template][i], data)):
                return (
                    f"{template[[*template][i]]} "
                    f"{remove(data, [*template][i])}"
                    )
            i += 1
        return data

    def validate(self, data: Any) -> bool:
        try:
            for ele in ["ERROR: ", "INFO: ", "WARNING: "]:
                if in_string(ele, data):
                    print("Validation: Log entry verified")
                    return True
                else:
                    raise ValueError("Validation: Log entry not verified")
        except ValueError as e:
            print(e)
            return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("")

    num_data = [1, 2, 3, 4, 5]
    num_process = NumericProcessor()
    print(f"Processing data: {num_data}")
    try:
        num_process.validate(num_data)
        print(num_process.format_output(num_process.process(num_data)))
    except ValueError as e:
        print(e)
    print("")

    text_data = "Hello Nexus World"
    text_process = TextProcessor()
    print(f"Processing data: \"{text_data}\"")
    text_process.validate(text_data)
    print(text_process.format_output(text_process.process(text_data)))
    print("")

    log_data = "ERROR: Connection timeout"
    log_process = LogProcessor()
    print(f"Processing data: \"{log_data}\"")
    log_process.validate(log_data)
    print(log_process.format_output(log_process.process(log_data)))
    print("")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    re = [[1, 2, 3], "Hello worlds", "INFO: system ready"]
    obj = [num_process, text_process, log_process]
    i = 0
    while (i < ne_len(re)):
        print(f"Result {i + 1}: {obj[i].process(re[i])}")
        i += 1
    print("")
    print("Foundation systems online. Nexus ready for advanced streams.")


if (__name__ == "__main__"):
    main()
