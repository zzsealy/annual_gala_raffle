from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `lottery_queue` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `prize_level` INT NOT NULL COMMENT '奖项等级，1为一等奖，以此类推',
    `LotteryQueuePersonNum` INT NOT NULL COMMENT '抽奖人数'
) CHARACTER SET utf8mb4 COMMENT='抽奖队列';
        ALTER TABLE `participants` ADD `is_is_drawn` BOOL NOT NULL COMMENT '是否已抽奖' DEFAULT 0;
        ALTER TABLE `participants` ADD `code` INT NOT NULL COMMENT '工号';
        ALTER TABLE `participants` DROP COLUMN `department`;
        ALTER TABLE `participants` DROP COLUMN `is_active`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `participants` ADD `department` VARCHAR(100) COMMENT '所属部门';
        ALTER TABLE `participants` ADD `is_active` BOOL NOT NULL COMMENT '是否参与抽奖' DEFAULT 1;
        ALTER TABLE `participants` DROP COLUMN `is_is_drawn`;
        ALTER TABLE `participants` DROP COLUMN `code`;
        DROP TABLE IF EXISTS `lottery_queue`;"""


MODELS_STATE = (
    "eJztWltv2kgU/iuIp6yUrcD4AvsGhKhsk5AldHfVUlljewxWzJjY46Zslf++c8Y2vhN7N1"
    "xaIVXUnMt45ptz+WbI9+bKMbDtvbtxKMXu5g8f+7j5W+N7k6AVPBTqLxtNtF7HWhBQpNnc"
    "wQ4s1aetqeZRF+mUKU1ke5iJDOzprrWmlkPAZe7LgmbMfaknyXO/J7dN9iy0FfA2HJ25W2"
    "TBDIlv20zkE4sNrlJngekSu0zx+QsTW8TA37AXfV0/qqaFbSO1GsuAMblcpZs1l40JveaG"
    "8DZN1R3bX5HYeL2hS4dsrS1CQbrABLuIYhieuj4sCmYXghCtM5hpbBJMMeFjYBP5No3Xlk"
    "YmEuYx0B0CqLLZeHyBC3jLr0JbVMRuRxa7zITPZCtRXoLlxWsPHDkCd7PmC9cjigILDmOM"
    "29q1/sGqjb9iuwaAGa/XkYxw2wVlJIixjKNqJ5jNbYB1ld7cVzQRPjFS5r5ptvT23BdxB8"
    "FnqxWpAwdQgxxLLFI1WWRaXdHYcwd1S2J0L/sT70cyHe+x6znkzl/V2JlS/+PvUbIUiFhj"
    "GyJLSutwMEPtMB8TWQACDemPz8g11JzGEZwy27xqJayyEkTQgiMEK4LJhQX3HrnU0q01Ir"
    "SoHifVO8vxOjb0qlZjqaMLPA9wejsUuStGmyKJUhc+W6DtSNK5Vp9Kreb/55AbLpFbDF1k"
    "nwGPTfnQqZ+KrJ7RCeKrYuqv0DfWasiCLtlXqbUDwj/70+H7/vRCav0CYzssHYJcuQs1Al"
    "elK67OUqtGPEbmx6+nkgFtS+qYZXRqz63K8lT2z3DRM8njN3AcGyNSktNpzwyUGnPdF5bl"
    "PFUWgJuKggzAmkKyPlaDdwd2g8nkBgZZed6TzQXjWSZAP94ORtOLNo9bZmRRXAy67mKARE"
    "U0j/kV01BrhUsCN+WZwdwIXd9FDwcN5uoVlq3BmBB7ExbvHZjPxrejh1n/9j4F/FV/NgKN"
    "wKWbjPRCztSN7SCNv8az9w342vg0uRtxBB2PLlz+xthu9qkJc0I+dVTiPKvISPSZSBoBU4"
    "eRxBHgYt1xDa8g5ULH6w9TbCMObX6jQ5YxRaZp4ykf6vDNQEjxwFrpFUujENgrV4NzTiFL"
    "44rd/AxMqjMzrAADM9sogkYS4eTS1TTG1RRTxmceduZhb3NMDiIrYPhKz6x6BEvxsHarCh"
    "FjVqVMjOvSza3uNcT5AuLtWd2Tzw6UFt3U2Iaky+F2ov1agMPtAtuStm6e5B3DT9TRZUFs"
    "pfs67MAJ9/UUWAXtPQtmeZd3uaWa2MIq3T4JFevwDDzJPN+0nE6HP5+yfqJTVrK7JS5N1V"
    "rJkXc8Puf4bweptyYMwW9B9cBMuBwfxv/TvfbCGQrDNQ/vteNia0E+4A1HecwmhohedNIo"
    "/mnh9EO1jBtcQt993va7guRki2dLxsEt2rD/MOxfjZr5sH0LUKNxfpSQrQxqIkmL4TzO72"
    "d97Fr6soi1hZqdfA3FNq/xtPJ+eWZkB2dkX7HrheefqtcuCZcj37xURzF1xyJIUoU7FmZV"
    "esfCdel2DalRA8TQ/McEcC+XVOyNFBf1498fJndlvxluXTJAfiRsgZ8NS6eXDdvy6JfThH"
    "UHirDqFPmPwLu47f+dxXV4MxlkWT0MMDj2n2e8/AvQjH5h"
)
