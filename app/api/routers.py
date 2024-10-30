from fastapi import APIRouter, Depends
from src.dependencies.dependencies import get_code_review_service
from src.domain.services.abstract_code_review_service import AbstractCodeReviewService
from src.schemes.code_review_schemes import RequestCodeReview

router = APIRouter(prefix="/code_review", tags=["code_review"])


@router.post("/review")
async def review_code(request: RequestCodeReview, service: AbstractCodeReviewService = Depends(get_code_review_service)):
    result = await service.review_code(request)
    return {"review": result}
