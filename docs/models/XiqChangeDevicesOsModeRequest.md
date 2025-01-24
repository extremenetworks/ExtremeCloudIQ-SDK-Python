# extremecloudiq.model.xiq_change_devices_os_mode_request.XiqChangeDevicesOsModeRequest

The request for change the device(s) OS mode.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for change the device(s) OS mode. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**target_os** | str,  | str,  | The target OS mode to change to, for AP: only WiNG is supported, for Switch: EXOS or VOSS | 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \&quot;AP_410C\&quot;, \&quot;AP_460C\&quot;, \&quot;AP_305C\&quot;, \&quot;AP_305CX\&quot;, \&quot;AP_460S6C\&quot;, \&quot;AP_460S12C\&quot;, \&quot;AP_302W\&quot; are allowed change to WiNG OS. For Switch: only \&quot;5520\&quot;, \&quot;5420F\&quot;, \&quot;5420M\&quot; are allowed to change its OS type. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_ids

The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \"AP_410C\", \"AP_460C\", \"AP_305C\", \"AP_305CX\", \"AP_460S6C\", \"AP_460S12C\", \"AP_302W\" are allowed change to WiNG OS. For Switch: only \"5520\", \"5420F\", \"5420M\" are allowed to change its OS type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \&quot;AP_410C\&quot;, \&quot;AP_460C\&quot;, \&quot;AP_305C\&quot;, \&quot;AP_305CX\&quot;, \&quot;AP_460S6C\&quot;, \&quot;AP_460S12C\&quot;, \&quot;AP_302W\&quot; are allowed change to WiNG OS. For Switch: only \&quot;5520\&quot;, \&quot;5420F\&quot;, \&quot;5420M\&quot; are allowed to change its OS type. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \&quot;AP_410C\&quot;, \&quot;AP_460C\&quot;, \&quot;AP_305C\&quot;, \&quot;AP_305CX\&quot;, \&quot;AP_460S6C\&quot;, \&quot;AP_460S12C\&quot;, \&quot;AP_302W\&quot; are allowed change to WiNG OS. For Switch: only \&quot;5520\&quot;, \&quot;5420F\&quot;, \&quot;5420M\&quot; are allowed to change its OS type. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

