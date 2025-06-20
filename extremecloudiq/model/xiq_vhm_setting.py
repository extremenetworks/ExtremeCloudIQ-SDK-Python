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


class XiqVhmSetting(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The VHM Setting.
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
            enable_copilot = schemas.BoolSchema
            enable_ssh = schemas.BoolSchema
            enable_supplemental_cli = schemas.BoolSchema
            enable_wireless_onboarding = schemas.BoolSchema
            enable_password_for_exos_voss = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "org_id": org_id,
                "enable_copilot": enable_copilot,
                "enable_ssh": enable_ssh,
                "enable_supplemental_cli": enable_supplemental_cli,
                "enable_wireless_onboarding": enable_wireless_onboarding,
                "enable_password_for_exos_voss": enable_password_for_exos_voss,
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
    def __getitem__(self, name: typing_extensions.Literal["enable_copilot"]) -> MetaOapg.properties.enable_copilot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_ssh"]) -> MetaOapg.properties.enable_ssh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_supplemental_cli"]) -> MetaOapg.properties.enable_supplemental_cli: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_wireless_onboarding"]) -> MetaOapg.properties.enable_wireless_onboarding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_password_for_exos_voss"]) -> MetaOapg.properties.enable_password_for_exos_voss: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "org_id", "enable_copilot", "enable_ssh", "enable_supplemental_cli", "enable_wireless_onboarding", "enable_password_for_exos_voss", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["enable_copilot"]) -> typing.Union[MetaOapg.properties.enable_copilot, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_ssh"]) -> typing.Union[MetaOapg.properties.enable_ssh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_supplemental_cli"]) -> typing.Union[MetaOapg.properties.enable_supplemental_cli, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_wireless_onboarding"]) -> typing.Union[MetaOapg.properties.enable_wireless_onboarding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_password_for_exos_voss"]) -> typing.Union[MetaOapg.properties.enable_password_for_exos_voss, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "org_id", "enable_copilot", "enable_ssh", "enable_supplemental_cli", "enable_wireless_onboarding", "enable_password_for_exos_voss", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enable_copilot: typing.Union[MetaOapg.properties.enable_copilot, bool, schemas.Unset] = schemas.unset,
        enable_ssh: typing.Union[MetaOapg.properties.enable_ssh, bool, schemas.Unset] = schemas.unset,
        enable_supplemental_cli: typing.Union[MetaOapg.properties.enable_supplemental_cli, bool, schemas.Unset] = schemas.unset,
        enable_wireless_onboarding: typing.Union[MetaOapg.properties.enable_wireless_onboarding, bool, schemas.Unset] = schemas.unset,
        enable_password_for_exos_voss: typing.Union[MetaOapg.properties.enable_password_for_exos_voss, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqVhmSetting':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            org_id=org_id,
            enable_copilot=enable_copilot,
            enable_ssh=enable_ssh,
            enable_supplemental_cli=enable_supplemental_cli,
            enable_wireless_onboarding=enable_wireless_onboarding,
            enable_password_for_exos_voss=enable_password_for_exos_voss,
            _configuration=_configuration,
            **kwargs,
        )
