from fastapi import APIRouter, Query
from tortoise.expressions import Q

from app.models import Participant, ParticipantSpecial, RaffleQueue
from app.special_raffle import (
    extract_special_position,
    get_special_pool_positions,
    is_special_prize_level,
)

router = APIRouter()

@router.get("/persons")
async def get_persons(queue_id: int | None = Query(default=None)):
    # 为了复用原有接口，这里根据当前轮次自动切换普通奖池或特别大奖奖池。
    if queue_id is not None:
        raffle_queue = await RaffleQueue.filter(id=queue_id).first()
        if raffle_queue and is_special_prize_level(raffle_queue.prize_level):
            position = extract_special_position(raffle_queue.desc)
            special_positions = get_special_pool_positions(position)
            persons = await ParticipantSpecial.filter(
                Q(position__in=special_positions)
            ).all()
            return [{"code": p.code, "name": p.name} for p in persons]

    persons = await Participant.filter(is_drawn=False).all()
    return [{"code": p.code, "name": p.name} for p in persons]