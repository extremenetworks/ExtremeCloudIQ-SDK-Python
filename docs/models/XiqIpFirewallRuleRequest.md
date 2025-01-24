# extremecloudiq.model.xiq_ip_firewall_rule_request.XiqIpFirewallRuleRequest

List of IP Firewall Rules.....

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of IP Firewall Rules..... | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**action** | [**XiqIpFirewallAction**](XiqIpFirewallAction.md) | [**XiqIpFirewallAction**](XiqIpFirewallAction.md) |  | [optional] 
**service_id** | decimal.Decimal, int,  | decimal.Decimal,  | Application or Network Service ID for IP Firewall Rule. | [optional] value must be a 64 bit integer
**source_ip_id** | decimal.Decimal, int,  | decimal.Decimal,  | Source IP for IP Firewall Rule. | [optional] value must be a 64 bit integer
**destination_ip_id** | decimal.Decimal, int,  | decimal.Decimal,  | Destination IP for IP Firewall Rule. | [optional] value must be a 64 bit integer
**logging_type** | [**XiqLoggingType**](XiqLoggingType.md) | [**XiqLoggingType**](XiqLoggingType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

