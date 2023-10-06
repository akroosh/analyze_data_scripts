from datetime import date

from pydantic import BaseModel
from typing import Any


class RegionModel(BaseModel):
    code: str
    name: str


class CountryModel(BaseModel):
    cc: str
    name: str
    region: RegionModel


class EstimateCountryModel(BaseModel):
    country: str
    value: int


class EstimateModel(BaseModel):
    td: date
    countries: list[EstimateCountryModel]


class DownloadsSchema(BaseModel):
    estimates: list[EstimateModel]
    estimates_agg: dict[str, int]
    estimates_total: str
    regions: dict[str, Any]
    countries: list[CountryModel]
    package_name: str
