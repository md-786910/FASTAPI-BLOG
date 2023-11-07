from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.user_router import userRouter
from router.blog_router import blogRouter


app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5173",
    # "http://localhost:8080",
    # "http://your_frontend_domain",
    # "https://your_frontend_domain",
]

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# simple route
@app.get("/")
def check_server():
    return {"server is working"}


app.include_router(userRouter)
app.include_router(blogRouter)
