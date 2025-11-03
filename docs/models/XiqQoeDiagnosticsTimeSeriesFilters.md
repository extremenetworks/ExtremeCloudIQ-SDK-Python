# extremecloudiq.model.xiq_qoe_diagnostics_time_series_filters.XiqQoeDiagnosticsTimeSeriesFilters

metrics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | metrics | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**async** | bool,  | BoolClass,  | LRO Call | if omitted the server will use the default value of False
**[floor_ids](#floor_ids)** | list, tuple,  | tuple,  | The list of Floor Ids | 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Start Time in epoch milliseconds | value must be a 64 bit integer
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | The list of Site Ids | 
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | End Time in epoch milliseconds | value must be a 64 bit integer
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | The list of Building Ids | 
**metrics** | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) |  | 
**[bands](#bands)** | list, tuple,  | tuple,  | List of bands | [optional] 
**[contypes](#contypes)** | list, tuple,  | tuple,  | List of Connection Types | [optional] 
**[devicetypes](#devicetypes)** | list, tuple,  | tuple,  | List of device types | [optional] 
**[vlan_ids](#vlan_ids)** | list, tuple,  | tuple,  | The list of vlan Ids | [optional] 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The list of device Ids | [optional] 
**[ssids](#ssids)** | list, tuple,  | tuple,  | The list of ssids | [optional] 
**[user_names](#user_names)** | list, tuple,  | tuple,  | The list of usernames | [optional] 
**[client_macs](#client_macs)** | list, tuple,  | tuple,  | The list of client MACs | [optional] 
**[port_nums](#port_nums)** | list, tuple,  | tuple,  | The list of port numbers | [optional] 
**[app_ids](#app_ids)** | list, tuple,  | tuple,  | The list of application Ids | [optional] 
**[channel_nums](#channel_nums)** | list, tuple,  | tuple,  | The list of channel numbers | [optional] 
**[admin_roles](#admin_roles)** | list, tuple,  | tuple,  | The list of Admin Roles | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | page Value | [optional] value must be a 32 bit integer
**limit** | decimal.Decimal, int,  | decimal.Decimal,  | limit Value | [optional] value must be a 32 bit integer
**[os_types](#os_types)** | list, tuple,  | tuple,  |  | [optional] 
**isSSIDSelected** | bool,  | BoolClass,  | is ssid filter applied | [optional] if omitted the server will use the default value of True
**isBandSelected** | bool,  | BoolClass,  | is band filter applied | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_ids

The list of Site Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Site Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of Site Ids | value must be a 64 bit integer

# floor_ids

The list of Floor Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Floor Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of Floor Ids | value must be a 64 bit integer

# building_ids

The list of Building Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Building Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of Building Ids | value must be a 64 bit integer

# bands

List of bands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of bands | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) |  | 

# contypes

List of Connection Types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Connection Types | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqQoeDiagnosticsConnTypes**](XiqQoeDiagnosticsConnTypes.md) | [**XiqQoeDiagnosticsConnTypes**](XiqQoeDiagnosticsConnTypes.md) | [**XiqQoeDiagnosticsConnTypes**](XiqQoeDiagnosticsConnTypes.md) |  | 

# devicetypes

List of device types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device types | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqQoeDiagnosticsDeviceTypes**](XiqQoeDiagnosticsDeviceTypes.md) | [**XiqQoeDiagnosticsDeviceTypes**](XiqQoeDiagnosticsDeviceTypes.md) | [**XiqQoeDiagnosticsDeviceTypes**](XiqQoeDiagnosticsDeviceTypes.md) |  | 

# vlan_ids

The list of vlan Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of vlan Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of vlan Ids | value must be a 32 bit integer

# device_ids

The list of device Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of device Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of device Ids | value must be a 64 bit integer

# ssids

The list of ssids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of ssids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The list of ssids | 

# user_names

The list of usernames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of usernames | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The list of usernames | 

# client_macs

The list of client MACs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of client MACs | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The list of client MACs | 

# port_nums

The list of port numbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of port numbers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of port numbers | value must be a 64 bit integer

# app_ids

The list of application Ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of application Ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of application Ids | value must be a 64 bit integer

# channel_nums

The list of channel numbers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of channel numbers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of channel numbers | value must be a 32 bit integer

# admin_roles

The list of Admin Roles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Admin Roles | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of Admin Roles | value must be a 64 bit integer

# os_types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

