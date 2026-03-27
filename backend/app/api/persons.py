from fastapi import APIRouter
from app.models import Participant

router = APIRouter()

@router.get("/persons")
async def get_persons():
    persons = await Participant.filter(is_drawn=False).all()
    r = [{"code": p.code, "name": p.name} for p in persons]
    return r