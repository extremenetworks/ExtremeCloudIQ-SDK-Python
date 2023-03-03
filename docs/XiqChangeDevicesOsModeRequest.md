# XiqChangeDevicesOsModeRequest

The request for change the device(s) OS mode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **list[int]** | The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \&quot;AP_410C\&quot;, \&quot;AP_460C\&quot;, \&quot;AP_305C\&quot;, \&quot;AP_305CX\&quot;, \&quot;AP_460S6C\&quot;, \&quot;AP_460S12C\&quot;, \&quot;AP_302W\&quot; are allowed change to WiNG OS. For Switch: only \&quot;5520\&quot;, \&quot;5420F\&quot;, \&quot;5420M\&quot; are allowed to change its OS type. | 
**target_os** | **str** | The target OS mode to change to, for AP: only WiNG is supported, for Switch: EXOS or VOSS | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


