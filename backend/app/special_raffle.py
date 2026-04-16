SPECIAL_PRIZE_LEVEL = -1
SPECIAL_PRIZE_NAME = "特别大奖"
SPECIAL_PRIZE_DISPLAY_NAME = "华为折叠屏手机"
SPECIAL_PRIZE_IMAGE = "/raffle/special_big_gift.png"
SPECIAL_STAFF_POSITION = "工作人员"


def normalize_special_position(position: str | None) -> str:
    if position is None:
        return ""
    text = str(position).strip()
    if text in {"左", "右"}:
        return text
    return ""


def is_special_prize_level(prize_level: int) -> bool:
    return prize_level == SPECIAL_PRIZE_LEVEL


def build_special_desc(position: str) -> str:
    normalized_position = normalize_special_position(position)
    if not normalized_position:
        raise ValueError("特别大奖必须指定左或右半场")
    return f"{SPECIAL_PRIZE_NAME}({normalized_position}半场)"


def extract_special_position(desc: str) -> str:
    if "左" in desc:
        return "左"
    if "右" in desc:
        return "右"
    return ""


def get_special_pool_positions(position: str) -> list[str]:
    normalized_position = normalize_special_position(position)
    if not normalized_position:
        return [SPECIAL_STAFF_POSITION]
    return [normalized_position, SPECIAL_STAFF_POSITION]