# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
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


class XiqIotpMaBleScanVendor(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Collection of BLE Scan vendor filters for Generic Scan applications, for BLE Scan applications of type GENERIC.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def vendor_type() -> typing.Type['XiqIotpMaBleScanVendorType']:
                return XiqIotpMaBleScanVendorType
            vendor_name = schemas.StrSchema
            
            
            class company_id(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 65535
                    inclusive_minimum = -1
            __annotations__ = {
                "vendor_type": vendor_type,
                "vendor_name": vendor_name,
                "company_id": company_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor_type"]) -> 'XiqIotpMaBleScanVendorType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor_name"]) -> MetaOapg.properties.vendor_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["vendor_type", "vendor_name", "company_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor_type"]) -> typing.Union['XiqIotpMaBleScanVendorType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor_name"]) -> typing.Union[MetaOapg.properties.vendor_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> typing.Union[MetaOapg.properties.company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["vendor_type", "vendor_name", "company_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        vendor_type: typing.Union['XiqIotpMaBleScanVendorType', schemas.Unset] = schemas.unset,
        vendor_name: typing.Union[MetaOapg.properties.vendor_name, str, schemas.Unset] = schemas.unset,
        company_id: typing.Union[MetaOapg.properties.company_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqIotpMaBleScanVendor':
        return super().__new__(
            cls,
            *_args,
            vendor_type=vendor_type,
            vendor_name=vendor_name,
            company_id=company_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_iotp_ma_ble_scan_vendor_type import XiqIotpMaBleScanVendorType
