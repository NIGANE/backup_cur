from pydantic import BaseModel, ValidationError, Field
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3,
        max_length=10,
        description="station id should be between (3-10) characters"
        )
    name: str = Field(
        min_length=1,
        max_length=50,
        description="name should be between (1-50) characters"
        )
    crew_size: int = Field(
        ge=1,
        le=20,
        description="Input should be less than or equal to 20"
    )
    power_level: float = Field(
        ge=0.0,
        le=100.0,
        description="power level should be between (0-100)"
    )
    oxygen_level: float = Field(
        ge=0.0,
        le=100.0,
        description="oxygen level should be between (0-100)"
    )
    last_maintenence: datetime = Field(
        description="input should be valid datetime"
    )
    is_operational: bool = True
    notes: Optional[str] = Field(
        max_length=200,
        description="notes should be less than or equal 200"
    )


def output_mess(station: SpaceStation) -> None:
    print("Valid station created")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size}")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(
          f"Status: "
          f"{"Operational" if station.is_operational else "Not operational"}"
          )


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    station = None
    now = datetime.now()
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenence=now,
            is_operational=True,
            notes=""
            )
    except ValidationError as e:
        print(e)
    else:
        output_mess(station)
    print()
    print("========================================")
    print("Expected validation error:")
    fault_station = None
    now = datetime.now()
    try:
        fault_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=56,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenence=now,
            is_operational=True,
            notes=""
            )
        print(fault_station)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


main() if __name__ == "__main__" else ""
