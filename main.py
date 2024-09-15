from fastapi import FastAPI
from ticket.routes import app as ticketRoutes
from auth.routes import app as authRoutes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ticketRoutes)
app.include_router(authRoutes)