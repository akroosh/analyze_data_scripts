from collections import defaultdict
from datetime import date
from app.downloads.loggers import logger

from pydantic import BaseModel, model_validator
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

    @classmethod
    def _get_values_by_countries(cls, estimates: list[dict[str, list]]) -> dict[str, int]:
        values_by_countries = defaultdict(lambda: 0)

        for estimate in estimates:
            for country_estimate in estimate["countries"]:
                value = country_estimate.get("value")
                country = country_estimate.get("country")

                if value is None:
                    logger.error({
                        "type_error": "missing",
                        "field": "estimates",
                        "td": estimate["td"],
                        "country": country,

                    })
                else:
                    values_by_countries[country] += value

        return values_by_countries

    @model_validator(mode="before")
    @classmethod
    def validate_estimates_agg(cls, values):
        values_by_countries = cls._get_values_by_countries(values["estimates"])
        for country, actual_value in values_by_countries.items():
            expected_value = values["estimates_agg"].get(country, 0)
            if expected_value != actual_value:
                logger.error({
                    "type_error": "incorrect",
                    "field": "estimates_agg",
                    "country": country,
                    "expected_value": expected_value,
                    "actual_value": actual_value,
                    "message": "Expected and actual values do not match",

                })
        return values

    @model_validator(mode="before")
    @classmethod
    def _validate_estimates_total(cls, values):
        try:
            actual_value = sum(values["estimates_agg"].values())
        except TypeError:
            return values

        expected_value = int(values["estimates_total"].replace(",", ""))
        if expected_value != actual_value:
            logger.error(
                {
                    "type_error": "incorrect",
                    "field": "estimates_total",
                    "expected_value": expected_value,
                    "actual_value": actual_value,
                    "message": "Sum of estimates agg don't match",
                }

            )

        return values
