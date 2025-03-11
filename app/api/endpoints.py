from fastapi import APIRouter
from services import get_summary
from pydantic import BaseModel
from helpers import constants

router = APIRouter()
    

class VideoRequest(BaseModel):
    video_id: str
    user_input: str = constants.DEFAULT_USER_INPUT


@router.get("/")
def read_root():
    return {
        "app": "Youtube video summarizer",
        "author": "Vinayaka D",
        "email": "vinayakadayanand007@@gmail.com",
    }


@router.post("/get-summary")
def get_video_summary(request: VideoRequest):
    summarized_transcript = get_summary(request.video_id, request.user_input)
    return {"video_id": request.video_id, "summary": summarized_transcript}
