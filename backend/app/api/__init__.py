from fastapi import APIRouter
from .raffle_query import router as raffle_query_router
from .upload_person import router as upload_person_router
from .persons import router as persons_router
from .raffle import router as raffle_router

router = APIRouter()

router.include_router(raffle_query_router, prefix="", tags=["抽奖队列"])
router.include_router(upload_person_router, prefix="", tags=["上传人员"])
router.include_router(persons_router, prefix="", tags=["人员"])
router.include_router(raffle_router, prefix="", tags=["抽奖"])
