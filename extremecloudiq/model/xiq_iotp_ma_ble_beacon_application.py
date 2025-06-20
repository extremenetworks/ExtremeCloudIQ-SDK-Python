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


class XiqIotpMaBleBeaconApplication(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Collection of BLE Beacon applications
    """


    class MetaOapg:
        required = {
            "app_type",
        }
        
        class properties:
        
            @staticmethod
            def app_type() -> typing.Type['XiqIotpMaBleBeaconAppType']:
                return XiqIotpMaBleBeaconAppType
            
            
            class measured_rss(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 15
                    inclusive_minimum = -120
            
            
            class advertise_interval(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 10240
                    inclusive_minimum = 100
            
            
            class tx_power(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 3
                    inclusive_minimum = -16
            
            
            class major(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 65535
                    inclusive_minimum = 0
            
            
            class minor(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 65535
                    inclusive_minimum = 0
            
            
            class uuid(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$',  # noqa: E501
                    }]
            
            
            class url(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 34
                    min_length = 0
            __annotations__ = {
                "app_type": app_type,
                "measured_rss": measured_rss,
                "advertise_interval": advertise_interval,
                "tx_power": tx_power,
                "major": major,
                "minor": minor,
                "uuid": uuid,
                "url": url,
            }
    
    app_type: 'XiqIotpMaBleBeaconAppType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_type"]) -> 'XiqIotpMaBleBeaconAppType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["measured_rss"]) -> MetaOapg.properties.measured_rss: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["advertise_interval"]) -> MetaOapg.properties.advertise_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tx_power"]) -> MetaOapg.properties.tx_power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["major"]) -> MetaOapg.properties.major: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minor"]) -> MetaOapg.properties.minor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["app_type", "measured_rss", "advertise_interval", "tx_power", "major", "minor", "uuid", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_type"]) -> 'XiqIotpMaBleBeaconAppType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["measured_rss"]) -> typing.Union[MetaOapg.properties.measured_rss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["advertise_interval"]) -> typing.Union[MetaOapg.properties.advertise_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tx_power"]) -> typing.Union[MetaOapg.properties.tx_power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["major"]) -> typing.Union[MetaOapg.properties.major, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minor"]) -> typing.Union[MetaOapg.properties.minor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["app_type", "measured_rss", "advertise_interval", "tx_power", "major", "minor", "uuid", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        app_type: 'XiqIotpMaBleBeaconAppType',
        measured_rss: typing.Union[MetaOapg.properties.measured_rss, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        advertise_interval: typing.Union[MetaOapg.properties.advertise_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tx_power: typing.Union[MetaOapg.properties.tx_power, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        major: typing.Union[MetaOapg.properties.major, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minor: typing.Union[MetaOapg.properties.minor, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqIotpMaBleBeaconApplication':
        return super().__new__(
            cls,
            *_args,
            app_type=app_type,
            measured_rss=measured_rss,
            advertise_interval=advertise_interval,
            tx_power=tx_power,
            major=major,
            minor=minor,
            uuid=uuid,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_iotp_ma_ble_beacon_app_type import XiqIotpMaBleBeaconAppType
