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


class XiqDeploymentRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The configuration/firmware update deployment request to devices.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def schedule() -> typing.Type['XiqScheduleDetails']:
                return XiqScheduleDetails
        
            @staticmethod
            def devices() -> typing.Type['XiqDeployDeviceFilter']:
                return XiqDeployDeviceFilter
        
            @staticmethod
            def policy() -> typing.Type['XiqDeploymentPolicy']:
                return XiqDeploymentPolicy
            __annotations__ = {
                "schedule": schedule,
                "devices": devices,
                "policy": policy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule"]) -> 'XiqScheduleDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["devices"]) -> 'XiqDeployDeviceFilter': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policy"]) -> 'XiqDeploymentPolicy': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schedule", "devices", "policy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule"]) -> typing.Union['XiqScheduleDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["devices"]) -> typing.Union['XiqDeployDeviceFilter', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policy"]) -> typing.Union['XiqDeploymentPolicy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schedule", "devices", "policy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        schedule: typing.Union['XiqScheduleDetails', schemas.Unset] = schemas.unset,
        devices: typing.Union['XiqDeployDeviceFilter', schemas.Unset] = schemas.unset,
        policy: typing.Union['XiqDeploymentPolicy', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeploymentRequest':
        return super().__new__(
            cls,
            *_args,
            schedule=schedule,
            devices=devices,
            policy=policy,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_deploy_device_filter import XiqDeployDeviceFilter
from extremecloudiq.model.xiq_deployment_policy import XiqDeploymentPolicy
from extremecloudiq.model.xiq_schedule_details import XiqScheduleDetails
