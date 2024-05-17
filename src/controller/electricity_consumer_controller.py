from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Path

from ..repository.electricity_reading_repository import ElectricityReadingRepository
from ..service.electricity_reading_service import ElectricityReadingService
from .models import OPENAPI_EXAMPLES, Readings

repository = ElectricityReadingRepository()
service = ElectricityReadingService(repository)

router = APIRouter(prefix="/consumers", tags=["Consumers"])


@router.get("/{smart_meter_id}", response_model=Readings, description="")
def electricity_consumer(smart_meter_id: str = Path(openapi_examples=OPENAPI_EXAMPLES)):
    readings = service.retrieve_readings_for(smart_meter_id)
    # com base no timestamp, filtrar o retorno da ultima semana
    last = max([r.time for r in readings])
    readings = list(filter(lambda r: r.time == last, readings))

    if len(readings) < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="No readings found")
    else:
        return readings[0].to_json()
