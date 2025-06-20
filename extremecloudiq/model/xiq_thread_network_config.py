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


class XiqThreadNetworkConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The thread network configuration and security policy
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            channel = schemas.Int32Schema
            channel_mask = schemas.StrSchema
            ext_pan_id = schemas.StrSchema
            mesh_local_prefix = schemas.StrSchema
            network_key = schemas.StrSchema
            network_name = schemas.StrSchema
            pan_id = schemas.StrSchema
            pskc = schemas.StrSchema
            obtain_network_key_enabled = schemas.BoolSchema
            native_commissioning_enabled = schemas.BoolSchema
            routers_enabled = schemas.BoolSchema
            external_commissioning_enabled = schemas.BoolSchema
            beacons_enabled = schemas.BoolSchema
            commercial_commissioning_enabled = schemas.BoolSchema
            autonomous_enrollment_enabled = schemas.BoolSchema
            network_key_provisioning_enabled = schemas.BoolSchema
            non_ccm_routers_enabled = schemas.BoolSchema
            active_timestamp = schemas.Int32Schema
            __annotations__ = {
                "id": id,
                "channel": channel,
                "channel_mask": channel_mask,
                "ext_pan_id": ext_pan_id,
                "mesh_local_prefix": mesh_local_prefix,
                "network_key": network_key,
                "network_name": network_name,
                "pan_id": pan_id,
                "pskc": pskc,
                "obtain_network_key_enabled": obtain_network_key_enabled,
                "native_commissioning_enabled": native_commissioning_enabled,
                "routers_enabled": routers_enabled,
                "external_commissioning_enabled": external_commissioning_enabled,
                "beacons_enabled": beacons_enabled,
                "commercial_commissioning_enabled": commercial_commissioning_enabled,
                "autonomous_enrollment_enabled": autonomous_enrollment_enabled,
                "network_key_provisioning_enabled": network_key_provisioning_enabled,
                "non_ccm_routers_enabled": non_ccm_routers_enabled,
                "active_timestamp": active_timestamp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel_mask"]) -> MetaOapg.properties.channel_mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ext_pan_id"]) -> MetaOapg.properties.ext_pan_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mesh_local_prefix"]) -> MetaOapg.properties.mesh_local_prefix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_key"]) -> MetaOapg.properties.network_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_name"]) -> MetaOapg.properties.network_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pan_id"]) -> MetaOapg.properties.pan_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pskc"]) -> MetaOapg.properties.pskc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["obtain_network_key_enabled"]) -> MetaOapg.properties.obtain_network_key_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["native_commissioning_enabled"]) -> MetaOapg.properties.native_commissioning_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routers_enabled"]) -> MetaOapg.properties.routers_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_commissioning_enabled"]) -> MetaOapg.properties.external_commissioning_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beacons_enabled"]) -> MetaOapg.properties.beacons_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commercial_commissioning_enabled"]) -> MetaOapg.properties.commercial_commissioning_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autonomous_enrollment_enabled"]) -> MetaOapg.properties.autonomous_enrollment_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_key_provisioning_enabled"]) -> MetaOapg.properties.network_key_provisioning_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["non_ccm_routers_enabled"]) -> MetaOapg.properties.non_ccm_routers_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_timestamp"]) -> MetaOapg.properties.active_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "channel", "channel_mask", "ext_pan_id", "mesh_local_prefix", "network_key", "network_name", "pan_id", "pskc", "obtain_network_key_enabled", "native_commissioning_enabled", "routers_enabled", "external_commissioning_enabled", "beacons_enabled", "commercial_commissioning_enabled", "autonomous_enrollment_enabled", "network_key_provisioning_enabled", "non_ccm_routers_enabled", "active_timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel_mask"]) -> typing.Union[MetaOapg.properties.channel_mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ext_pan_id"]) -> typing.Union[MetaOapg.properties.ext_pan_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mesh_local_prefix"]) -> typing.Union[MetaOapg.properties.mesh_local_prefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_key"]) -> typing.Union[MetaOapg.properties.network_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_name"]) -> typing.Union[MetaOapg.properties.network_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pan_id"]) -> typing.Union[MetaOapg.properties.pan_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pskc"]) -> typing.Union[MetaOapg.properties.pskc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["obtain_network_key_enabled"]) -> typing.Union[MetaOapg.properties.obtain_network_key_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["native_commissioning_enabled"]) -> typing.Union[MetaOapg.properties.native_commissioning_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routers_enabled"]) -> typing.Union[MetaOapg.properties.routers_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_commissioning_enabled"]) -> typing.Union[MetaOapg.properties.external_commissioning_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beacons_enabled"]) -> typing.Union[MetaOapg.properties.beacons_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commercial_commissioning_enabled"]) -> typing.Union[MetaOapg.properties.commercial_commissioning_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autonomous_enrollment_enabled"]) -> typing.Union[MetaOapg.properties.autonomous_enrollment_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_key_provisioning_enabled"]) -> typing.Union[MetaOapg.properties.network_key_provisioning_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["non_ccm_routers_enabled"]) -> typing.Union[MetaOapg.properties.non_ccm_routers_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_timestamp"]) -> typing.Union[MetaOapg.properties.active_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "channel", "channel_mask", "ext_pan_id", "mesh_local_prefix", "network_key", "network_name", "pan_id", "pskc", "obtain_network_key_enabled", "native_commissioning_enabled", "routers_enabled", "external_commissioning_enabled", "beacons_enabled", "commercial_commissioning_enabled", "autonomous_enrollment_enabled", "network_key_provisioning_enabled", "non_ccm_routers_enabled", "active_timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        channel_mask: typing.Union[MetaOapg.properties.channel_mask, str, schemas.Unset] = schemas.unset,
        ext_pan_id: typing.Union[MetaOapg.properties.ext_pan_id, str, schemas.Unset] = schemas.unset,
        mesh_local_prefix: typing.Union[MetaOapg.properties.mesh_local_prefix, str, schemas.Unset] = schemas.unset,
        network_key: typing.Union[MetaOapg.properties.network_key, str, schemas.Unset] = schemas.unset,
        network_name: typing.Union[MetaOapg.properties.network_name, str, schemas.Unset] = schemas.unset,
        pan_id: typing.Union[MetaOapg.properties.pan_id, str, schemas.Unset] = schemas.unset,
        pskc: typing.Union[MetaOapg.properties.pskc, str, schemas.Unset] = schemas.unset,
        obtain_network_key_enabled: typing.Union[MetaOapg.properties.obtain_network_key_enabled, bool, schemas.Unset] = schemas.unset,
        native_commissioning_enabled: typing.Union[MetaOapg.properties.native_commissioning_enabled, bool, schemas.Unset] = schemas.unset,
        routers_enabled: typing.Union[MetaOapg.properties.routers_enabled, bool, schemas.Unset] = schemas.unset,
        external_commissioning_enabled: typing.Union[MetaOapg.properties.external_commissioning_enabled, bool, schemas.Unset] = schemas.unset,
        beacons_enabled: typing.Union[MetaOapg.properties.beacons_enabled, bool, schemas.Unset] = schemas.unset,
        commercial_commissioning_enabled: typing.Union[MetaOapg.properties.commercial_commissioning_enabled, bool, schemas.Unset] = schemas.unset,
        autonomous_enrollment_enabled: typing.Union[MetaOapg.properties.autonomous_enrollment_enabled, bool, schemas.Unset] = schemas.unset,
        network_key_provisioning_enabled: typing.Union[MetaOapg.properties.network_key_provisioning_enabled, bool, schemas.Unset] = schemas.unset,
        non_ccm_routers_enabled: typing.Union[MetaOapg.properties.non_ccm_routers_enabled, bool, schemas.Unset] = schemas.unset,
        active_timestamp: typing.Union[MetaOapg.properties.active_timestamp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqThreadNetworkConfig':
        return super().__new__(
            cls,
            *_args,
            id=id,
            channel=channel,
            channel_mask=channel_mask,
            ext_pan_id=ext_pan_id,
            mesh_local_prefix=mesh_local_prefix,
            network_key=network_key,
            network_name=network_name,
            pan_id=pan_id,
            pskc=pskc,
            obtain_network_key_enabled=obtain_network_key_enabled,
            native_commissioning_enabled=native_commissioning_enabled,
            routers_enabled=routers_enabled,
            external_commissioning_enabled=external_commissioning_enabled,
            beacons_enabled=beacons_enabled,
            commercial_commissioning_enabled=commercial_commissioning_enabled,
            autonomous_enrollment_enabled=autonomous_enrollment_enabled,
            network_key_provisioning_enabled=network_key_provisioning_enabled,
            non_ccm_routers_enabled=non_ccm_routers_enabled,
            active_timestamp=active_timestamp,
            _configuration=_configuration,
            **kwargs,
        )
