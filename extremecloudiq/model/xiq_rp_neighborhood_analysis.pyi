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


class XiqRpNeighborhoodAnalysis(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload of neighborhood analysis config for the radio profile
    """


    class MetaOapg:
        required = {
            "update_time",
            "create_time",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            enable_background_scan = schemas.BoolSchema
            background_scan_interval = schemas.Int32Schema
            enable_skip_scan_when_clients_connected = schemas.BoolSchema
            enable_skip_scan_when_clients_in_power_save_mode = schemas.BoolSchema
            enable_skip_scan_when_process_voice_traffic = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "enable_background_scan": enable_background_scan,
                "background_scan_interval": background_scan_interval,
                "enable_skip_scan_when_clients_connected": enable_skip_scan_when_clients_connected,
                "enable_skip_scan_when_clients_in_power_save_mode": enable_skip_scan_when_clients_in_power_save_mode,
                "enable_skip_scan_when_process_voice_traffic": enable_skip_scan_when_process_voice_traffic,
            }
    
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_background_scan"]) -> MetaOapg.properties.enable_background_scan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["background_scan_interval"]) -> MetaOapg.properties.background_scan_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_skip_scan_when_clients_connected"]) -> MetaOapg.properties.enable_skip_scan_when_clients_connected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_skip_scan_when_clients_in_power_save_mode"]) -> MetaOapg.properties.enable_skip_scan_when_clients_in_power_save_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_skip_scan_when_process_voice_traffic"]) -> MetaOapg.properties.enable_skip_scan_when_process_voice_traffic: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "enable_background_scan", "background_scan_interval", "enable_skip_scan_when_clients_connected", "enable_skip_scan_when_clients_in_power_save_mode", "enable_skip_scan_when_process_voice_traffic", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_background_scan"]) -> typing.Union[MetaOapg.properties.enable_background_scan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["background_scan_interval"]) -> typing.Union[MetaOapg.properties.background_scan_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_skip_scan_when_clients_connected"]) -> typing.Union[MetaOapg.properties.enable_skip_scan_when_clients_connected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_skip_scan_when_clients_in_power_save_mode"]) -> typing.Union[MetaOapg.properties.enable_skip_scan_when_clients_in_power_save_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_skip_scan_when_process_voice_traffic"]) -> typing.Union[MetaOapg.properties.enable_skip_scan_when_process_voice_traffic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "enable_background_scan", "background_scan_interval", "enable_skip_scan_when_clients_connected", "enable_skip_scan_when_clients_in_power_save_mode", "enable_skip_scan_when_process_voice_traffic", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        enable_background_scan: typing.Union[MetaOapg.properties.enable_background_scan, bool, schemas.Unset] = schemas.unset,
        background_scan_interval: typing.Union[MetaOapg.properties.background_scan_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_skip_scan_when_clients_connected: typing.Union[MetaOapg.properties.enable_skip_scan_when_clients_connected, bool, schemas.Unset] = schemas.unset,
        enable_skip_scan_when_clients_in_power_save_mode: typing.Union[MetaOapg.properties.enable_skip_scan_when_clients_in_power_save_mode, bool, schemas.Unset] = schemas.unset,
        enable_skip_scan_when_process_voice_traffic: typing.Union[MetaOapg.properties.enable_skip_scan_when_process_voice_traffic, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqRpNeighborhoodAnalysis':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            enable_background_scan=enable_background_scan,
            background_scan_interval=background_scan_interval,
            enable_skip_scan_when_clients_connected=enable_skip_scan_when_clients_connected,
            enable_skip_scan_when_clients_in_power_save_mode=enable_skip_scan_when_clients_in_power_save_mode,
            enable_skip_scan_when_process_voice_traffic=enable_skip_scan_when_process_voice_traffic,
            _configuration=_configuration,
            **kwargs,
        )
