from fastapi import FastAPI
from models import User, Feedback

app = FastAPI()

#user = User(
    #name="ванёк гладких крутой с 1 айдишником",
    #id=1
#)

feedback_storage = []

@app.get("/users")
def get_user():
    return user

@app.post("/user")
def check_user(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

# Дополнительно: можно посмотреть все отзывы
@app.get("/feedback")
def get_all_feedback():
    return feedback_storage

# uvicorn t1_3-2_2:app --reload --port 8003