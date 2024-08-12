# XiqChangeDevicesIbeaconRequest

The request to update the existing device level iBeacon setting or create the new device level iBeacon settings if the devices' Network Policy iBeacon service has been enabled.The update will be effective on all devices or none if one of the devices has Network Policy iBeacon service not enabled.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_ids** | **list[int]** | The list of device IDs.  Consult ExtremeNetworks documentation for the complete list of devices that support the beacon transmitter.  The following are some of the AP devices with the embedded beacon: AP122, AP122X, AP150W, AP245X, AP250, and AP550. | 
**enabled** | **bool** | Whether to enable the device beacon.  Default to true for newly enabled device. | [optional] 
**major** | **int** | Identification of a subset of beacons in a geographical venue. Default to 1 for newly enabled device. | [optional] 
**minor** | **int** | Identification of a beacon in a specific location. Default to 1 for newly enabled device. | [optional] 
**power** | **int** | The transmission power in dBm. Default to -59 for newly enabled device. | [optional] 
**enable_monitoring** | **bool** | Whether to enable iBeacon monitoring. Default to true for newly enabled device. | [optional] 
**enable_cloud_reporting** | **bool** | Whether the device iBeacon Cloud Reporting is enabled. Default to true for newly enabled device. | [optional] 
**enable_batch_reporting** | **bool** | Whether the device iBeacon Batch Reporting is enabled. Default to false for newly enabled device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


