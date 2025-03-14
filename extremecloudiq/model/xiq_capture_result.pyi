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


class XiqCaptureResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This represents the packet capture result on an AP's interface. A packet capture session may involve multiple APs on multiple interfaces.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            org_id = schemas.Int64Schema
            start_time = schemas.DateTimeSchema
            end_time = schemas.DateTimeSchema
            device_id = schemas.Int64Schema
            hostname = schemas.StrSchema
            mac_address = schemas.StrSchema
            interface_name = schemas.StrSchema
            location_id = schemas.Int64Schema
            
            
            class locations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqLocationLegend']:
                        return XiqLocationLegend
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqLocationLegend'], typing.List['XiqLocationLegend']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'locations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqLocationLegend':
                    return super().__getitem__(i)
        
            @staticmethod
            def status() -> typing.Type['XiqPacketCaptureStatus']:
                return XiqPacketCaptureStatus
            error_message = schemas.StrSchema
        
            @staticmethod
            def storage() -> typing.Type['XiqStorage']:
                return XiqStorage
            __annotations__ = {
                "id": id,
                "org_id": org_id,
                "start_time": start_time,
                "end_time": end_time,
                "device_id": device_id,
                "hostname": hostname,
                "mac_address": mac_address,
                "interface_name": interface_name,
                "location_id": location_id,
                "locations": locations,
                "status": status,
                "error_message": error_message,
                "storage": storage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interface_name"]) -> MetaOapg.properties.interface_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locations"]) -> MetaOapg.properties.locations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'XiqPacketCaptureStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_message"]) -> MetaOapg.properties.error_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storage"]) -> 'XiqStorage': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "org_id", "start_time", "end_time", "device_id", "hostname", "mac_address", "interface_name", "location_id", "locations", "status", "error_message", "storage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> typing.Union[MetaOapg.properties.end_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> typing.Union[MetaOapg.properties.mac_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interface_name"]) -> typing.Union[MetaOapg.properties.interface_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locations"]) -> typing.Union[MetaOapg.properties.locations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['XiqPacketCaptureStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_message"]) -> typing.Union[MetaOapg.properties.error_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storage"]) -> typing.Union['XiqStorage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "org_id", "start_time", "end_time", "device_id", "hostname", "mac_address", "interface_name", "location_id", "locations", "status", "error_message", "storage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        end_time: typing.Union[MetaOapg.properties.end_time, str, datetime, schemas.Unset] = schemas.unset,
        device_id: typing.Union[MetaOapg.properties.device_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, schemas.Unset] = schemas.unset,
        interface_name: typing.Union[MetaOapg.properties.interface_name, str, schemas.Unset] = schemas.unset,
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        locations: typing.Union[MetaOapg.properties.locations, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union['XiqPacketCaptureStatus', schemas.Unset] = schemas.unset,
        error_message: typing.Union[MetaOapg.properties.error_message, str, schemas.Unset] = schemas.unset,
        storage: typing.Union['XiqStorage', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCaptureResult':
        return super().__new__(
            cls,
            *_args,
            id=id,
            org_id=org_id,
            start_time=start_time,
            end_time=end_time,
            device_id=device_id,
            hostname=hostname,
            mac_address=mac_address,
            interface_name=interface_name,
            location_id=location_id,
            locations=locations,
            status=status,
            error_message=error_message,
            storage=storage,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_location_legend import XiqLocationLegend
from extremecloudiq.model.xiq_packet_capture_status import XiqPacketCaptureStatus
from extremecloudiq.model.xiq_storage import XiqStorage
