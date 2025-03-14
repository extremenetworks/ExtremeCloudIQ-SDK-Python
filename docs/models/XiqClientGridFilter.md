# extremecloudiq.model.xiq_client_grid_filter.XiqClientGridFilter

Request body for Client Grid Filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request body for Client Grid Filter | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | The site ids | [optional] 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The device ids | [optional] 
**[number_filter](#number_filter)** | list, tuple,  | tuple,  | The health status | [optional] 
**[alias](#alias)** | list, tuple,  | tuple,  | The aliases | [optional] 
**[auth_methods](#auth_methods)** | list, tuple,  | tuple,  | The authentication methods | [optional] 
**[encryption_methods](#encryption_methods)** | list, tuple,  | tuple,  | The encryption methods | [optional] 
**[operating_systems](#operating_systems)** | list, tuple,  | tuple,  | The operating systems | [optional] 
**[ssids](#ssids)** | list, tuple,  | tuple,  | The SSIDs | [optional] 
**[user_profiles](#user_profiles)** | list, tuple,  | tuple,  | The user profile names | [optional] 
**[frequency](#frequency)** | list, tuple,  | tuple,  | The frequency | [optional] 
**[category_assignments](#category_assignments)** | list, tuple,  | tuple,  | The category assignments | [optional] 
**has_authentication_issues** | bool,  | BoolClass,  | Flag to check authentication issues | [optional] 
**has_association_issues** | bool,  | BoolClass,  | Flag to check association issues | [optional] 
**has_ip_address_issues** | bool,  | BoolClass,  | Flag to check ip address issues | [optional] 
**has_roaming_issues** | bool,  | BoolClass,  | Flag to check roaming issues | [optional] 
**is_client_unhealthy** | bool,  | BoolClass,  | Flag to check unhealthy clients | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_ids

The site ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The site ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The site ids | value must be a 64 bit integer

# device_ids

The device ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The device ids | value must be a 64 bit integer

# number_filter

The health status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The health status | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqNumberFilter**](XiqNumberFilter.md) | [**XiqNumberFilter**](XiqNumberFilter.md) | [**XiqNumberFilter**](XiqNumberFilter.md) |  | 

# alias

The aliases

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The aliases | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The aliases | 

# auth_methods

The authentication methods

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The authentication methods | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The authentication methods | 

# encryption_methods

The encryption methods

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The encryption methods | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The encryption methods | 

# operating_systems

The operating systems

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The operating systems | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The operating systems | 

# ssids

The SSIDs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The SSIDs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The SSIDs | 

# user_profiles

The user profile names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The user profile names | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The user profile names | 

# frequency

The frequency

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The frequency | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The frequency | 

# category_assignments

The category assignments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The category assignments | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The category assignments | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

