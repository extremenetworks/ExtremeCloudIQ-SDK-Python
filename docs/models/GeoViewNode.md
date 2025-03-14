# extremecloudiq.model.geo_view_node.GeoViewNode

Geo View Node

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Geo View Node | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**folder_id** | decimal.Decimal, int,  | decimal.Decimal,  | Folder ID | [optional] value must be a 64 bit integer
**folder_name** | str,  | str,  | Folder Name | [optional] 
**folder_type** | str,  | str,  | Folder Type | [optional] 
**total_children** | decimal.Decimal, int,  | decimal.Decimal,  | Total Children | [optional] value must be a 64 bit integer
**total_unhealthy_children** | decimal.Decimal, int,  | decimal.Decimal,  | Total Unhealthy Children | [optional] value must be a 64 bit integer
**[folders](#folders)** | list, tuple,  | tuple,  | List of Children | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# folders

List of Children

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Children | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GeoViewNode**](GeoViewNode.md) | [**GeoViewNode**](GeoViewNode.md) | [**GeoViewNode**](GeoViewNode.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

