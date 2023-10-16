# XiqCaptureFilter

The filter criteria for packet capture
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_addr** | **list[str]** | List of the client MAC addresses used for packet capturing | [optional] 
**ip_addr** | **list[str]** | List of  the client IP addresses used to filter the packets | [optional] 
**protocol** | [**XiqPolicyRuleProtocolType**](XiqPolicyRuleProtocolType.md) |  | [optional] 
**protocol_number** | **int** | The protocol number if protocol is \&quot;USER_DEFINED\&quot; | [optional] 
**port** | **int** | The port for packet capture | [optional] 
**vlan** | **str** | Specific vlan ids in a string, e.g. range \&quot;2-100\&quot;; single \&quot;3\&quot;; list \&quot;1,2,5,7,122\&quot;; mixed \&quot;2,4,5-10,19,29\&quot;. If not specified, default is all VLANs. | [optional] 
**wlan** | **str** | A WLAN SSID. If not specified, default is all WLANs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


