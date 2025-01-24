# extremecloudiq.model.xiq_hotspot_qos_map.XiqHotspotQosMap

Quality of Service (QoS) map for Hotspot profile.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Quality of Service (QoS) map for Hotspot profile. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[dscp_ranges](#dscp_ranges)** | list, tuple,  | tuple,  | A list of ah-class to DSCP range. | [optional] 
**[dscp_exceptions](#dscp_exceptions)** | list, tuple,  | tuple,  | The list of exceptions to the mapping of ah-class to DSCP values. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dscp_ranges

A list of ah-class to DSCP range.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of ah-class to DSCP range. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotQosAhClassToDscpRange**](XiqHotspotQosAhClassToDscpRange.md) | [**XiqHotspotQosAhClassToDscpRange**](XiqHotspotQosAhClassToDscpRange.md) | [**XiqHotspotQosAhClassToDscpRange**](XiqHotspotQosAhClassToDscpRange.md) |  | 

# dscp_exceptions

The list of exceptions to the mapping of ah-class to DSCP values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of exceptions to the mapping of ah-class to DSCP values. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotQosDscpException**](XiqHotspotQosDscpException.md) | [**XiqHotspotQosDscpException**](XiqHotspotQosDscpException.md) | [**XiqHotspotQosDscpException**](XiqHotspotQosDscpException.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

