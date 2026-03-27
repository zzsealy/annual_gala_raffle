import random
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models import RaffleQueue, Participant, RaffleRecord
from tortoise.transactions import in_transaction

router = APIRouter()

class InputSchema(BaseModel):
    queue_id: int

@router.post("/raffle")
async def raffle(input: InputSchema):
    queue_id = input.queue_id
    
    async with in_transaction() as conn:
        # 1. 拿到这个抽奖队列 (使用 select_for_update 锁定，防止并发重复抽奖)
        raffle_queue = await RaffleQueue.filter(id=queue_id).select_for_update().first()
        
        if not raffle_queue:
            raise HTTPException(status_code=404, detail="未找到该抽奖轮次")
        
        if raffle_queue.is_drawn:
            raise HTTPException(status_code=400, detail="该轮次已经抽过奖了")

        # 2. 拿到所有未抽奖的人员
        participants = await Participant.filter(is_drawn=False).values('id', 'name', 'code')
        
        raffle_queue_person_num = raffle_queue.raffleQueuePersonNum
        if len(participants) < raffle_queue_person_num:
             raise HTTPException(status_code=400, detail=f"剩余人员不足({len(participants)})，无法完成本次抽奖")

        # 3. 随机抽取
        winners = random.sample(participants, raffle_queue_person_num) 

        # 4. 更新状态
        raffle_queue.is_drawn = True
        await raffle_queue.save()

        winner_ids = [winner['id'] for winner in winners]
        await Participant.filter(id__in=winner_ids).update(is_drawn=True)
        
        # 5. 写入中奖记录
        records = [
            RaffleRecord(
                participant_id=winner['id'], 
                desc=raffle_queue.desc,
                name=winner['name'],
                code=winner['code']
            ) for winner in winners
        ]
        await RaffleRecord.bulk_create(records)
        
        return winners