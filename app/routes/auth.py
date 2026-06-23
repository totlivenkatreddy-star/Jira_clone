from fastapi import APIRouter

router = APIRouter()


# Dummy database
users = [
    {
        "id": 1,
        "email": "venkat@gmail.com",
        "password": "12345"
    }
]

#login user works  with swagger only
@router.post("/login")
def login(email: str, password: str):

    for user in users:

        if user["email"] == email and user["password"] == password:

            return {
                "status": "success",
                "message": "Login successful",
                "user_id": user["id"]
            }

    return {
        "status": "failed",
        "message": "Invalid credentials"
    }