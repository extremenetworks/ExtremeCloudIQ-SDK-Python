# extremecloudiq.model.xiq_mac_firewall_policy_request.XiqMacFirewallPolicyRequest

The MAC Firewall policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The MAC Firewall policy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The MAC firewall policy name | [optional] 
**description** | str,  | str,  | The MAC firewall policy description. | [optional] 
**[rules](#rules)** | list, tuple,  | tuple,  | List of MAC Firewall Rules | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

List of MAC Firewall Rules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of MAC Firewall Rules | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqMacFirewallRuleRequest**](XiqMacFirewallRuleRequest.md) | [**XiqMacFirewallRuleRequest**](XiqMacFirewallRuleRequest.md) | [**XiqMacFirewallRuleRequest**](XiqMacFirewallRuleRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

