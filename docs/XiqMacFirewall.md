# XiqMacFirewall

MAC Firewall policy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The MAC Firewall policy name | [optional] 
**description** | **str** | The MAC Firewall policy description. | [optional] 
**rules** | [**list[XiqMacFirewallRule]**](XiqMacFirewallRule.md) | List of MAC Firewall Rules. | [optional] 
**predefined** | **bool** | Flag to describe whether the application is predefined or customized. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


