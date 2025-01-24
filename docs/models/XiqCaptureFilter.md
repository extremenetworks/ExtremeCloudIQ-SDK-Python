# extremecloudiq.model.xiq_capture_filter.XiqCaptureFilter

The filter criteria for packet capture

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The filter criteria for packet capture | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mac_addr](#mac_addr)** | list, tuple,  | tuple,  | List of the client MAC addresses used for packet capturing | [optional] 
**[ip_addr](#ip_addr)** | list, tuple,  | tuple,  | List of  the client IP addresses used to filter the packets | [optional] 
**protocol** | [**XiqPolicyRuleProtocolType**](XiqPolicyRuleProtocolType.md) | [**XiqPolicyRuleProtocolType**](XiqPolicyRuleProtocolType.md) |  | [optional] 
**protocol_number** | decimal.Decimal, int,  | decimal.Decimal,  | The protocol number if protocol is \&quot;USER_DEFINED\&quot; | [optional] value must be a 32 bit integer
**port** | decimal.Decimal, int,  | decimal.Decimal,  | The port for packet capture | [optional] value must be a 32 bit integer
**vlan** | str,  | str,  | Specific vlan ids in a string, e.g. range \&quot;2-100\&quot;; single \&quot;3\&quot;; list \&quot;1,2,5,7,122\&quot;; mixed \&quot;2,4,5-10,19,29\&quot;. If not specified, default is all VLANs. | [optional] 
**wlan** | str,  | str,  | A WLAN SSID. If not specified, default is all WLANs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mac_addr

List of the client MAC addresses used for packet capturing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the client MAC addresses used for packet capturing | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of the client MAC addresses used for packet capturing | 

# ip_addr

List of  the client IP addresses used to filter the packets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of  the client IP addresses used to filter the packets | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of  the client IP addresses used to filter the packets | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

