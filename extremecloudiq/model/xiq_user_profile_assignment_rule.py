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


class XiqUserProfileAssignmentRule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The SSID user profile assignment rules.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def user_profile() -> typing.Type['XiqUserProfile']:
                return XiqUserProfile
        
            @staticmethod
            def user_profile_assignment() -> typing.Type['XiqUserProfileAssignment']:
                return XiqUserProfileAssignment
            enable_by_cwp = schemas.BoolSchema
            __annotations__ = {
                "user_profile": user_profile,
                "user_profile_assignment": user_profile_assignment,
                "enable_by_cwp": enable_by_cwp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_profile"]) -> 'XiqUserProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_profile_assignment"]) -> 'XiqUserProfileAssignment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_by_cwp"]) -> MetaOapg.properties.enable_by_cwp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_profile", "user_profile_assignment", "enable_by_cwp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_profile"]) -> typing.Union['XiqUserProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_profile_assignment"]) -> typing.Union['XiqUserProfileAssignment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_by_cwp"]) -> typing.Union[MetaOapg.properties.enable_by_cwp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_profile", "user_profile_assignment", "enable_by_cwp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_profile: typing.Union['XiqUserProfile', schemas.Unset] = schemas.unset,
        user_profile_assignment: typing.Union['XiqUserProfileAssignment', schemas.Unset] = schemas.unset,
        enable_by_cwp: typing.Union[MetaOapg.properties.enable_by_cwp, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUserProfileAssignmentRule':
        return super().__new__(
            cls,
            *_args,
            user_profile=user_profile,
            user_profile_assignment=user_profile_assignment,
            enable_by_cwp=enable_by_cwp,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_user_profile import XiqUserProfile
from extremecloudiq.model.xiq_user_profile_assignment import XiqUserProfileAssignment
