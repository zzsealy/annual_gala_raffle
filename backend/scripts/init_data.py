import asyncio
import os
import sys
import random

# 加入项目根目录到 sys.path，确保可以导入 app (向上两级到达 backend)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from tortoise import Tortoise
from app.db import TORTOISE_ORM
from app.models import RaffleQueue, Participant, RaffleRecord

async def reset_db_data():
    # 清空所有中奖记录
    await RaffleRecord.all().delete()
    
    # 重置所有人员未中奖状态
    await Participant.all().update(is_drawn=False)

    # 清空抽奖队列
    await RaffleQueue.all().delete()

    # 再插入
    index = 10
    # 先插入三等奖实物
    for i in range(5):
        create_info = {
            'prize_level': 3,
            'raffleQueuePersonNum': 10,
            'desc': '背包',
            'img_url': '/raffle/three_gift.png',
            'order': index
        }
        await RaffleQueue.create(**create_info)
        index += 1
    # 插入三等奖现金
    for i in range(5):
        create_info = {
            'prize_level': 3,
            'raffleQueuePersonNum': 10,
            'desc': '现金200元',
            'img_url': '/raffle/cash.png',
            'order': index
        }
        await RaffleQueue.create(**create_info)
        index += 1
    # 二等奖实物
    create_info_two_gift = {
            'prize_level': 2,
            'raffleQueuePersonNum': 10,
            'desc': '剃须刀',
            'img_url': '/raffle/two_gift.png',
            'order': index
    }
    await RaffleQueue.create(**create_info_two_gift)
    index += 1
    # 二等奖现金
    create_info_two_cash = {
            'prize_level': 2,
            'raffleQueuePersonNum': 10,
            'desc': '现金500元',
            'img_url': '/raffle/cash.png',
            'order': index
    }
    await RaffleQueue.create(**create_info_two_cash)
    index += 1

    # 一等奖实物
    create_info_one_gift = {
            'prize_level': 1,
            'raffleQueuePersonNum': 3,
            'desc': '智能手表',
            'img_url': '/raffle/one_gift.png',
            'order': index
    }
    await RaffleQueue.create(**create_info_one_gift)
    index += 1

    # 一等奖现金
    create_info_one_cash = {
            'prize_level': 1,
            'raffleQueuePersonNum': 3,
            'desc': '现金1000元',
            'img_url': '/raffle/cash.png',
            'order': index
    }
    await RaffleQueue.create(**create_info_one_cash)
    index += 1

    # 特等奖实物
    create_info_special_gift = {
            'prize_level': 0,
            'raffleQueuePersonNum': 1,
            'desc': '平板电脑',
            'img_url': '/raffle/special_gift.png',
            'order': index
    }
    await RaffleQueue.create(**create_info_special_gift)
    index += 1

    # 特等奖现金
    create_info_special_cash = {
            'prize_level': 0,
            'raffleQueuePersonNum': 1,
            'desc': '现金3000元',
            'img_url': '/raffle/cash.png',
            'order': index
    }
    await RaffleQueue.create(**create_info_special_cash)

async def run():
    await Tortoise.init(config=TORTOISE_ORM)  # 初始化数据库连接
    await reset_db_data()
    await Tortoise.close_connections()  # 执行完毕后关闭数据库连接

if __name__ == "__main__":
    asyncio.run(run())