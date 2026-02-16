from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum
from typing import Optional


def publish_data(obj: 'AlienContact') -> None:
    print("Valid contact report:")
    print(f"ID: {obj.contact_id.upper()}")
    print(f"Type: {obj.contact_type}")
    print(f"Location: {obj.location}")
    print(f"Signal: {obj.signal_strength}/10")
    print(f"Duration: {obj.duration_minutes} minutes")
    print(f"Witnesses: {obj.witness_count}")
    print(f"Message: '{obj.message_received}'")


class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


def ne_len(s: Optional[str]) -> int:
    if isinstance(s, type(None)):
        return 0
    else:
        return len(s)


class AlienContact(BaseModel):
    contact_id: str = Field(
        min_length=5,
        max_length=15,
        description="Contact id should be between 5-15 and starts with AC"
    )
    timestamp: datetime = Field(
        description="Timestamp is required"
    )
    location: str = Field(
        min_length=3,
        max_length=100,
        description="Location should be between 3-15"
    )
    contact_type: ContactType = Field(
        description="Contact type should be valid type"
    )
    signal_strength: float = Field(
        ge=0.0,
        le=10.0,
        description="Signal stength should be between 0.0-10.0"
    )
    duration_minutes: int = Field(
        ge=1,
        le=1440,
        description="Duration should be less than 24 hours"
    )
    witness_count: int = Field(
        ge=1,
        le=100,
        description="witnesses should be between 1-100 people"
    )
    message_received: Optional[str] = Field(
        max_length=500,
        description="massages should be less than 500 characters"
    )
    is_verified: bool = False

    @model_validator(mode='after')
    def validation(self) -> 'AlienContact':
        if not self.contact_id.startswith('AC'):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if (not self.is_verified):
            print(self.is_verified)
            raise ValueError("Physical contact reports must be verified")
        if (self.witness_count < 3):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        if (self.signal_strength > 7.0 and ne_len(self.message_received) == 0):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
                )
        return self


def sep() -> None:
    print("======================================")


def create_new_Contact(data: dict) -> None:
    try:
        alien_contact = AlienContact(
            **data
        )
    except ValidationError as e:
        print('Expected validation error:')
        print(f'{e.errors()[0]['ctx']['error']}')
    except ValueError as e:
        print('Expected validation error:')
        print(f"{e}")
        print("value")
    else:
        publish_data(alien_contact)


def main() -> None:
    print("Alien Contact Log Validation")
    sep()
    now = datetime.now()
    valid_records = {
        'contact_id': 'AC_2024_001',
        'timestamp': now,
        'location': 'Area 51, Nevada',
        'contact_type': ContactType.RADIO.value,
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }
    fault_records = {
        'contact_id': 'AC_2024_001',
        'timestamp': now,
        'location': 'Area 51, Nevada',
        'contact_type': ContactType.RADIO.value,
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 2,
        'message_received': 'Greetings from Zeta Reticuli',
        'is_verified': True
    }
    create_new_Contact(valid_records)
    print()
    sep()
    create_new_Contact(fault_records)


if __name__ == '__main__':
    main()
