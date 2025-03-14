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


class XiqDeviceSystemInformation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            host_name = schemas.StrSchema
            network_policy = schemas.StrSchema
            
            
            class ssids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            device_model = schemas.StrSchema
        
            @staticmethod
            def function() -> typing.Type['XiqDeviceFunction']:
                return XiqDeviceFunction
            device_template = schemas.StrSchema
            configuration_type = schemas.StrSchema
            serial_number = schemas.StrSchema
            iq_engine = schemas.StrSchema
        
            @staticmethod
            def device_status() -> typing.Type['XiqDeviceAdminState']:
                return XiqDeviceAdminState
            mgt0_ipv4_address = schemas.StrSchema
            mgt0_ipv6_address = schemas.StrSchema
            ipv4_subnet_mask = schemas.StrSchema
            ipv6_subnet_mask = schemas.StrSchema
            ipv4_default_gateway = schemas.StrSchema
            ipv6_default_gateway = schemas.StrSchema
            mgt0_macaddress = schemas.StrSchema
            dns = schemas.StrSchema
            ntp = schemas.StrSchema
            __annotations__ = {
                "host_name": host_name,
                "network_policy": network_policy,
                "ssids": ssids,
                "device_model": device_model,
                "function": function,
                "device_template": device_template,
                "configuration_type": configuration_type,
                "serial_number": serial_number,
                "iq_engine": iq_engine,
                "device_status": device_status,
                "mgt0_ipv4_address": mgt0_ipv4_address,
                "mgt0_ipv6_address": mgt0_ipv6_address,
                "ipv4_subnet_mask": ipv4_subnet_mask,
                "ipv6_subnet_mask": ipv6_subnet_mask,
                "ipv4_default_gateway": ipv4_default_gateway,
                "ipv6_default_gateway": ipv6_default_gateway,
                "mgt0_macaddress": mgt0_macaddress,
                "dns": dns,
                "ntp": ntp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_name"]) -> MetaOapg.properties.host_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_policy"]) -> MetaOapg.properties.network_policy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssids"]) -> MetaOapg.properties.ssids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_model"]) -> MetaOapg.properties.device_model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["function"]) -> 'XiqDeviceFunction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_template"]) -> MetaOapg.properties.device_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration_type"]) -> MetaOapg.properties.configuration_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serial_number"]) -> MetaOapg.properties.serial_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iq_engine"]) -> MetaOapg.properties.iq_engine: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_status"]) -> 'XiqDeviceAdminState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mgt0_ipv4_address"]) -> MetaOapg.properties.mgt0_ipv4_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mgt0_ipv6_address"]) -> MetaOapg.properties.mgt0_ipv6_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv4_subnet_mask"]) -> MetaOapg.properties.ipv4_subnet_mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv6_subnet_mask"]) -> MetaOapg.properties.ipv6_subnet_mask: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv4_default_gateway"]) -> MetaOapg.properties.ipv4_default_gateway: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipv6_default_gateway"]) -> MetaOapg.properties.ipv6_default_gateway: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mgt0_macaddress"]) -> MetaOapg.properties.mgt0_macaddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dns"]) -> MetaOapg.properties.dns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ntp"]) -> MetaOapg.properties.ntp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["host_name", "network_policy", "ssids", "device_model", "function", "device_template", "configuration_type", "serial_number", "iq_engine", "device_status", "mgt0_ipv4_address", "mgt0_ipv6_address", "ipv4_subnet_mask", "ipv6_subnet_mask", "ipv4_default_gateway", "ipv6_default_gateway", "mgt0_macaddress", "dns", "ntp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_name"]) -> typing.Union[MetaOapg.properties.host_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_policy"]) -> typing.Union[MetaOapg.properties.network_policy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssids"]) -> typing.Union[MetaOapg.properties.ssids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_model"]) -> typing.Union[MetaOapg.properties.device_model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["function"]) -> typing.Union['XiqDeviceFunction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_template"]) -> typing.Union[MetaOapg.properties.device_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration_type"]) -> typing.Union[MetaOapg.properties.configuration_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial_number"]) -> typing.Union[MetaOapg.properties.serial_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iq_engine"]) -> typing.Union[MetaOapg.properties.iq_engine, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_status"]) -> typing.Union['XiqDeviceAdminState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mgt0_ipv4_address"]) -> typing.Union[MetaOapg.properties.mgt0_ipv4_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mgt0_ipv6_address"]) -> typing.Union[MetaOapg.properties.mgt0_ipv6_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv4_subnet_mask"]) -> typing.Union[MetaOapg.properties.ipv4_subnet_mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv6_subnet_mask"]) -> typing.Union[MetaOapg.properties.ipv6_subnet_mask, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv4_default_gateway"]) -> typing.Union[MetaOapg.properties.ipv4_default_gateway, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipv6_default_gateway"]) -> typing.Union[MetaOapg.properties.ipv6_default_gateway, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mgt0_macaddress"]) -> typing.Union[MetaOapg.properties.mgt0_macaddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dns"]) -> typing.Union[MetaOapg.properties.dns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ntp"]) -> typing.Union[MetaOapg.properties.ntp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["host_name", "network_policy", "ssids", "device_model", "function", "device_template", "configuration_type", "serial_number", "iq_engine", "device_status", "mgt0_ipv4_address", "mgt0_ipv6_address", "ipv4_subnet_mask", "ipv6_subnet_mask", "ipv4_default_gateway", "ipv6_default_gateway", "mgt0_macaddress", "dns", "ntp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        host_name: typing.Union[MetaOapg.properties.host_name, str, schemas.Unset] = schemas.unset,
        network_policy: typing.Union[MetaOapg.properties.network_policy, str, schemas.Unset] = schemas.unset,
        ssids: typing.Union[MetaOapg.properties.ssids, list, tuple, schemas.Unset] = schemas.unset,
        device_model: typing.Union[MetaOapg.properties.device_model, str, schemas.Unset] = schemas.unset,
        function: typing.Union['XiqDeviceFunction', schemas.Unset] = schemas.unset,
        device_template: typing.Union[MetaOapg.properties.device_template, str, schemas.Unset] = schemas.unset,
        configuration_type: typing.Union[MetaOapg.properties.configuration_type, str, schemas.Unset] = schemas.unset,
        serial_number: typing.Union[MetaOapg.properties.serial_number, str, schemas.Unset] = schemas.unset,
        iq_engine: typing.Union[MetaOapg.properties.iq_engine, str, schemas.Unset] = schemas.unset,
        device_status: typing.Union['XiqDeviceAdminState', schemas.Unset] = schemas.unset,
        mgt0_ipv4_address: typing.Union[MetaOapg.properties.mgt0_ipv4_address, str, schemas.Unset] = schemas.unset,
        mgt0_ipv6_address: typing.Union[MetaOapg.properties.mgt0_ipv6_address, str, schemas.Unset] = schemas.unset,
        ipv4_subnet_mask: typing.Union[MetaOapg.properties.ipv4_subnet_mask, str, schemas.Unset] = schemas.unset,
        ipv6_subnet_mask: typing.Union[MetaOapg.properties.ipv6_subnet_mask, str, schemas.Unset] = schemas.unset,
        ipv4_default_gateway: typing.Union[MetaOapg.properties.ipv4_default_gateway, str, schemas.Unset] = schemas.unset,
        ipv6_default_gateway: typing.Union[MetaOapg.properties.ipv6_default_gateway, str, schemas.Unset] = schemas.unset,
        mgt0_macaddress: typing.Union[MetaOapg.properties.mgt0_macaddress, str, schemas.Unset] = schemas.unset,
        dns: typing.Union[MetaOapg.properties.dns, str, schemas.Unset] = schemas.unset,
        ntp: typing.Union[MetaOapg.properties.ntp, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeviceSystemInformation':
        return super().__new__(
            cls,
            *_args,
            host_name=host_name,
            network_policy=network_policy,
            ssids=ssids,
            device_model=device_model,
            function=function,
            device_template=device_template,
            configuration_type=configuration_type,
            serial_number=serial_number,
            iq_engine=iq_engine,
            device_status=device_status,
            mgt0_ipv4_address=mgt0_ipv4_address,
            mgt0_ipv6_address=mgt0_ipv6_address,
            ipv4_subnet_mask=ipv4_subnet_mask,
            ipv6_subnet_mask=ipv6_subnet_mask,
            ipv4_default_gateway=ipv4_default_gateway,
            ipv6_default_gateway=ipv6_default_gateway,
            mgt0_macaddress=mgt0_macaddress,
            dns=dns,
            ntp=ntp,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_device_admin_state import XiqDeviceAdminState
from extremecloudiq.model.xiq_device_function import XiqDeviceFunction
