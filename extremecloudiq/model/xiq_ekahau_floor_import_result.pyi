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


class XiqEkahauFloorImportResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Result of importing an Ekahau floor
    """


    class MetaOapg:
        required = {
            "name",
            "issues",
            "status",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['XiqEkahauFloorImportStatus']:
                return XiqEkahauFloorImportStatus
        
            @staticmethod
            def issues() -> typing.Type['XiqEkahauImportIssues']:
                return XiqEkahauImportIssues
            __annotations__ = {
                "name": name,
                "status": status,
                "issues": issues,
            }
    
    name: MetaOapg.properties.name
    issues: 'XiqEkahauImportIssues'
    status: 'XiqEkahauFloorImportStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'XiqEkahauFloorImportStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues"]) -> 'XiqEkahauImportIssues': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "status", "issues", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'XiqEkahauFloorImportStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues"]) -> 'XiqEkahauImportIssues': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "status", "issues", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        issues: 'XiqEkahauImportIssues',
        status: 'XiqEkahauFloorImportStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqEkahauFloorImportResult':
        return super().__new__(
            cls,
            *_args,
            name=name,
            issues=issues,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_ekahau_floor_import_status import XiqEkahauFloorImportStatus
from extremecloudiq.model.xiq_ekahau_import_issues import XiqEkahauImportIssues
