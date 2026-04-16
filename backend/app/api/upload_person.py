from fastapi import APIRouter, File, HTTPException, UploadFile

from app.models import Participant, ParticipantSpecial
from app.participant_import import (
    build_participants_from_excel,
    build_special_participants_from_excel,
)

router = APIRouter()

@router.post("/upload_person")
async def upload_person(file: UploadFile = File(...)):
    contents = await file.read()

    try:
        participant_list = build_participants_from_excel(contents)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    # 普通上传接口只负责普通抽奖名单，避免覆盖特别大奖单独上传的数据。
    await Participant.all().delete()

    if participant_list:
        await Participant.bulk_create(participant_list)

    return {"message": "success"}


@router.post("/upload_special_person")
async def upload_special_person(file: UploadFile = File(...)):
    contents = await file.read()

    try:
        special_participant_list = build_special_participants_from_excel(contents)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    # 特别大奖名单独立维护，避免与普通抽奖名单互相覆盖。
    await ParticipantSpecial.all().delete()

    if special_participant_list:
        await ParticipantSpecial.bulk_create(special_participant_list)

    return {
        "message": "success",
        "special_participant_count": len(special_participant_list),
    }