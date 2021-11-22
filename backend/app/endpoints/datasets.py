from datetime import date
from typing import Any, Optional

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

import cruds
from db import database
from definitions import GroupBy, OrderDir, SumBy

from utils import string_to_enums


api_router = APIRouter()


@api_router.get("/", response_class=StreamingResponse)
async def read_data_entries(
    *,
    db: Session = Depends(database.get_db),
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    channel: Optional[str] = None,
    country: Optional[str] = None,
    os: Optional[str] = None,
    group_by: Optional[str] = None,
    sum_by: Optional[str] = None,
    order_by: Optional[str] = "date",
    order_dir: Optional[OrderDir] = OrderDir.desc,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve many data entries, according to the given filter criteria.
    Note: the group_by and sum_by parameters accept a set of
    values (comma separated):
     e.g. group_by = date,channel
     e.g. sum_by = impressions,clicks
    """
    response = StreamingResponse(
        cruds.dataset.get_multi(
            db,
            date_from=date_from,
            date_to=date_to,
            order_by=order_by,
            group_by=string_to_enums(group_by, GroupBy),
            sum_by=string_to_enums(sum_by, SumBy),
            order_dir=order_dir,
            skip=skip,
            limit=limit,
            channel=channel,
            country=country,
            os=os,
        ),
        media_type="text/csv"
    )
    filename = "query_results" + str(date.today())
    response.headers["Content-Disposition"] = f"attachment; filename={filename}.csv"
    response.headers["charset"] = "utf-8"
    return response
