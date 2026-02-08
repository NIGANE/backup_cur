from pydantic import BaseModel, ValidationError


class User(BaseModel):
    name: str
    email: str
    accound_id: int
user: User = None
try:
    user = User(name=32, email="mail.com", accound_id=3224)
except ValidationError as e:
    print("Error: ", e.errors()[0]['msg'])
else:
    print(user)
