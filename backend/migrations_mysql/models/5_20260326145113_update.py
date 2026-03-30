from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `raffle_queue` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `prize_level` INT NOT NULL COMMENT '奖项等级，1为一等奖，以此类推, 0特等奖',
    `raffleQueuePersonNum` INT NOT NULL COMMENT '抽奖人数',
    `desc` VARCHAR(100) NOT NULL COMMENT '抽奖描述',
    `img_url` VARCHAR(100) COMMENT '图片路径，用于前端展示',
    `order` INT NOT NULL COMMENT '排序，越小越靠前',
    `is_drawn` BOOL NOT NULL COMMENT '是否已抽奖' DEFAULT 0,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='抽奖队列';
        DROP TABLE IF EXISTS `lottery_queue`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `raffle_queue`;"""


MODELS_STATE = (
    "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"
)
