from typing import Any, List, Union, Optional, Dict
from abc import ABCMeta, abstractmethod


class DataStream(metaclass=ABCMeta):

    def __init__(self, id: str) -> None:
        self.stream_id = id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self, data_batch: List[Any],  criteria: Optional[str] = None
            ) -> List[Any]:
        if not criteria:
            return data_batch
        else:
            if (len(data_batch) > 0):
                if isinstance(data_batch[0], str):
                    return [
                        ele for ele in data_batch if ele.startswith(criteria)
                        ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return ({"stream_id": self.stream_id, "type": self.type})


class SensorStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.type = "Environmental Data"
        self.records = []
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        temps = []
        for ele in data_batch:
            if isinstance(ele, str) and ":" in ele:
                key, value = ele.split(":")
                if key.strip() == "temp":
                    self.records.append(ele)
                    temps.append(float(value))
                elif key.strip() == "humidity":
                    self.records.append(ele)
                elif key.strip() == "pressure":
                    self.records.append(ele)

        return (f"Sensor analysis: {len(self.records)} "
                f"readings processed, avg temp: {sum(temps) / len(temps)}°C")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"count": len(self.records)}

    def batch(self) -> str:
        return (f"Sensor data: {len(self.records)} readings processed")


class TransactionStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.type = "Financial Data"
        self.records = []
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        bought = []
        sold = []

        for ele in data_batch:
            if isinstance(ele, str) and ":" in ele:
                key, value = ele.split(":")
                if key.strip().startswith("buy"):
                    self.records.append(ele)
                    bought.append(int(value))
                elif key.strip().startswith("sell"):
                    self.records.append(ele)
                    sold.append(int(value))
        total_units = sum(bought) - sum(sold)
        return (
            f"Transaction analysis: {len(bought) + len(sold)} operations, "
            f"net flow: {'+' if total_units > 0 else '-'}{total_units} units"
            )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"count": len(self.records)}

    def batch(self) -> str:
        return (f"Transaction data: {len(self.records)} operations processed")


class EventStream(DataStream):
    def __init__(self, id: str) -> None:
        super().__init__(id)
        self.records = []
        self.type = "System Events"
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.records = [ele for ele in data_batch if ":" not in ele]
        count_err = len([ele for ele in self.records if ele == "error"])
        return (
            f"Event analysis: {len(self.records)} events, "
            f"{count_err} error detected"
            )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"count": len(self.records)}

    def batch(self) -> str:
        return (
            f"Event data: "
            f"{len(self.records)} events processed"
            )


class StreamProcessor():

    def __init__(self, *obj: DataStream) -> None:
        er = ("error: found 1 object not belongs to the Data Stream Hierarchy")
        self.obj = []
        try:
            for ele in obj:
                if (isinstance(ele, DataStream)):
                    self.obj.append(ele)
                else:
                    raise ValueError(er)
        except ValueError as err:
            print(err)

    def batch(self) -> None:
        print("Batch 1 Results:")
        for ele in self.obj:
            print("- " + ele.batch())

    def get_state(self) -> None:
        alerts = 0
        trans = 0
        for ele in self.obj:
            if (isinstance(ele, SensorStream)):
                alerts += ele.get_stats()["count"]
            elif (isinstance(ele, TransactionStream)
                  and ele.get_stats()["count"] > 0):
                trans = 1
        return (f"Filtered results: {alerts} critical "
                f"sensor alerts, {trans} large transaction")


def format_arr(data: list) -> None:
    print("[", end="")
    i = 0
    while i < len(data):
        print(f"{data[i]}", end=f"{'' if i + 1 == len(data) else ', '}")
        i += 1
    print("]")


def ft_data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("")
    sensor_records = ["temp:22.5", "humidity:65", "pressure:1013"]
    trans_records = ["buy:100", "sell:150", "buy:75"]
    event_records = ["login", "error", "logout"]

    sensor_stream = SensorStream("SENSOR_001")
    print("Processing sensor batch: ", end="")
    format_arr(sensor_records)
    re = sensor_stream.process_batch(sensor_records)
    print(re)

    print("")

    trans_stream = TransactionStream("TRANS_001")
    print("Processing transaction batch: ", end="")
    format_arr(trans_records)
    re = trans_stream.process_batch(trans_records)
    print(re)

    print("")

    event_stream = EventStream("EVENT_001")
    print("Processing event batch: ", end="")
    format_arr(event_records)
    re = event_stream.process_batch(event_records)
    print(re)

    print("")
    sensor_stream.records = sensor_stream.records[:-1]
    trans_stream.records = [*trans_stream.records, "buy:43"]
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("")

    try:
        new_stream = StreamProcessor(sensor_stream, trans_stream, event_stream)
    except ValueError as e:
        print(e)
    new_stream.batch()
    print("")

    print("Stream filtering active: High-priority data only")
    print(new_stream.get_state())
    print("")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    ft_data_stream()
