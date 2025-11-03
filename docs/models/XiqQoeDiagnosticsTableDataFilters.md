# extremecloudiq.model.xiq_qoe_diagnostics_table_data_filters.XiqQoeDiagnosticsTableDataFilters

metrics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | metrics | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[floor_ids](#floor_ids)** | list, tuple,  | tuple,  | The list of Floor Ids | 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | Start Time in epoch milliseconds | value must be a 64 bit integer
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | The list of Site Ids | 
**sort_field** | str,  | str,  | Sort Field | must be one of ["TIME_STAMP", "MAC", "HOSTNAME", "SESSION_DURATION", "CONNECTED_TIME", "DISCONNECTED_TIME", "TOTAL_DATA_USAGE", "RELATIVE_TIME", "TOTAL_POWER_USAGE", "IDLE_POWER", "MAX_POWER", "AVG_POWER", "APPLICATION_USAGE", "PERCENTAGE_CHANNEL_UTILIZATION", "PERCENTAGE_AIRTIME_UTILIZATION", "ERROR_TIMESTAMP", "NETWORK_USAGE", "RETRY_COUNT", "FAILED_ROAM_DATE_AND_TIME", "LAST_AP_HOSTNAME", "FROM_AP_HOSTNAME", "TO_AP_HOSTNAME", "FAILURE_TIME_STAMP", "PORT_SPEED", "DEVICE_DOWN_DATE_AND_TIME", "DOWN_TIME", "LOGIN_DATE_AND_TIME", "LOGIN_DURATION", "AUTHENTICATION_DATE_TIME", "USB_POWER_CONSUMED", "ALERT_DATE_TIME", "DFS_CHANNEL_CHANGE_DATE_AND_TIME", "ACSP_CHANGE_DATE_AND_TIME", "DATE_AND_TIME", "PERCENTAGE_CONGESTION", ] if omitted the server will use the default value of "TIME_STAMP"
**end_time** | decimal.Decimal, int,  | decimal.Decimal,  | End Time in epoch milliseconds | value must be a 64 bit integer
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | The list of Building Ids | 
**metrics** | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) |  | 
**sort_order** | [**XiqSortOrder**](XiqSortOrder.md) | [**XiqSortOrder**](XiqSortOrder.md) |  | 
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
**page_no** | decimal.Decimal, int,  | decimal.Decimal,  | page no | [optional] if omitted the server will use the default value of 1value must be a 32 bit integer
**limit** | decimal.Decimal, int,  | decimal.Decimal,  | limit | [optional] if omitted the server will use the default value of 1value must be a 32 bit integer
**export_data** | bool,  | BoolClass,  | export data | [optional] if omitted the server will use the default value of False
**search_parameter** | str,  | str,  | search parameter | [optional] 
**async** | bool,  | BoolClass,  | LRO Call | [optional] if omitted the server will use the default value of False
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

