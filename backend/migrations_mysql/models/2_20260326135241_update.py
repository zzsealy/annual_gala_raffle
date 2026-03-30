from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `lottery_queue` ADD `img_url` VARCHAR(100) COMMENT '图片路径，用于前端展示';
        ALTER TABLE `lottery_queue` ADD `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `lottery_queue` ADD `desc` VARCHAR(100) NOT NULL COMMENT '抽奖描述';
        ALTER TABLE `lottery_queue` MODIFY COLUMN `prize_level` INT NOT NULL COMMENT '奖项等级，1为一等奖，以此类推, 0特等奖';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `lottery_queue` DROP COLUMN `img_url`;
        ALTER TABLE `lottery_queue` DROP COLUMN `created_at`;
        ALTER TABLE `lottery_queue` DROP COLUMN `desc`;
        ALTER TABLE `lottery_queue` MODIFY COLUMN `prize_level` INT NOT NULL COMMENT '奖项等级，1为一等奖，以此类推';"""


MODELS_STATE = (
    "eJztWm1z2jgQ/isMn3IzuQ4Yv8B9gzSZ5pqElNC7m5aOR7Zl4omRiSw35Tr576eVbfxO7F"
    "wItGWmQ82+COnZlfbROt/bC8/Crv/mwmMM09WHAAe4/Ufre5ugBTyU6o9bbbRcJloQMGS4"
    "wsENLfX7tanhM4pMxpU2cn3MRRb2TeosmeMRcJkFqmRYs0AZKOosGKhdmz9LXQ28Lc/k7g"
    "6Zc0MSuC4XBcThg+vMm2N2iylXfP7CxQ6x8Dfsx1+Xd7rtYNfKrMaxYEwh19lqKWTnhJ0J"
    "Q/g1Qzc9N1iQxHi5YrceWVs7hIF0jgmmiGEYntEAFgWzi0CI1xnONDEJp5jysbCNApcla8"
    "siEwuLGJgeAVT5bHyxwDn8yu9SV9bkfk+V+9xEzGQt0R7D5SVrDx0FAlfT9qPQI4ZCCwFj"
    "gtuSOv9i3cVfsdsAwJzX00jGuG2CMhYkWCZZtRHM9jrB+tpgFmiGDJ8YabPAtjtmdxbIuI"
    "fgs9OJ1aEDqEGOFZ6phipzrakZ/LmHONBgLCUjgktF4m4laEmQ0nv0GlPfI1fBokG4Kv13"
    "H7j0+SBjg0dJVbTObmCGyRVRPblFtBzW2D6HIp/iLlFUeyY/Zfs8tWuiuEDf+FYmc3bLv3"
    "Y7nQ2Y/TWcnLwbTo641W8wuseP/7A4XEUqKdRlgXUWcz2gJQdMNbYpl2fBGx3DL3O4qDaG"
    "o0DmB0qfm3OJ3Zfj00NTpD7kbh9DbZN5HDQkbEyFnyraoIf2Jg4mxYCYjlgxFG+5hjkLXB"
    "6OrGcuIlbk+iZ+eNX0r19K+RqsMXFXUXpswHd6fnl6Mx1eXsNKFr5/7wqIhtNT0EhCuspJ"
    "j9RcKNaDtP4+n75rwdfWp/HVqUDQ89mcil9M7Kaf2jAnFDBPJ96DjqwUoYilMTCPQIXsu1"
    "RRB4GBzLsHRC29oPEkr8q2qFpIi7wEETQXYQFwYZoRf7xGlDmms0SEldHLtHoju1wmhn5d"
    "cqn0TEmUdZw9AjUVtmdYThRZ6cNnB7Q9RTlQz32hnuL/BiUhtt99uc1k1sDqhfn1nGNeqX"
    "PKK9WHvFI84/nWapCPsfnumaBiAQtXenbV7XDL7M/xdf7PouiBFPEbeZ6LEanY01nPHJQG"
    "d90WltXXblUCCiJLKgBrS+nzsR68G7AbjccXmcI4Op/mEvTj5eiU0xORt9zIYbgc9AMj+T"
    "UZSZIBFJsetfySLRc5nr2fYBcJaIuBjljGBNm2iydiqNcvBlLmBttoeyXSOAW2ytWgbVPK"
    "0oRiMz8Dk/rMDGvAwOwuiqFRZGjE9A0DrlK2ig887MDDXqbrF2ZWyPC1wR61PZp2VX/ufu"
    "puWN19wC+UDls1CEPa5fUi0X0qwaEvykPSNe3XQ/LXrOiqJHeydR0isMd1PQNWSXnPg1ld"
    "5amw1FMhrFPt01DxCt+BBumh07I/Ff5wy/qJblnp6pZqmuqNNkfRcfec43kXqZcmDOGr7W"
    "Zgplx2D+P/qV5b4Qyl6VqE98yj2JmT93glUD7nE0PELLtplL9a2P9UreIGx1B3H9b1rmRz"
    "8sXzJeOwi3YyvDkZvj1tF9P2JUCNx/lRUrY2qKlNWg7nbt6fDTF1zNsy1hZpNvI1lNg8xd"
    "Oq6+WBkb06I/uKqR/df+q2XVIuO+681Ecx02ORFKVGj4VbVfZYhC5brmFrNAAxMv8xAdzO"
    "34R4hOGyevznzfiq6p3h2iUH5EfCF/jZckx23HIdn33ZT1g3oAirzpD/GLyjy+E/eVxPLs"
    "ajPKuHAUbNWicvX14e/wOU9QOL"
)
