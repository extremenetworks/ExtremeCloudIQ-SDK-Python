# extremecloudiq.model.xiq_ip_firewall.XiqIpFirewall

IP Firewall policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | IP Firewall policy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The IP Firewall policy name | [optional] 
**description** | str,  | str,  | The IP Firewall policy description. | [optional] 
**[rules](#rules)** | list, tuple,  | tuple,  | List of IP Firewall Rules. | [optional] 
**predefined** | bool,  | BoolClass,  | Flag to describe whether the application is predefined or customized. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

List of IP Firewall Rules.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of IP Firewall Rules. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqIpFirewallRule**](XiqIpFirewallRule.md) | [**XiqIpFirewallRule**](XiqIpFirewallRule.md) | [**XiqIpFirewallRule**](XiqIpFirewallRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

