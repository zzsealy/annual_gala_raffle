from fastapi import APIRouter
from pydantic import BaseModel
from app.models import RaffleQueue

router = APIRouter()

class AddQueueInput(BaseModel):
    prize_level: int
    prize_type: str # 'gift' or 'cash'
    insert_position: str # 'before' or 'after'
    person_num: int # 抽奖人数

@router.get("/raffle_queue")
async def get_raffle_queue():
    raffle_queue = await RaffleQueue.filter(is_drawn=False).order_by('order').values()
    return raffle_queue

@router.post("/raffle_queue/add")
async def add_raffle_queue(input: AddQueueInput):
    # 根据等级和类型生成配置
    level_map = {
        0: {'name': '特等奖', 'personNum': 1, 'gift_img': '/raffle/special_gift.png'},
        1: {'name': '一等奖', 'personNum': 3, 'gift_img': '/raffle/one_gift.png'},
        2: {'name': '二等奖', 'personNum': 10, 'gift_img': '/raffle/two_gift.png'},
        3: {'name': '三等奖', 'personNum': 5, 'gift_img': '/raffle/three_gift.png'},
    }
    
    config = level_map.get(input.prize_level, level_map[3])
    desc = f"{config['name']}实物" if input.prize_type == 'gift' else f"{config['name']}现金"
    img_url = config['gift_img'] if input.prize_type == 'gift' else '/raffle/cash.png'
    person_num = input.person_num
    
    # 获取需要插入的 order 顺序
    active_queues = await RaffleQueue.filter(is_drawn=False).order_by('order')
    
    if not active_queues:
         # 如果当前没有队伍，随便写个 order
         new_order = 0
    else:
        if input.insert_position == 'before':
            # 插在还没抽的最前面
            new_order = active_queues[0].order - 1
        else:
            # 插在还没抽的最后面
            new_order = active_queues[-1].order + 1
            
    queue = await RaffleQueue.create(
        prize_level=input.prize_level,
        raffleQueuePersonNum=person_num,
        desc=desc,
        img_url=img_url,
        order=new_order
    )
    
    return {"status": "success", "id": queue.id}
