# extremecloudiq.model.xiq_qoe_metadata_device_filter.XiqQoeMetadataDeviceFilter

The Request Body Device Metadata 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Request Body Device Metadata  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | The list of Site Ids | [optional] 
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | The list of Building Ids | [optional] 
**[floor_ids](#floor_ids)** | list, tuple,  | tuple,  | The list of Floor Ids | [optional] 
**[ssids](#ssids)** | list, tuple,  | tuple,  | The list of ssids | [optional] 
**[bands](#bands)** | list, tuple,  | tuple,  | The list of bands | [optional] 
**[channels](#channels)** | list, tuple,  | tuple,  | The list of channels | [optional] 
**[os_types](#os_types)** | list, tuple,  | tuple,  | The list of os_types | [optional] 
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

# bands

The list of bands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of bands | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) |  | 

# channels

The list of channels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of channels | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of channels | value must be a 32 bit integer

# os_types

The list of os_types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of os_types | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The list of os_types | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

