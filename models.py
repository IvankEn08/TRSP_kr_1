from pydantic import BaseModel, validator, Field

BAD_WORDS = ["кринж", "рофл", "вайб"]

class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @validator("message")
    def check_bad_words(cls, v):
        lowered = v.lower()
        for word in BAD_WORDS:
            if word in lowered:
                raise ValueError("Использование недопустимых слов")
        return v