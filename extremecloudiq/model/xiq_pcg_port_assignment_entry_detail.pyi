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


class XiqPcgPortAssignmentEntryDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The PCG port assignment entry detail
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
            org_id = schemas.Int64Schema
        
            @staticmethod
            def device() -> typing.Type['XiqPcgPortAssignmentEntryDeviceMeta']:
                return XiqPcgPortAssignmentEntryDeviceMeta
        
            @staticmethod
            def eth1() -> typing.Type['XiqPcgPortAssignmentEntryEthUserMeta']:
                return XiqPcgPortAssignmentEntryEthUserMeta
        
            @staticmethod
            def eth2() -> typing.Type['XiqPcgPortAssignmentEntryEthUserMeta']:
                return XiqPcgPortAssignmentEntryEthUserMeta
        
            @staticmethod
            def eth3() -> typing.Type['XiqPcgPortAssignmentEntryEthUserMeta']:
                return XiqPcgPortAssignmentEntryEthUserMeta
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "org_id": org_id,
                "device": device,
                "eth1": eth1,
                "eth2": eth2,
                "eth3": eth3,
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
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device"]) -> 'XiqPcgPortAssignmentEntryDeviceMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth1"]) -> 'XiqPcgPortAssignmentEntryEthUserMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth2"]) -> 'XiqPcgPortAssignmentEntryEthUserMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eth3"]) -> 'XiqPcgPortAssignmentEntryEthUserMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "org_id", "device", "eth1", "eth2", "eth3", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device"]) -> typing.Union['XiqPcgPortAssignmentEntryDeviceMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth1"]) -> typing.Union['XiqPcgPortAssignmentEntryEthUserMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth2"]) -> typing.Union['XiqPcgPortAssignmentEntryEthUserMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eth3"]) -> typing.Union['XiqPcgPortAssignmentEntryEthUserMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "org_id", "device", "eth1", "eth2", "eth3", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        device: typing.Union['XiqPcgPortAssignmentEntryDeviceMeta', schemas.Unset] = schemas.unset,
        eth1: typing.Union['XiqPcgPortAssignmentEntryEthUserMeta', schemas.Unset] = schemas.unset,
        eth2: typing.Union['XiqPcgPortAssignmentEntryEthUserMeta', schemas.Unset] = schemas.unset,
        eth3: typing.Union['XiqPcgPortAssignmentEntryEthUserMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqPcgPortAssignmentEntryDetail':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            org_id=org_id,
            device=device,
            eth1=eth1,
            eth2=eth2,
            eth3=eth3,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_pcg_port_assignment_entry_device_meta import XiqPcgPortAssignmentEntryDeviceMeta
from extremecloudiq.model.xiq_pcg_port_assignment_entry_eth_user_meta import XiqPcgPortAssignmentEntryEthUserMeta
