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


class XiqDeploymentStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The configuration deployment status
    """


    class MetaOapg:
        required = {
            "is_finished",
        }
        
        class properties:
            is_finished = schemas.BoolSchema
            current_progress = schemas.Int32Schema
            current_step_code = schemas.StrSchema
            current_step_message = schemas.StrSchema
            is_finished_successful = schemas.BoolSchema
            last_deploy_time = schemas.Int64Schema
            status_message = schemas.StrSchema
            is_pending_config = schemas.BoolSchema
            __annotations__ = {
                "is_finished": is_finished,
                "current_progress": current_progress,
                "current_step_code": current_step_code,
                "current_step_message": current_step_message,
                "is_finished_successful": is_finished_successful,
                "last_deploy_time": last_deploy_time,
                "status_message": status_message,
                "is_pending_config": is_pending_config,
            }
    
    is_finished: MetaOapg.properties.is_finished
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_finished"]) -> MetaOapg.properties.is_finished: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_progress"]) -> MetaOapg.properties.current_progress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_step_code"]) -> MetaOapg.properties.current_step_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_step_message"]) -> MetaOapg.properties.current_step_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_finished_successful"]) -> MetaOapg.properties.is_finished_successful: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_deploy_time"]) -> MetaOapg.properties.last_deploy_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_message"]) -> MetaOapg.properties.status_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_pending_config"]) -> MetaOapg.properties.is_pending_config: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_finished", "current_progress", "current_step_code", "current_step_message", "is_finished_successful", "last_deploy_time", "status_message", "is_pending_config", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_finished"]) -> MetaOapg.properties.is_finished: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_progress"]) -> typing.Union[MetaOapg.properties.current_progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_step_code"]) -> typing.Union[MetaOapg.properties.current_step_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_step_message"]) -> typing.Union[MetaOapg.properties.current_step_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_finished_successful"]) -> typing.Union[MetaOapg.properties.is_finished_successful, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_deploy_time"]) -> typing.Union[MetaOapg.properties.last_deploy_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_message"]) -> typing.Union[MetaOapg.properties.status_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_pending_config"]) -> typing.Union[MetaOapg.properties.is_pending_config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_finished", "current_progress", "current_step_code", "current_step_message", "is_finished_successful", "last_deploy_time", "status_message", "is_pending_config", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_finished: typing.Union[MetaOapg.properties.is_finished, bool, ],
        current_progress: typing.Union[MetaOapg.properties.current_progress, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        current_step_code: typing.Union[MetaOapg.properties.current_step_code, str, schemas.Unset] = schemas.unset,
        current_step_message: typing.Union[MetaOapg.properties.current_step_message, str, schemas.Unset] = schemas.unset,
        is_finished_successful: typing.Union[MetaOapg.properties.is_finished_successful, bool, schemas.Unset] = schemas.unset,
        last_deploy_time: typing.Union[MetaOapg.properties.last_deploy_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status_message: typing.Union[MetaOapg.properties.status_message, str, schemas.Unset] = schemas.unset,
        is_pending_config: typing.Union[MetaOapg.properties.is_pending_config, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqDeploymentStatus':
        return super().__new__(
            cls,
            *_args,
            is_finished=is_finished,
            current_progress=current_progress,
            current_step_code=current_step_code,
            current_step_message=current_step_message,
            is_finished_successful=is_finished_successful,
            last_deploy_time=last_deploy_time,
            status_message=status_message,
            is_pending_config=is_pending_config,
            _configuration=_configuration,
            **kwargs,
        )
