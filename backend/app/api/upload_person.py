import io

import pandas as pd
from fastapi import APIRouter, UploadFile, File
from app.models import Participant

router = APIRouter()

@router.post("/upload_person")
async def upload_person(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_excel(io.BytesIO(contents), engine='openpyxl')
    participant_list = []
    for val_a, val_f in zip(df.iloc[:, 0], df.iloc[:, 5]):
        participant_list.append(Participant(
            code=str(val_a),
            name=str(val_f)
        ))
    await Participant.bulk_create(participant_list)

    return {"message": "success"}