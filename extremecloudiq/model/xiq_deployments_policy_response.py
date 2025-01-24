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


class XiqDeploymentsPolicyResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The deployment policy
    """


    class MetaOapg:
        
        class properties:
            enable_complete_configuration_update = schemas.BoolSchema
        
            @staticmethod
            def firmware_upgrade_policy() -> typing.Type['XiqFirmwareUpgradePolicy']:
                return XiqFirmwareUpgradePolicy
            
            
            class firmware_upgrade_versions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqFirmwareUpgradeVersion']:
                        return XiqFirmwareUpgradeVersion
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqFirmwareUpgradeVersion'], typing.List['XiqFirmwareUpgradeVersion']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'firmware_upgrade_versions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqFirmwareUpgradeVersion':
                    return super().__getitem__(i)
        
            @staticmethod
            def firmware_activate_option() -> typing.Type['XiqFirmwareActivateOption']:
                return XiqFirmwareActivateOption
            __annotations__ = {
                "enable_complete_configuration_update": enable_complete_configuration_update,
                "firmware_upgrade_policy": firmware_upgrade_policy,
                "firmware_upgrade_versions": firmware_upgrade_versions,
                "firmware_activate_option": firmware_activate_option,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_complete_configuration_update"]) -> MetaOapg.properties.enable_complete_configuration_update: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware_upgrade_policy"]) -> 'XiqFirmwareUpgradePolicy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware_upgrade_versions"]) -> MetaOapg.properties.firmware_upgrade_versions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware_activate_option"]) -> 'XiqFirmwareActivateOption': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enable_complete_configuration_update", "firmware_upgrade_policy", "firmware_upgrade_versions", "firmware_activate_option", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_complete_configuration_update"]) -> typing.Union[MetaOapg.properties.enable_complete_configuration_update, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware_upgrade_policy"]) -> typing.Union['XiqFirmwareUpgradePolicy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware_upgrade_versions"]) -> typing.Union[MetaOapg.properties.firmware_upgrade_versions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware_activate_option"]) -> typing.Union['XiqFirmwareActivateOption', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enable_complete_configuration_update", "firmware_upgrade_policy", "firmware_upgrade_versions", "firmware_activate_option", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_complete_configuration_update: typing.Union[MetaOapg.properties.enable_complete_configuration_update, bool, schemas.Unset] = schemas.unset,
        firmware_upgrade_policy: typing.Union['XiqFirmwareUpgradePolicy', schemas.Unset] = schemas.unset,
        firmware_upgrade_versions: typing.Union[MetaOapg.properties.firmware_upgrade_versions, list, tuple, schemas.Unset] = schemas.unset,
        firmware_activate_option: typing.Union['XiqFirmwareActivateOption', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeploymentsPolicyResponse':
        return super().__new__(
            cls,
            *_args,
            enable_complete_configuration_update=enable_complete_configuration_update,
            firmware_upgrade_policy=firmware_upgrade_policy,
            firmware_upgrade_versions=firmware_upgrade_versions,
            firmware_activate_option=firmware_activate_option,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_firmware_activate_option import XiqFirmwareActivateOption
from extremecloudiq.model.xiq_firmware_upgrade_policy import XiqFirmwareUpgradePolicy
from extremecloudiq.model.xiq_firmware_upgrade_version import XiqFirmwareUpgradeVersion
