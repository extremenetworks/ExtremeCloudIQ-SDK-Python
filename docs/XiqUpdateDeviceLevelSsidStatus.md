# XiqUpdateDeviceLevelSsidStatus

The request for disable/enable device level ssid.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssid_ids** | **list[int]** | The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered. | 
**if_names** | [**list[XiqWirelessIfName]**](XiqWirelessIfName.md) | The one or multiple ssid on wifi interfaces (example:wifi0 or wifi1) to be disabled/enabled, cannot be empty or no SSID will be disabled or enabled. | 
**enabled** | **bool** | To disable or enable the given device level SSIDs on the wifi interfaces. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


