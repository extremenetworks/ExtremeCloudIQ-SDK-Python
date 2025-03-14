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


class PagedXiqRadiusProxy(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "total_count",
            "count",
            "page",
            "total_pages",
        }
        
        class properties:
            page = schemas.Int32Schema
            count = schemas.Int32Schema
            total_pages = schemas.Int32Schema
            total_count = schemas.Int64Schema
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqRadiusProxy']:
                        return XiqRadiusProxy
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqRadiusProxy'], typing.List['XiqRadiusProxy']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqRadiusProxy':
                    return super().__getitem__(i)
            __annotations__ = {
                "page": page,
                "count": count,
                "total_pages": total_pages,
                "total_count": total_count,
                "data": data,
            }
    
    total_count: MetaOapg.properties.total_count
    count: MetaOapg.properties.count
    page: MetaOapg.properties.page
    total_pages: MetaOapg.properties.total_pages
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["page", "count", "total_pages", "total_count", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page", "count", "total_pages", "total_count", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, ],
        total_pages: typing.Union[MetaOapg.properties.total_pages, decimal.Decimal, int, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PagedXiqRadiusProxy':
        return super().__new__(
            cls,
            *_args,
            total_count=total_count,
            count=count,
            page=page,
            total_pages=total_pages,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_radius_proxy import XiqRadiusProxy
