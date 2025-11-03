# extremecloudiq.model.xiq_rm_device_list_request.XiqRmDeviceListRequest

Request body for RM Device List

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request body for RM Device List | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | List of site ids to filter | [optional] 
**[sns](#sns)** | list, tuple,  | tuple,  | List of device serial numbers to filter | [optional] 
**[mac_addresses](#mac_addresses)** | list, tuple,  | tuple,  | List of device MAC addresses to filter | [optional] 
**[hostnames](#hostnames)** | list, tuple,  | tuple,  | List of device host names to filter | [optional] 
**[default_gateway_ips](#default_gateway_ips)** | list, tuple,  | tuple,  | List of device default gateway IPs to filter | [optional] 
**[product_types](#product_types)** | list, tuple,  | tuple,  | List of device product types to filter | [optional] 
**[firmware_versions](#firmware_versions)** | list, tuple,  | tuple,  | List of device firmware versions to filter | [optional] 
**[country_codes](#country_codes)** | list, tuple,  | tuple,  | List of country codes to filter | [optional] 
**[managed_by](#managed_by)** | list, tuple,  | tuple,  | List of entities managing the device to filter | [optional] 
**[network_policies](#network_policies)** | list, tuple,  | tuple,  | List of network policies to filter | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_ids

List of site ids to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of site ids to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of site ids to filter | value must be a 64 bit integer

# sns

List of device serial numbers to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device serial numbers to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of device serial numbers to filter | 

# mac_addresses

List of device MAC addresses to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device MAC addresses to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of device MAC addresses to filter | 

# hostnames

List of device host names to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device host names to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of device host names to filter | 

# default_gateway_ips

List of device default gateway IPs to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device default gateway IPs to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of device default gateway IPs to filter | 

# product_types

List of device product types to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device product types to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of device product types to filter | 

# firmware_versions

List of device firmware versions to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device firmware versions to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of device firmware versions to filter | 

# country_codes

List of country codes to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of country codes to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of country codes to filter | value must be a 32 bit integer

# managed_by

List of entities managing the device to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of entities managing the device to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of entities managing the device to filter | 

# network_policies

List of network policies to filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of network policies to filter | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of network policies to filter | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

