# extremecloudiq.model.xiq_rp_miscellaneous_settings.XiqRpMiscellaneousSettings

The payload of config for the radio profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of config for the radio profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**sla_throughput_level** | str,  | str,  | The Client SLA options -- \&quot;NORMAL_DENSITY\&quot;, \&quot;HIGH_DENSITY\&quot; (performance-oriented), or \&quot;LOW_DENSITY\&quot; (coverage-oriented) | [optional] 
**radio_range** | decimal.Decimal, int,  | decimal.Decimal,  | The Outdoor Deployment for signal distance from 300 to 10000 meters | [optional] value must be a 32 bit integer
**[wmm_qos_settings](#wmm_qos_settings)** | list, tuple,  | tuple,  | The WMM QoS settings for various media types | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# wmm_qos_settings

The WMM QoS settings for various media types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The WMM QoS settings for various media types | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRpWmmQosSettings**](XiqRpWmmQosSettings.md) | [**XiqRpWmmQosSettings**](XiqRpWmmQosSettings.md) | [**XiqRpWmmQosSettings**](XiqRpWmmQosSettings.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

