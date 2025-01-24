# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.1.0.147
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


class XiqPostExpirationAction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The type of action to take after the account expiration.
    """


    class MetaOapg:
        
        class properties:
            enable_credentials_renewal = schemas.BoolSchema
            enable_delete_immediately = schemas.BoolSchema
            delete_after_value = schemas.Int32Schema
        
            @staticmethod
            def delete_after_unit() -> typing.Type['XiqDateTimeUnitType']:
                return XiqDateTimeUnitType
            __annotations__ = {
                "enable_credentials_renewal": enable_credentials_renewal,
                "enable_delete_immediately": enable_delete_immediately,
                "delete_after_value": delete_after_value,
                "delete_after_unit": delete_after_unit,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_credentials_renewal"]) -> MetaOapg.properties.enable_credentials_renewal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_delete_immediately"]) -> MetaOapg.properties.enable_delete_immediately: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_after_value"]) -> MetaOapg.properties.delete_after_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delete_after_unit"]) -> 'XiqDateTimeUnitType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enable_credentials_renewal", "enable_delete_immediately", "delete_after_value", "delete_after_unit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_credentials_renewal"]) -> typing.Union[MetaOapg.properties.enable_credentials_renewal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_delete_immediately"]) -> typing.Union[MetaOapg.properties.enable_delete_immediately, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_after_value"]) -> typing.Union[MetaOapg.properties.delete_after_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delete_after_unit"]) -> typing.Union['XiqDateTimeUnitType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enable_credentials_renewal", "enable_delete_immediately", "delete_after_value", "delete_after_unit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_credentials_renewal: typing.Union[MetaOapg.properties.enable_credentials_renewal, bool, schemas.Unset] = schemas.unset,
        enable_delete_immediately: typing.Union[MetaOapg.properties.enable_delete_immediately, bool, schemas.Unset] = schemas.unset,
        delete_after_value: typing.Union[MetaOapg.properties.delete_after_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        delete_after_unit: typing.Union['XiqDateTimeUnitType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqPostExpirationAction':
        return super().__new__(
            cls,
            *_args,
            enable_credentials_renewal=enable_credentials_renewal,
            enable_delete_immediately=enable_delete_immediately,
            delete_after_value=delete_after_value,
            delete_after_unit=delete_after_unit,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_date_time_unit_type import XiqDateTimeUnitType
