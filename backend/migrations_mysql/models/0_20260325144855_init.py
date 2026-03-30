from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `participants` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL COMMENT '人员姓名',
    `department` VARCHAR(100) COMMENT '所属部门',
    `is_active` BOOL NOT NULL COMMENT '是否参与抽奖' DEFAULT 1,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='参与抽奖的人员名单';
CREATE TABLE IF NOT EXISTS `prizes` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL COMMENT '奖品名称',
    `level` INT NOT NULL COMMENT '奖项等级，1为一等奖，以此类推',
    `quantity` INT NOT NULL COMMENT '奖品数量' DEFAULT 1
) CHARACTER SET utf8mb4 COMMENT='年会奖品设置';
CREATE TABLE IF NOT EXISTS `raffle_records` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `participant_id` INT NOT NULL COMMENT '中奖人',
    `prize_id` INT NOT NULL COMMENT '所中奖品',
    CONSTRAINT `fk_raffle_r_particip_1106caf6` FOREIGN KEY (`participant_id`) REFERENCES `participants` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_raffle_r_prizes_603abb0d` FOREIGN KEY (`prize_id`) REFERENCES `prizes` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='中奖记录';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmW1z2jgQgP8Kw6fcTK4DBttw34CQKdcmdAhtb1o6HtlegybGJraclHby308rY/yCTU"
    "xKCL3jC+B9kaVHK+1K/KzOXRNs/80H4jFq0AVxWPWvys+qQ+bAf+SpzytVsljEShQwotvC"
    "fhEbCgXRfeYRAxu1iO0DF5ngGx5dMOo66DEJ5IYhTYIm1GASKJJucklbViaBqrSaKNcJlz"
    "TlFn7WUNuQZWzbdA3eOHWmvBknsG0uChx6F4DG3CmwGXhc8fUbF1PHhO/gR4+LW82iYJup"
    "kVIT2xRyjS0XQjZw2KUwxLfpmuHawdyJjRdLNnOdtTUN4UzBAY8wwOaZF+CQsXcrQhGFsK"
    "exSdjFhI8JFglsFo8tzS0SbjIwXAeZU5wBHOAU3/KnVG+qzVZDaba4iejJWqI+hsOLxx46"
    "CgLX4+qj0BNGQguBMeYmvjfI9WbEy0cX2Wfg8S5n4UWottGLBDG+OMy28qtmIqttNsL4Ko"
    "isLNU5+a7Z4EzZjD/KtS0IP3VGvbed0Zlc+wPbdvlyCNfK9UojCRVSjqmagCtpDmFIlWWb"
    "9noW4VX07QWwIjVrHKoh84XdrgHH3Jah9RzA9VoZwtyqELHQpRlTX+M7E73PCd+u69pAnI"
    "LFn/TLQNa540vF8XpjyGJWJAtjV1KK9tJyyLcQ7g6H77GRue/f2UIwGGdIf7zq9vkUiAng"
    "RpRBcv+IqRseIBeN5ET2BdcwOod87mnPDHhz5fom+nHQ3aT8bszHYA4de7mazy3Mx4Or/s"
    "24c/UhBf6iM+6jRhLSZUZ6pmQWwLqRyufB+G0FHytfhtd9QdD12dQTb4ztxl+q2CcSMFdz"
    "3AeNmImcFEkjMI+YTa3bRF5AgU6M2wfimVpKE0eAB4brmX7Oqls5Xr4bgU0E2s2JXlUkI2"
    "JZNoxEU4dPHNK6SMEkstPyiqVRCCAzV3KLKG6q5tI8KyEOmYpR4LvxTVHh5tEfkFvRCcX2"
    "Wg5NyldxoGK1ZtVJhEZuGvVJ0NJ1vheplgKnmu1Us/3q0ktGVngaUNtW7WhKChvuwd4hJt"
    "f2T4flYci2W2qbM9Wb+AlEnQSWVUPYTWgQUVjUInXogGqUg8wLDl3hW4BqqDr/3SBlK729"
    "BHs8B3cBP3xSttxhGpIuh5uJ+lMBrsgqp92uG9bhSP4/M3p4UknmdZyBI87rKVg56T0Lsz"
    "jLe8JSS0xhmWyfRMUzPB7zrNOtzPFk+NMp6z90ykpmt8QFq7bT4th0fP2a43kHqX0XDOKc"
    "syPMhMvrY/yV7PUiNUNuuG7ivXQ9oFPnHSwF5QHvGHGMvJNG/t8Qxx+qRbXBOebdh3W+y1"
    "mcfPB8yBDeovU6N73ORb+6Gbb7gBq187uEbGmoiUWaj7O4tn3J2q0DHjVmeVXbSrO1XiOx"
    "zVN1WnG+PFVkB6/I7sHzV+efstcuCZdXvnkpTzF1xyLJcok7Fm5VeMcidOl0jUtjB4gr89"
    "8T4ItcUvE3stw/Fv++GV4XHApilwzIjw4f4FeTGuy8YlOffTtOrFso4qhTxX8E7+yq80+W"
    "a+/9sJut6rGB7m5XJ/tPL4//AtfayDY="
)
