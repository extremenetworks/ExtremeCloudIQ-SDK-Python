# extremecloudiq.model.xiq_capture_location.XiqCaptureLocation

This represents the options for location packet capture.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This represents the options for location packet capture. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**direction** | [**XiqCaptureDirectionSelection**](XiqCaptureDirectionSelection.md) | [**XiqCaptureDirectionSelection**](XiqCaptureDirectionSelection.md) |  | [optional] 
**radio** | [**XiqCaptureRadioSelection**](XiqCaptureRadioSelection.md) | [**XiqCaptureRadioSelection**](XiqCaptureRadioSelection.md) |  | [optional] 
**wired_interface** | [**XiqCaptureWiredSelection**](XiqCaptureWiredSelection.md) | [**XiqCaptureWiredSelection**](XiqCaptureWiredSelection.md) |  | [optional] 
**wireless_band** | [**XiqCaptureBandSelection**](XiqCaptureBandSelection.md) | [**XiqCaptureBandSelection**](XiqCaptureBandSelection.md) |  | [optional] 
**[wired_filters](#wired_filters)** | list, tuple,  | tuple,  | The list of pre-defined wired filters for packet capture | [optional] 
**[wireless_filters](#wireless_filters)** | list, tuple,  | tuple,  | The list of pre-defined wireless filters for packet capture | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# wired_filters

The list of pre-defined wired filters for packet capture

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of pre-defined wired filters for packet capture | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWiredFilterType**](XiqWiredFilterType.md) | [**XiqWiredFilterType**](XiqWiredFilterType.md) | [**XiqWiredFilterType**](XiqWiredFilterType.md) |  | 

# wireless_filters

The list of pre-defined wireless filters for packet capture

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of pre-defined wireless filters for packet capture | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWirelessFilterType**](XiqWirelessFilterType.md) | [**XiqWirelessFilterType**](XiqWirelessFilterType.md) | [**XiqWirelessFilterType**](XiqWirelessFilterType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

