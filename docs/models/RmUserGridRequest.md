# extremecloudiq.model.rm_user_grid_request.RmUserGridRequest

User Grid Request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User Grid Request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[user_name](#user_name)** | list, tuple,  | tuple,  | The User Names | [optional] 
**[source](#source)** | list, tuple,  | tuple,  | The source list | [optional] 
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | The site IDs | [optional] 
**status** | bool,  | BoolClass,  | The status | [optional] 
**[duration](#duration)** | list, tuple,  | tuple,  | The duration filter list | [optional] 
**[user_ids](#user_ids)** | list, tuple,  | tuple,  | The User IDs | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_name

The User Names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The User Names | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The User Names | 

# source

The source list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The source list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The source list | 

# site_ids

The site IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The site IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The site IDs | value must be a 64 bit integer

# duration

The duration filter list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The duration filter list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RmUserNumberFilter**](RmUserNumberFilter.md) | [**RmUserNumberFilter**](RmUserNumberFilter.md) | [**RmUserNumberFilter**](RmUserNumberFilter.md) |  | 

# user_ids

The User IDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The User IDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The User IDs | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

