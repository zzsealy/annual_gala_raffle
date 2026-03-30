from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `raffle_records` ADD `code` VARCHAR(50) NOT NULL COMMENT '工号';
        ALTER TABLE `raffle_records` ADD `name` VARCHAR(50) NOT NULL COMMENT '人员姓名';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `raffle_records` DROP COLUMN `code`;
        ALTER TABLE `raffle_records` DROP COLUMN `name`;"""


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
    "W03nyxVMpUubsUS9maUjdNSGfO5Sn2+RRLF4l4IGlyeT1weT1wzq8HLmLjfyQ2shObeRNt"
    "7HUqbjY8fZX0ukfSb3Fobui3QsKbeG99it0J+YgXgnKP3xgiVlESKv4Xg/OnW/bA/xo04v"
    "NKmxWsJz54PmQc1T+d1kOnddOtLk8jjFuYuta0WiCJY89WMYzSmJdEcHlOusjdo8vdH5gG"
    "8fu3XSVEpsmJVcTuFNe0g6woO4gHHlWqHoRvXT7A1tgDYhz+3wR4kPqAX5HhogPkj4dBv0"
    "zMrprkQH4mfIDfbNdi1xXPDdj388S6hSKMek1gJfCu7lp/57l2Pg3aeeUEHbSLzu1jHi/L"
    "fwGkp9RV"
)
