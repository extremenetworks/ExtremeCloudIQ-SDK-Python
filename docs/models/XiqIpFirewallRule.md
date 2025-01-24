# extremecloudiq.model.xiq_ip_firewall_rule.XiqIpFirewallRule

IP Firewall Rule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | IP Firewall Rule | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**action** | [**XiqIpFirewallAction**](XiqIpFirewallAction.md) | [**XiqIpFirewallAction**](XiqIpFirewallAction.md) |  | [optional] 
**network_service** | [**XiqNetworkService**](XiqNetworkService.md) | [**XiqNetworkService**](XiqNetworkService.md) |  | [optional] 
**application_service** | [**XiqApplicationService**](XiqApplicationService.md) | [**XiqApplicationService**](XiqApplicationService.md) |  | [optional] 
**source_ip** | [**XiqL3AddressProfile**](XiqL3AddressProfile.md) | [**XiqL3AddressProfile**](XiqL3AddressProfile.md) |  | [optional] 
**destination_ip** | [**XiqL3AddressProfile**](XiqL3AddressProfile.md) | [**XiqL3AddressProfile**](XiqL3AddressProfile.md) |  | [optional] 
**logging_type** | [**XiqLoggingType**](XiqLoggingType.md) | [**XiqLoggingType**](XiqLoggingType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

