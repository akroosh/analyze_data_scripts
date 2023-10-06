from pydantic import BaseModel, AnyUrl, EmailStr, field_validator
from datetime import datetime
from pydantic_extra_types.country import CountryAlpha2
from typing import Any
from iso639 import languages


class SchemaValidator(BaseModel):
    package_name: str
    market_status: str
    category: str
    cat_key: str
    cat_keys: list[str]
    cat_type: int
    title: str
    description: str
    short_desc: str
    icon: AnyUrl
    icon_72: AnyUrl
    market_url: AnyUrl
    what_is_new: str
    downloads: str
    downloads_min: int
    downloads_min: int
    market_update: datetime
    created: datetime
    promo_video: AnyUrl
    promo_video_image: AnyUrl
    rating: float
    size: int
    screenshots: list[AnyUrl]
    version: str
    website: AnyUrl
    privacy_policy: AnyUrl
    developer: str
    content_rating: str
    number_ratings: int
    ratings_1: int
    ratings_2: int
    ratings_3: int
    ratings_4: int
    ratings_5: int
    price_currency: str
    price_numeric: float
    price: str
    price_i18n_countries: list[CountryAlpha2]
    iap: bool
    iap_min: float
    iap_max: float
    i18n_lang: list[str] #??
    similar: list[str]
    from_developer: list[str]
    badges: list[str]
    interactive_elements: list[str]
    content_descriptors: list[str]
    contains_ads: bool
    age_approved_by_teachers: str
    price_i18n: dict[str, Any]
    i18n: dict[str, Any]
    app_availability: dict[str, Any]
    permissions: list
    sdks: list
    physical_address: str
    email: EmailStr
    stores: dict[str, Any]

    @field_validator('i18n_lang')
    @classmethod
    def validate_languages_i18(cls, languages_i18_list: list[str]) -> list[str]:
        all_languages_codes = [lang.alpha2 for lang in languages.languages if lang.alpha2]
        incorrect_languages = []

        for language in languages_i18_list:
            codes = language.split('-')
            if any(code not in all_languages_codes for code in codes):
                incorrect_languages.append(language)

        if incorrect_languages:
            raise ValueError({"incorrect_languages": incorrect_languages})

        return languages_i18_list
