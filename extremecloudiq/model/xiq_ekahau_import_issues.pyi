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


class XiqEkahauImportIssues(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Any issues related to the import of this floor, eg: why it failed, why an AP was discarded, etc.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def floor() -> typing.Type['XiqEkahauImportIssue']:
                return XiqEkahauImportIssue
        
            @staticmethod
            def background() -> typing.Type['XiqEkahauImportIssue']:
                return XiqEkahauImportIssue
            
            
            class custom_ap_configurations(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['XiqEkahauImportIssue']:
                                return XiqEkahauImportIssue
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['XiqEkahauImportIssue'], typing.List['XiqEkahauImportIssue']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'XiqEkahauImportIssue':
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'custom_ap_configurations':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class discarded_aps(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['XiqEkahauImportIssue']:
                        return XiqEkahauImportIssue
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'XiqEkahauImportIssue':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'XiqEkahauImportIssue':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'XiqEkahauImportIssue',
                ) -> 'discarded_aps':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class discarded_walls(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['XiqEkahauImportIssue']:
                        return XiqEkahauImportIssue
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'XiqEkahauImportIssue':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'XiqEkahauImportIssue':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'XiqEkahauImportIssue',
                ) -> 'discarded_walls':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "floor": floor,
                "background": background,
                "custom_ap_configurations": custom_ap_configurations,
                "discarded_aps": discarded_aps,
                "discarded_walls": discarded_walls,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["floor"]) -> 'XiqEkahauImportIssue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["background"]) -> 'XiqEkahauImportIssue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_ap_configurations"]) -> MetaOapg.properties.custom_ap_configurations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discarded_aps"]) -> MetaOapg.properties.discarded_aps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discarded_walls"]) -> MetaOapg.properties.discarded_walls: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["floor", "background", "custom_ap_configurations", "discarded_aps", "discarded_walls", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["floor"]) -> typing.Union['XiqEkahauImportIssue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["background"]) -> typing.Union['XiqEkahauImportIssue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_ap_configurations"]) -> typing.Union[MetaOapg.properties.custom_ap_configurations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discarded_aps"]) -> typing.Union[MetaOapg.properties.discarded_aps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discarded_walls"]) -> typing.Union[MetaOapg.properties.discarded_walls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["floor", "background", "custom_ap_configurations", "discarded_aps", "discarded_walls", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        floor: typing.Union['XiqEkahauImportIssue', schemas.Unset] = schemas.unset,
        background: typing.Union['XiqEkahauImportIssue', schemas.Unset] = schemas.unset,
        custom_ap_configurations: typing.Union[MetaOapg.properties.custom_ap_configurations, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        discarded_aps: typing.Union[MetaOapg.properties.discarded_aps, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        discarded_walls: typing.Union[MetaOapg.properties.discarded_walls, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqEkahauImportIssues':
        return super().__new__(
            cls,
            *_args,
            floor=floor,
            background=background,
            custom_ap_configurations=custom_ap_configurations,
            discarded_aps=discarded_aps,
            discarded_walls=discarded_walls,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_ekahau_import_issue import XiqEkahauImportIssue
