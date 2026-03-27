from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `lottery_queue` ADD `is_drawn` BOOL NOT NULL COMMENT '是否已抽奖' DEFAULT 0;
        ALTER TABLE `participants` RENAME COLUMN `is_is_drawn` TO `is_drawn`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `participants` RENAME COLUMN `is_drawn` TO `is_is_drawn`;
        ALTER TABLE `lottery_queue` DROP COLUMN `is_drawn`;"""


MODELS_STATE = (
    "eJztWtty2kgQ/RWKJ6fKmwKhG/uGbxVvbOO1SXYrIaUaSSOsshhhaRSHTfnft3uE0AUJS1"
    "7b4CwvWPRlmDnT032m5Z/tqW9TL3x/5nNOg/mfEY1o+/fWzzYjU3wo1e+32mQ2S7Uo4MT0"
    "hIMXWxp3S1Mz5AGxOCgd4oUURDYNrcCdcddn6DKOVMm0x5HSV9Rx1Fe7DjxLXQ29bd8Cd5"
    "dNwJBFngeiiLkwuMH9CeU3NADF128gdplNf9Aw+Tq7NRyXenZuNa6NYwq5weczITtl/EQY"
    "4q+ZhuV70ZSlxrM5v/HZ0tplHKUTymhAOMXheRDhonB2CxCSdcYzTU3iKWZ8bOqQyOPp2v"
    "LIJMJVDCyfIaowm1AscIK/8pvUlTVZ76myDiZiJkuJ9hAvL1177CgQuBi1H4SecBJbCBhT"
    "3GaB+w81PPqdeg0ALHg9jmSC2zooE0GKZRpVa8FsLwNM1/rjSDNl/KREG0eO07G640imPY"
    "KfnU6ijh1QjXKqQKSaqgxaSzPhuUcAaDSW0hHRpSJwX2TT0k3KntFLGoQ+u4imDbar0n/z"
    "G5fNDzI1YZdURetsBmac3CqqhzckKIc1sS+gCFPcJIpqz4Isq0No10RxSn7AUWYTfgNfu5"
    "3OGsw+D64OPwyu9sDqHY7uQ/qPi8PFQiXFujyw7nRiREFJgqnGNuPyJHgXafh5kovqUEwF"
    "MiQUHcxB4uhykj00RdIxdnWKtU2GfdCIsLEUyCpav0e2Zh/8wKZBg7yxtN+CPNHrS4Ap1Z"
    "0Ed93WCaLccZLnvqZ24j3YTP5wQ8MOyD1bRfjA9z1KWEWoZ9wKQJvg91JIV1M2VcLwlSVI"
    "JortSNn0Ug/YNagdDIdnOMg0DO88ITgdFSL40/nBMYS2CGwwcjkth9sKKEJiEL4K+BFouD"
    "ul5YjnPQuY2wvX98nDq4Z6fWIIa7CHzJsvkt0azEen58fXo8H5ZQ74o8HoGDWSkM4L0j21"
    "kFiWg7T+Oh19aOHX1pfhxbFA0A/5JBC/mNqNvrRxTiTivsH8e4PYGXqcSBNgHpDYO7cZio"
    "oCk1i39ySwjRWNL/lVtquqqTQtSggjE7EtCC5Oc3EbuiQBdy13Rhhvl1yWsuq1d6VZahjW"
    "vSopPUsSJJXmC7qmYrGJyZEiKzp+dlDbU5TdRWpbLlLibwOCk9hvnjzmIqtv9+L4egppUe"
    "pwFqWasigrjMWCo9UgHhPzzfMVxcY7pdJzqnodOy6y4yI7LvLWuUgaAQG14LoUlpy3hePJ"
    "xyvqEQHt6kYv+MUVcRyPXomhXr8MSLlOTKPjlUqTEHhRlobtx1J+JhTrmRma1OdkVEPu5X"
    "RJAo0iY0NRN01sCTgq3TGwHQN7nu51HFkxt9f6W9S+a/p24Nd+L7AZPncXwVXS5fMG25B1"
    "eb2d6D4W4Njfhy3pWs7rIfn/rOiqJHfydR13YIvreg6skvJeBLO6ygfC0shsYZ1qn4UKKj"
    "w2k51dj2V7KvzulvUL3bKy1S3TLjUaHY5Vx81zjqddpJ6bMMT/otEMzIzL5mH8L9XrRThD"
    "abiuwnviB9SdsI90LlA+hYkRZpXdNMpfKmx/qFZxg32su/fLeldyOGHxsGQad9EOB9eHg6"
    "Pj9mrYPgeoyThvJWRrg5o5pOVwbubN2YAGrnVTxtoWmrV8jaQ2j/G06nq5Y2Svzsi+0yBc"
    "3H/qtl0yLhvuvNRHMddjkRSlRo8FrCp7LEKXL9d4NBqAuDB/mwC+SJMKfpHTsnr8x/Xwou"
    "pt4dKlAOQnBgv8arsW3295bsi/bSesa1DEVefIfwLe3vng7yKuh2fDgyKrxwEOmrVOnr+8"
    "PPwL/KXiEg=="
)
