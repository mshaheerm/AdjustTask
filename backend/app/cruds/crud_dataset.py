from datetime import date
import json
import logging
from typing import Iterable, Iterator
from fastapi.encoders import jsonable_encoder

from sqlalchemy import asc, desc, func
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import label

import models
from definitions import GroupBy, OrderDir, SumBy


logger = logging.getLogger(__name__)


class CRUDDataSet:
    def __init__(self, model: models.DataSet):
        """
        Provides operations on events

        **Parameters**
        * `model`: A SQLAlchemy model class
        """
        self.model = model
    
    def get_multi(
        self,
        db: Session,
        *,
        date_from: date,
        date_to: date,
        order_by: str = "date",
        group_by: Iterable[GroupBy],
        sum_by: Iterable[SumBy],
        order_dir: OrderDir = OrderDir.desc,
        skip: int = 0,
        limit: int = 100,
        **params,
    ) -> Iterator[str]:
        """
        Read multiple data entries according to the given criteria.
        Note: the group_by and sum_by parameters accept multiple values (comma separated)
        """
        # filter out the empty params
        criteria = {name: value for name, value in params.items() if value is not None}
        group_by_cols = tuple(getattr(self.model, col_name.name) for col_name in group_by)
        total_data = (
            db.query(
                *group_by_cols,
                label('cpi', self.model.spend / self.model.installs),
                *(
                    func.sum(
                        getattr(self.model, col_name.name).label(col_name.name)
                    ) for col_name in sum_by
                )
            )
        )
        if date_from is not None:  # filter only if date_from is present
            total_data = (
                total_data
                .filter(self.model.date>=date_from)
            )
        if date_to is not None:  # filter only if date_to is present
            total_data = (
                total_data
                .filter(self.model.date<=date_to)
            )
        total_data = (
            total_data
            .filter_by(**criteria)
            .group_by(*group_by_cols)
            .order_by(asc(order_by) if order_dir is OrderDir.asc else desc(order_by))
        )
        total_data = total_data.offset(skip).limit(limit).all()
        # the header of the CSV
        yield ",".join(g.name for g in group_by) + ",cpi," + ",".join(s.name for s in sum_by) + "\n"
        
        for record in total_data:  # the records in the CSV
            yield ",".join(
                str(col) for col in record
            ) + "\n"


dataset = CRUDDataSet(models.DataSet)
