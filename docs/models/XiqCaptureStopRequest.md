# extremecloudiq.model.xiq_capture_stop_request.XiqCaptureStopRequest

The IDs of the devices for which the active packet capture is to be stopped. If empty, packet capture is to be stopped on all devices in this packet capture.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The IDs of the devices for which the active packet capture is to be stopped. If empty, packet capture is to be stopped on all devices in this packet capture. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The IDs of the devices for which the active packet capture is to be stopped. If empty, packet capture is to be stopped on all devices in this packet capture. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_ids

The IDs of the devices for which the active packet capture is to be stopped. If empty, packet capture is to be stopped on all devices in this packet capture.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The IDs of the devices for which the active packet capture is to be stopped. If empty, packet capture is to be stopped on all devices in this packet capture. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The IDs of the devices for which the active packet capture is to be stopped. If empty, packet capture is to be stopped on all devices in this packet capture. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

