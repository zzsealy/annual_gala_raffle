import io

import pandas as pd

from app.models import Participant, ParticipantSpecial


NAME_COLUMN_INDEX = 5
DESK_COLUMN_INDEX = 10
POSITION_COLUMN_INDEX = 15
PARTICIPANT_REQUIRED_COLUMN_COUNT = 6
SPECIAL_REQUIRED_COLUMN_COUNT = 16
STAFF_DESK_LABEL = "工作人员"


def _normalize_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def _normalize_position(value) -> str:
    text = _normalize_text(value)
    if text in {"左", "右"}:
        return text
    return ""


def _format_desk_label(value, fallback_code: str) -> str:
    desk_text = _normalize_text(value)
    if not desk_text:
        return fallback_code
    if desk_text == STAFF_DESK_LABEL:
        return STAFF_DESK_LABEL
    if desk_text.endswith("桌"):
        return desk_text
    return f"{desk_text}桌"


def _read_excel(contents: bytes, required_column_count: int, error_message: str) -> pd.DataFrame:
    df = pd.read_excel(io.BytesIO(contents), engine="openpyxl")

    if df.shape[1] < required_column_count:
        raise ValueError(error_message)

    return df


def build_participants_from_excel(contents: bytes) -> list[Participant]:
    df = _read_excel(
        contents,
        PARTICIPANT_REQUIRED_COLUMN_COUNT,
        "Excel 列数不足，普通抽奖名单至少需要包含 A、F 列数据",
    )

    participants: list[Participant] = []

    for row_index in range(len(df)):
        employee_code = _normalize_text(df.iloc[row_index, 0])
        name = _normalize_text(df.iloc[row_index, NAME_COLUMN_INDEX])

        if not employee_code or not name:
            continue

        participants.append(
            Participant(
                code=employee_code,
                name=name,
            )
        )

    return participants


def build_special_participants_from_excel(contents: bytes) -> list[ParticipantSpecial]:
    df = _read_excel(
        contents,
        SPECIAL_REQUIRED_COLUMN_COUNT,
        "Excel 列数不足，特别大奖名单至少需要包含 A、F、K、L 列数据",
    )

    special_participants: list[ParticipantSpecial] = []

    for row_index in range(len(df)):
        employee_code = _normalize_text(df.iloc[row_index, 0])
        name = _normalize_text(df.iloc[row_index, NAME_COLUMN_INDEX])

        if not employee_code or not name:
            continue

        desk_label = _normalize_text(df.iloc[row_index, DESK_COLUMN_INDEX])
        position = _normalize_position(df.iloc[row_index, POSITION_COLUMN_INDEX])

        # 工作人员不分左右半场，但无论左边还是右边获胜都需要一起参与特别大奖抽取。
        if desk_label == STAFF_DESK_LABEL:
            position = STAFF_DESK_LABEL

        if not position:
            continue

        # 特别大奖场景展示的是桌号 + 姓名，因此这里把桌号整理成可直接展示的文案。
        special_participants.append(
            ParticipantSpecial(
                code=_format_desk_label(df.iloc[row_index, DESK_COLUMN_INDEX], employee_code),
                name=name,
                position=position,
            )
        )

    return special_participants