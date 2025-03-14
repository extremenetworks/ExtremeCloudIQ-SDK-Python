# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.2.0.123
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from extremecloudiq import schemas  # noqa: F401


class XiqDeliverySettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The password delivery settings
    """


    class MetaOapg:
        
        class properties:
            email_template_id = schemas.Int64Schema
            sms_template_id = schemas.Int64Schema
            __annotations__ = {
                "email_template_id": email_template_id,
                "sms_template_id": sms_template_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_template_id"]) -> MetaOapg.properties.email_template_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sms_template_id"]) -> MetaOapg.properties.sms_template_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_template_id", "sms_template_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_template_id"]) -> typing.Union[MetaOapg.properties.email_template_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sms_template_id"]) -> typing.Union[MetaOapg.properties.sms_template_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_template_id", "sms_template_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        email_template_id: typing.Union[MetaOapg.properties.email_template_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sms_template_id: typing.Union[MetaOapg.properties.sms_template_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeliverySettings':
        return super().__new__(
            cls,
            *_args,
            email_template_id=email_template_id,
            sms_template_id=sms_template_id,
            _configuration=_configuration,
            **kwargs,
        )
