from pydantic import BaseModel, field_validator, ValidationError, Field
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3,
        max_length=10,
        description="station id should be between (3-10) characters"
        )
    name: str = Field(
        min_length=3,
        max_length=10,
        description="name should be between (1-50) characters"
        )
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenence: datetime
    is_operational: bool = True
    notes: Optional[str]

    # @field_validator('crew_size')
    # @classmethod
    # def validate_crew_size(cls, v: int) -> int:
    #     if (v > 20 or v < 1):
    #         raise ValueError("must use size between (1-20)")
    #     else:
    #         return v

    # @field_validator('power_level')
    # @classmethod
    # def validate_power_level(cls, v: float) -> float:
    #     if (v > 100.0 or v < 0.0):
    #         raise ValueError("must use power level between (1-20)")
    #     else:
    #         return v

    # @field_validator('oxygen_level')
    # @classmethod
    # def validate_oxygen_level(cls, v: float) -> float:
    #     if (v > 100.0 or v < 0.0):
    #         raise ValueError("must use size between (1-20)")
    #     else:
    #         return v

    # @field_validator('notes')
    # @classmethod
    # def validate_notes(cls, v: str) -> str:
    #     if (len(v) > 200):
    #         raise ValueError("must use string between (0 - 200) characters")
    #     else:
    #         return v


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    station = None
    import datetime
    print(datetime.datetime.now())
    # try:
    #     station = SpaceStation(station_id="ISS001", name="International Space Station", crew_size=6, power_level=85.5, oxygen_level=92.3, is_operational=True, last)


main() if __name__ == "__main__" else ""
