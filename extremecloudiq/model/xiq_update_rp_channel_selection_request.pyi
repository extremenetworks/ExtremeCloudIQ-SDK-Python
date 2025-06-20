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


class XiqUpdateRpChannelSelectionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            enable_dynamic_channel_switching = schemas.BoolSchema
            channel_width = schemas.StrSchema
            enable_dynamic_frequency_selection = schemas.BoolSchema
            enable_static_channel = schemas.BoolSchema
            enable_zero_wait_dfs = schemas.BoolSchema
            enable_use_last_selection = schemas.BoolSchema
            exclude_channels = schemas.StrSchema
            exclude_channels_width = schemas.StrSchema
            
            
            class channel(
                schemas.Int32Schema
            ):
                pass
            enable_limit_channel_selection = schemas.BoolSchema
            channel_region = schemas.StrSchema
            
            
            class channel_model(
                schemas.Int32Schema
            ):
                pass
            channels = schemas.StrSchema
            enable_channel_auto_selection = schemas.BoolSchema
            channel_selection_start_time = schemas.StrSchema
            channel_selection_end_time = schemas.StrSchema
            enable_avoid_switch_channel_if_clients_connected = schemas.BoolSchema
            
            
            class channel_selection_max_clients(
                schemas.Int32Schema
            ):
                pass
            enable_switch_channel_if_exceed_threshold = schemas.BoolSchema
            
            
            class rf_interference_threshold(
                schemas.Int32Schema
            ):
                pass
            
            
            class crc_error_threshold(
                schemas.Int32Schema
            ):
                pass
            __annotations__ = {
                "enable_dynamic_channel_switching": enable_dynamic_channel_switching,
                "channel_width": channel_width,
                "enable_dynamic_frequency_selection": enable_dynamic_frequency_selection,
                "enable_static_channel": enable_static_channel,
                "enable_zero_wait_dfs": enable_zero_wait_dfs,
                "enable_use_last_selection": enable_use_last_selection,
                "exclude_channels": exclude_channels,
                "exclude_channels_width": exclude_channels_width,
                "channel": channel,
                "enable_limit_channel_selection": enable_limit_channel_selection,
                "channel_region": channel_region,
                "channel_model": channel_model,
                "channels": channels,
                "enable_channel_auto_selection": enable_channel_auto_selection,
                "channel_selection_start_time": channel_selection_start_time,
                "channel_selection_end_time": channel_selection_end_time,
                "enable_avoid_switch_channel_if_clients_connected": enable_avoid_switch_channel_if_clients_connected,
                "channel_selection_max_clients": channel_selection_max_clients,
                "enable_switch_channel_if_exceed_threshold": enable_switch_channel_if_exceed_threshold,
                "rf_interference_threshold": rf_interference_threshold,
                "crc_error_threshold": crc_error_threshold,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_dynamic_channel_switching"]) -> MetaOapg.properties.enable_dynamic_channel_switching: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_width"]) -> MetaOapg.properties.channel_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_dynamic_frequency_selection"]) -> MetaOapg.properties.enable_dynamic_frequency_selection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_static_channel"]) -> MetaOapg.properties.enable_static_channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_zero_wait_dfs"]) -> MetaOapg.properties.enable_zero_wait_dfs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_use_last_selection"]) -> MetaOapg.properties.enable_use_last_selection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_channels"]) -> MetaOapg.properties.exclude_channels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_channels_width"]) -> MetaOapg.properties.exclude_channels_width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_limit_channel_selection"]) -> MetaOapg.properties.enable_limit_channel_selection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_region"]) -> MetaOapg.properties.channel_region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_model"]) -> MetaOapg.properties.channel_model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channels"]) -> MetaOapg.properties.channels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_channel_auto_selection"]) -> MetaOapg.properties.enable_channel_auto_selection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_selection_start_time"]) -> MetaOapg.properties.channel_selection_start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_selection_end_time"]) -> MetaOapg.properties.channel_selection_end_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_avoid_switch_channel_if_clients_connected"]) -> MetaOapg.properties.enable_avoid_switch_channel_if_clients_connected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_selection_max_clients"]) -> MetaOapg.properties.channel_selection_max_clients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_switch_channel_if_exceed_threshold"]) -> MetaOapg.properties.enable_switch_channel_if_exceed_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rf_interference_threshold"]) -> MetaOapg.properties.rf_interference_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["crc_error_threshold"]) -> MetaOapg.properties.crc_error_threshold: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enable_dynamic_channel_switching", "channel_width", "enable_dynamic_frequency_selection", "enable_static_channel", "enable_zero_wait_dfs", "enable_use_last_selection", "exclude_channels", "exclude_channels_width", "channel", "enable_limit_channel_selection", "channel_region", "channel_model", "channels", "enable_channel_auto_selection", "channel_selection_start_time", "channel_selection_end_time", "enable_avoid_switch_channel_if_clients_connected", "channel_selection_max_clients", "enable_switch_channel_if_exceed_threshold", "rf_interference_threshold", "crc_error_threshold", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_dynamic_channel_switching"]) -> typing.Union[MetaOapg.properties.enable_dynamic_channel_switching, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_width"]) -> typing.Union[MetaOapg.properties.channel_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_dynamic_frequency_selection"]) -> typing.Union[MetaOapg.properties.enable_dynamic_frequency_selection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_static_channel"]) -> typing.Union[MetaOapg.properties.enable_static_channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_zero_wait_dfs"]) -> typing.Union[MetaOapg.properties.enable_zero_wait_dfs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_use_last_selection"]) -> typing.Union[MetaOapg.properties.enable_use_last_selection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_channels"]) -> typing.Union[MetaOapg.properties.exclude_channels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_channels_width"]) -> typing.Union[MetaOapg.properties.exclude_channels_width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_limit_channel_selection"]) -> typing.Union[MetaOapg.properties.enable_limit_channel_selection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_region"]) -> typing.Union[MetaOapg.properties.channel_region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_model"]) -> typing.Union[MetaOapg.properties.channel_model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channels"]) -> typing.Union[MetaOapg.properties.channels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_channel_auto_selection"]) -> typing.Union[MetaOapg.properties.enable_channel_auto_selection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_selection_start_time"]) -> typing.Union[MetaOapg.properties.channel_selection_start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_selection_end_time"]) -> typing.Union[MetaOapg.properties.channel_selection_end_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_avoid_switch_channel_if_clients_connected"]) -> typing.Union[MetaOapg.properties.enable_avoid_switch_channel_if_clients_connected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_selection_max_clients"]) -> typing.Union[MetaOapg.properties.channel_selection_max_clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_switch_channel_if_exceed_threshold"]) -> typing.Union[MetaOapg.properties.enable_switch_channel_if_exceed_threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rf_interference_threshold"]) -> typing.Union[MetaOapg.properties.rf_interference_threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["crc_error_threshold"]) -> typing.Union[MetaOapg.properties.crc_error_threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enable_dynamic_channel_switching", "channel_width", "enable_dynamic_frequency_selection", "enable_static_channel", "enable_zero_wait_dfs", "enable_use_last_selection", "exclude_channels", "exclude_channels_width", "channel", "enable_limit_channel_selection", "channel_region", "channel_model", "channels", "enable_channel_auto_selection", "channel_selection_start_time", "channel_selection_end_time", "enable_avoid_switch_channel_if_clients_connected", "channel_selection_max_clients", "enable_switch_channel_if_exceed_threshold", "rf_interference_threshold", "crc_error_threshold", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_dynamic_channel_switching: typing.Union[MetaOapg.properties.enable_dynamic_channel_switching, bool, schemas.Unset] = schemas.unset,
        channel_width: typing.Union[MetaOapg.properties.channel_width, str, schemas.Unset] = schemas.unset,
        enable_dynamic_frequency_selection: typing.Union[MetaOapg.properties.enable_dynamic_frequency_selection, bool, schemas.Unset] = schemas.unset,
        enable_static_channel: typing.Union[MetaOapg.properties.enable_static_channel, bool, schemas.Unset] = schemas.unset,
        enable_zero_wait_dfs: typing.Union[MetaOapg.properties.enable_zero_wait_dfs, bool, schemas.Unset] = schemas.unset,
        enable_use_last_selection: typing.Union[MetaOapg.properties.enable_use_last_selection, bool, schemas.Unset] = schemas.unset,
        exclude_channels: typing.Union[MetaOapg.properties.exclude_channels, str, schemas.Unset] = schemas.unset,
        exclude_channels_width: typing.Union[MetaOapg.properties.exclude_channels_width, str, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_limit_channel_selection: typing.Union[MetaOapg.properties.enable_limit_channel_selection, bool, schemas.Unset] = schemas.unset,
        channel_region: typing.Union[MetaOapg.properties.channel_region, str, schemas.Unset] = schemas.unset,
        channel_model: typing.Union[MetaOapg.properties.channel_model, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        channels: typing.Union[MetaOapg.properties.channels, str, schemas.Unset] = schemas.unset,
        enable_channel_auto_selection: typing.Union[MetaOapg.properties.enable_channel_auto_selection, bool, schemas.Unset] = schemas.unset,
        channel_selection_start_time: typing.Union[MetaOapg.properties.channel_selection_start_time, str, schemas.Unset] = schemas.unset,
        channel_selection_end_time: typing.Union[MetaOapg.properties.channel_selection_end_time, str, schemas.Unset] = schemas.unset,
        enable_avoid_switch_channel_if_clients_connected: typing.Union[MetaOapg.properties.enable_avoid_switch_channel_if_clients_connected, bool, schemas.Unset] = schemas.unset,
        channel_selection_max_clients: typing.Union[MetaOapg.properties.channel_selection_max_clients, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_switch_channel_if_exceed_threshold: typing.Union[MetaOapg.properties.enable_switch_channel_if_exceed_threshold, bool, schemas.Unset] = schemas.unset,
        rf_interference_threshold: typing.Union[MetaOapg.properties.rf_interference_threshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        crc_error_threshold: typing.Union[MetaOapg.properties.crc_error_threshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUpdateRpChannelSelectionRequest':
        return super().__new__(
            cls,
            *_args,
            enable_dynamic_channel_switching=enable_dynamic_channel_switching,
            channel_width=channel_width,
            enable_dynamic_frequency_selection=enable_dynamic_frequency_selection,
            enable_static_channel=enable_static_channel,
            enable_zero_wait_dfs=enable_zero_wait_dfs,
            enable_use_last_selection=enable_use_last_selection,
            exclude_channels=exclude_channels,
            exclude_channels_width=exclude_channels_width,
            channel=channel,
            enable_limit_channel_selection=enable_limit_channel_selection,
            channel_region=channel_region,
            channel_model=channel_model,
            channels=channels,
            enable_channel_auto_selection=enable_channel_auto_selection,
            channel_selection_start_time=channel_selection_start_time,
            channel_selection_end_time=channel_selection_end_time,
            enable_avoid_switch_channel_if_clients_connected=enable_avoid_switch_channel_if_clients_connected,
            channel_selection_max_clients=channel_selection_max_clients,
            enable_switch_channel_if_exceed_threshold=enable_switch_channel_if_exceed_threshold,
            rf_interference_threshold=rf_interference_threshold,
            crc_error_threshold=crc_error_threshold,
            _configuration=_configuration,
            **kwargs,
        )
