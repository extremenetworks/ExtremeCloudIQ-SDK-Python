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


class XiqAfcApDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PENDING": "PENDING",
                        "GRACE_PERIOD": "GRACE_PERIOD",
                        "AVAILABLE": "AVAILABLE",
                        "NA": "NA",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
                
                @schemas.classproperty
                def GRACE_PERIOD(cls):
                    return cls("GRACE_PERIOD")
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("AVAILABLE")
                
                @schemas.classproperty
                def NA(cls):
                    return cls("NA")
            expire = schemas.Int64Schema
            received = schemas.Int64Schema
            reason = schemas.StrSchema
        
            @staticmethod
            def spectrum() -> typing.Type['XiqAfcAvailableSpectrum']:
                return XiqAfcAvailableSpectrum
            band_width = schemas.Int64Schema
            __annotations__ = {
                "status": status,
                "expire": expire,
                "received": received,
                "reason": reason,
                "spectrum": spectrum,
                "band_width": band_width,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expire"]) -> MetaOapg.properties.expire: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["received"]) -> MetaOapg.properties.received: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spectrum"]) -> 'XiqAfcAvailableSpectrum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["band_width"]) -> MetaOapg.properties.band_width: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "expire", "received", "reason", "spectrum", "band_width", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expire"]) -> typing.Union[MetaOapg.properties.expire, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["received"]) -> typing.Union[MetaOapg.properties.received, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spectrum"]) -> typing.Union['XiqAfcAvailableSpectrum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["band_width"]) -> typing.Union[MetaOapg.properties.band_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "expire", "received", "reason", "spectrum", "band_width", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        expire: typing.Union[MetaOapg.properties.expire, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        received: typing.Union[MetaOapg.properties.received, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        spectrum: typing.Union['XiqAfcAvailableSpectrum', schemas.Unset] = schemas.unset,
        band_width: typing.Union[MetaOapg.properties.band_width, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAfcApDetail':
        return super().__new__(
            cls,
            *_args,
            status=status,
            expire=expire,
            received=received,
            reason=reason,
            spectrum=spectrum,
            band_width=band_width,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_afc_available_spectrum import XiqAfcAvailableSpectrum
