from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `participants` MODIFY COLUMN `code` VARCHAR(50) NOT NULL COMMENT '工号';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `participants` MODIFY COLUMN `code` INT NOT NULL COMMENT '工号';"""


MODELS_STATE = (
    "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"
)
