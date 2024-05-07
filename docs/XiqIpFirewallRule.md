# XiqIpFirewallRule

IP Firewall Rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**action** | [**XiqIpFirewallAction**](XiqIpFirewallAction.md) |  | [optional] 
**network_service** | [**XiqNetworkService**](XiqNetworkService.md) |  | [optional] 
**application_service** | [**XiqApplicationService**](XiqApplicationService.md) |  | [optional] 
**source_ip** | [**XiqL3AddressProfile**](XiqL3AddressProfile.md) |  | [optional] 
**destination_ip** | [**XiqL3AddressProfile**](XiqL3AddressProfile.md) |  | [optional] 
**logging_type** | [**XiqLoggingType**](XiqLoggingType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


