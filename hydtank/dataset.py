import copy
from datetime import datetime
from typing import List

import pandas as pd

from .columns_constants import TIME_SERIES, PRECIPITATION, EVAPOTRANSPIRATION, DISCHARGE


class Dataset:
    def __init__(self, time_series: List[datetime], precipitation: List[float],
                 evapotranspiration: List[float],
                 discharge: List[float]):
        self._time_series = time_series
        self._precipitation = precipitation
        self._evapotranspiration = evapotranspiration
        self._discharge = discharge

    def to_dataframe(self):
        dataset_dict = {
            TIME_SERIES: self._time_series,
            PRECIPITATION: self._precipitation,
            EVAPOTRANSPIRATION: self._evapotranspiration,
            DISCHARGE: self._discharge
        }

        df = pd.DataFrame(dataset_dict)
        df[TIME_SERIES] = pd.to_datetime(df[TIME_SERIES])
        return df

    def copy(self):
        return copy.deepcopy(self)