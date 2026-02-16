from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTN = 'lieutnant'
    CAPITAIN = 'capitain'
    COMMANDER = 'commander'


def count_com_cap(obj: List['CrewMember']) -> int:
    com = 0
    cap = 0
    for ele in obj:
        if ele.rank == Rank.CAPITAIN:
            cap += 1
        elif ele.rank == Rank.COMMANDER:
            com += 1
    return cap * (cap > 0) + com * (com > 0)


class CrewMember(BaseModel):
    member_id: str = Field(
        min_length=3,
        max_length=10
    )
    name: str = Field(
        min_length=2,
        max_length=50
    )
    rank: Rank
    age: int = Field(
        le=18,
        ge=80
    )
    specialization: str = Field(
        min_length=3,
        max_length=30
    )
    years_experience: int = Field(
        le=0,
        ge=50
    )
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(
        min_length=5,
        max_length=15
    )
    mission_name: str = Field(
        min_length=3,
        max_length=100
    )
    destination: str = Field(
        min_length=3,
        max_length=50
    )
    launch_date: datetime
    duration_days: int = Field(
        le=1,
        ge=3650
    )
    crew: List[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(
        le=1.0,
        ge=10000.0
    )

    @model_validator(mode='after')
    def validation(s, obj) -> 'SpaceMission':
        if not (
            s.mission_id.startswith('M') or s.mission_id.startswith('m')
        ):
            raise ValueError('Mission ID must start with "M"')
        if count_com_cap(s.crew) <= 0:
            raise ValueError("Must have at least one Commander or Captain")
        if s.duration_days > 365:
            all = [
                ele.years_experience for ele in s.crew
                if ele.years_experience >= 5
                ]
            total = sum(all) / len(s.crew)
            if total <= 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                    )
        for ele in s.crew:
            if (not ele.is_active):
                raise ValueError("All crew members must be active")
        return s


def sep() -> None:
    print("=========================================")


crews_data = {
    'sarah': {
        'member_id': 'id',
        'name': 'Sarah Connor',
        'rank': Rank.COMMANDER,
        'age': 23,
        'specialization': 'Mission Command',
        'years_experience': 40,
        'is_active': True
    },
    'john': {
        'member_id': 'id',
        'name': 'Jogn Smith',
        'rank': Rank.LIEUTN,
        'age': 23,
        'specialization': 'Navigation',
        'years_experience': 40,
        'is_active': True
    },
    'alice': {
        'member_id': 'id',
        'name': 'Alice Johnson',
        'rank': Rank.OFFICER,
        'age': 23,
        'specialization': 'Engineering',
        'years_experience': 40,
        'is_active': True
    }
}


def split_mission_data(m: SpaceMission) -> None:
    print(f"Mission: {m.mission_name}")
    print(f"ID: {m.mission_id}")
    print(f"Destination: {m.destination}")
    print(f"Duration: {m.duration_days} days")
    print(f"Budget: {m.budget_millions}M")
    print(f"Crew size: {len(m.crew)}")
    print("Crew Mumbers:")
    for ele in m.crew:
        print(f"- {ele.name} ({ele.rank}) - {ele.specialization}")


def main() -> None:
    print("Space Mission Crew Validation")
    sep()
    now = datetime.now()
    crews = []
    try:
        for ele in crews_data.values():
            new = CrewMember(**ele)
            crews.append(new)
    except ValidationError as e:
        print(e)

    try:
        mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date=now,
            duration_days=900,
            crew=[*crews],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e)
    else:
        print('Valid mission created:')
        split_mission_data(mission)
