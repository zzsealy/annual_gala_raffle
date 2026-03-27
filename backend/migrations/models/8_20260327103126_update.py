from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `raffle_records` DROP FOREIGN KEY `fk_raffle_r_prizes_603abb0d`;
        ALTER TABLE `raffle_records` ADD `desc` VARCHAR(100) NOT NULL COMMENT '抽奖描述';
        ALTER TABLE `raffle_records` DROP COLUMN `prize_id`;
        DROP TABLE IF EXISTS `prizes`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `raffle_records` ADD `prize_id` INT NOT NULL COMMENT '所中奖品';
        ALTER TABLE `raffle_records` DROP COLUMN `desc`;
        ALTER TABLE `raffle_records` ADD CONSTRAINT `fk_raffle_r_prizes_603abb0d` FOREIGN KEY (`prize_id`) REFERENCES `prizes` (`id`) ON DELETE CASCADE;"""


MODELS_STATE = (
    "eJztmm1z2jgQx78Kw6t0JtcxBj9w74CQKdcGcoT2blo6HtmWwRMjE1luynX47qeVbWyMTS"
    "ATHu6GNwR2V7L1k7T6r51f1ZlvYy94f48ocy13jgir/l75VSVohvmXIvd1pYrm89QJBoZM"
    "T8TP00DhQGbAKLKgUwd5AeYmGwcWdefM9Qm0GIdK3ZLHYQNLeByqsmlzS1NRx6Gm6g2wm4"
    "hbGooOnxJ464oCfdu+xTt3yYR3Q0LP46aQuE8hNpg/wWyKKXd8+87NLrHxTxwkP+ePhuNi"
    "z14bqWtDn8JusMVc2HqE3YpAuJppWL4XzkgaPF+wqU9W0W4EZ4IJpohh6J7REIYMdxcTSi"
    "hEd5qGRLeYaWNjB4UeS8e2zi0xbjKwfALMXZgBGOAErvKbXGtoDb2uNnQeIu5kZdGW0fDS"
    "sUcNBYH+qLoUfsRQFCEwptzE3w1ynSmixeiS+Bw8fst5eAmqbfQSQ4ovXWZb+VVzK6tp16"
    "P1VbKy8lRn6KfhYTJhU/5TkbYg/NIadj60hleK9A769vl2iPZKP/bIwgWUU6oW31r7UE3i"
    "T09VsbECe9TRzoOkGxg2Rc9kk2bb9z2MSMkOzzTLQTV5u0NRLU2Sqio7sEBlFRA7cjZV7g"
    "Z6C9j2YPAJOpkFwZMnDL1RjvDnu3Z3eFUT4HmQy3A2PWQWLsWAxEBsE/gN9zB3hkuW8FrL"
    "HHM7bvo++XLUZb17suVjsAfEW8R5fAvzUe+u+zBq3d2vgb9pjbrgkYV1kbNeqbmFv+qk8l"
    "dv9KECPytfB/2uIOgHbELFFdO40dcq3BMKmW8Q/9lAdubISawJmCUcls5jJu2DwUTW4zOi"
    "trHmSVcAxZZP7aBgv8UNbz8OsYcE2s2JjgXHEDmOh4eiq+OfC/JKg8AZsdf2Sq3JEgBmvu"
    "yXUdx0zeRZ3oIImohRwLXhSmuY/gyxGPSGbMu6t8o2KgKNp1XkDrItK9Waag2yk1wrS/oX"
    "YXZ0YTan7j+Yn6w/sLcHwFyrl0keXE9EC0zXmrwiMBvwiZE2Dh1HsmqwQetIFA9S4o4agB"
    "vsIEZUU+WFhGZpJv9eRxw0BMtpj7sfom8zaZlkme7Qe0wDn/TD2R6zVdb89NOWzQ6R0FYV"
    "TToNZLi5fcR0En96MZ2lqNYtnmN1vrBfI6xr0i7KmkeVSmvhy2nr2cQIaUF6KWebafIqvH"
    "ESfpvUojoYEkGDpxOdh3OLA48cotyhKbIOa1fHcLI1+DxoSMRYCs8pWrO+ozA4wjxwkYTp"
    "HmljFX8GeaLe5LWMgnUn4a7bOpTlluQk35uaKkVzcJr8cSkhLyXkpYQ8eAl5+EIpridLK6"
    "W03nyxVMpUubsUS9maUjdNSGfO5Sn2+RRLF4l4IGlySeb/o2SendjMmz5jr6yz2fD0KvR1"
    "j/zeIiltnI+FhDfx3voUuxPyES8E5R6/MUSsondAxa9wz59u2QPVaziDn1dnX8F64oPnQ8"
    "aRvuy0Hjqtm251eRrh0cLUtaZFkiP2bBUbKI15SWSU56SLnDi6nPiBaRC/39hVUWSanFhU"
    "7E5xTT7IirKDfOBRpfJB+NblA2yNPSDG4f9NgIfRXz5huOgA+eNh0C/7X4JVkxzIz4QP8J"
    "vtWuy64rkB+36eWLdQhFGvCawE3tVd6+88186nQTuvnKCDdtG5fczjZfkvNUgBRw=="
)
