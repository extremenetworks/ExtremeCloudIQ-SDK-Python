# XiqDeploymentPolicy

Push configuration and upgrade firmware policy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_complete_configuration_update** | **bool** | true if update complete configuration, otherwise update delta configuration. Note: ExtremeCloud IQ will neither upgrade device firmware nor reboot device for a delta configuration push. That means that the other parameters for firmware upgrade and activation are not required when this is false. | [optional] 
**firmware_upgrade_policy** | [**XiqFirmwareUpgradePolicy**](XiqFirmwareUpgradePolicy.md) |  | [optional] 
**firmware_upgrade_versions** | [**list[XiqFirmwareUpgradeVersion]**](XiqFirmwareUpgradeVersion.md) |  | [optional] 
**firmware_activate_option** | [**XiqFirmwareActivateOption**](XiqFirmwareActivateOption.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


