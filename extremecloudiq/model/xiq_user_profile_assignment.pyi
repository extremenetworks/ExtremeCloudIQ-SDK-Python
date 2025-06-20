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


class XiqUserProfileAssignment(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload of User Profile Assignment
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
            name = schemas.StrSchema
            description = schemas.StrSchema
            authorisation_policy = schemas.StrSchema
            
            
            class folder_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'folder_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def assignment_radius_attribute() -> typing.Type['XiqUserProfileAssignmentRadiusAttribute']:
                return XiqUserProfileAssignmentRadiusAttribute
            
            
            class user_group(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqUserGroup']:
                        return XiqUserGroup
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqUserGroup'], typing.List['XiqUserGroup']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'user_group':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqUserGroup':
                    return super().__getitem__(i)
            
            
            class mac_object_profiles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqMacObject']:
                        return XiqMacObject
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqMacObject'], typing.List['XiqMacObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mac_object_profiles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqMacObject':
                    return super().__getitem__(i)
            
            
            class os_object_dhcp(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqOsObject']:
                        return XiqOsObject
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqOsObject'], typing.List['XiqOsObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'os_object_dhcp':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqOsObject':
                    return super().__getitem__(i)
            
            
            class os_object_https(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqOsObject']:
                        return XiqOsObject
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqOsObject'], typing.List['XiqOsObject']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'os_object_https':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqOsObject':
                    return super().__getitem__(i)
            
            
            class schedules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqSchedule']:
                        return XiqSchedule
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqSchedule'], typing.List['XiqSchedule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'schedules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqSchedule':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "org_id": org_id,
                "name": name,
                "description": description,
                "authorisation_policy": authorisation_policy,
                "folder_ids": folder_ids,
                "assignment_radius_attribute": assignment_radius_attribute,
                "user_group": user_group,
                "mac_object_profiles": mac_object_profiles,
                "os_object_dhcp": os_object_dhcp,
                "os_object_https": os_object_https,
                "schedules": schedules,
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
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorisation_policy"]) -> MetaOapg.properties.authorisation_policy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_ids"]) -> MetaOapg.properties.folder_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assignment_radius_attribute"]) -> 'XiqUserProfileAssignmentRadiusAttribute': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_group"]) -> MetaOapg.properties.user_group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_object_profiles"]) -> MetaOapg.properties.mac_object_profiles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_object_dhcp"]) -> MetaOapg.properties.os_object_dhcp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os_object_https"]) -> MetaOapg.properties.os_object_https: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedules"]) -> MetaOapg.properties.schedules: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "org_id", "name", "description", "authorisation_policy", "folder_ids", "assignment_radius_attribute", "user_group", "mac_object_profiles", "os_object_dhcp", "os_object_https", "schedules", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorisation_policy"]) -> typing.Union[MetaOapg.properties.authorisation_policy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_ids"]) -> typing.Union[MetaOapg.properties.folder_ids, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assignment_radius_attribute"]) -> typing.Union['XiqUserProfileAssignmentRadiusAttribute', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_group"]) -> typing.Union[MetaOapg.properties.user_group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_object_profiles"]) -> typing.Union[MetaOapg.properties.mac_object_profiles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_object_dhcp"]) -> typing.Union[MetaOapg.properties.os_object_dhcp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os_object_https"]) -> typing.Union[MetaOapg.properties.os_object_https, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedules"]) -> typing.Union[MetaOapg.properties.schedules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "org_id", "name", "description", "authorisation_policy", "folder_ids", "assignment_radius_attribute", "user_group", "mac_object_profiles", "os_object_dhcp", "os_object_https", "schedules", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        authorisation_policy: typing.Union[MetaOapg.properties.authorisation_policy, str, schemas.Unset] = schemas.unset,
        folder_ids: typing.Union[MetaOapg.properties.folder_ids, list, tuple, schemas.Unset] = schemas.unset,
        assignment_radius_attribute: typing.Union['XiqUserProfileAssignmentRadiusAttribute', schemas.Unset] = schemas.unset,
        user_group: typing.Union[MetaOapg.properties.user_group, list, tuple, schemas.Unset] = schemas.unset,
        mac_object_profiles: typing.Union[MetaOapg.properties.mac_object_profiles, list, tuple, schemas.Unset] = schemas.unset,
        os_object_dhcp: typing.Union[MetaOapg.properties.os_object_dhcp, list, tuple, schemas.Unset] = schemas.unset,
        os_object_https: typing.Union[MetaOapg.properties.os_object_https, list, tuple, schemas.Unset] = schemas.unset,
        schedules: typing.Union[MetaOapg.properties.schedules, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqUserProfileAssignment':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            id=id,
            org_id=org_id,
            name=name,
            description=description,
            authorisation_policy=authorisation_policy,
            folder_ids=folder_ids,
            assignment_radius_attribute=assignment_radius_attribute,
            user_group=user_group,
            mac_object_profiles=mac_object_profiles,
            os_object_dhcp=os_object_dhcp,
            os_object_https=os_object_https,
            schedules=schedules,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_mac_object import XiqMacObject
from extremecloudiq.model.xiq_os_object import XiqOsObject
from extremecloudiq.model.xiq_schedule import XiqSchedule
from extremecloudiq.model.xiq_user_group import XiqUserGroup
from extremecloudiq.model.xiq_user_profile_assignment_radius_attribute import XiqUserProfileAssignmentRadiusAttribute
