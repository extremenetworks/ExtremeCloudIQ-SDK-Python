# extremecloudiq.model.xiq_deployment_policy.XiqDeploymentPolicy

Push configuration and upgrade firmware policy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Push configuration and upgrade firmware policy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_complete_configuration_update** | bool,  | BoolClass,  | true if update complete configuration, otherwise update delta configuration. Note: ExtremeCloud IQ will neither upgrade device firmware nor reboot device for a delta configuration push. That means that the other parameters for firmware upgrade and activation are not required when this is false. | [optional] 
**firmware_upgrade_policy** | [**XiqFirmwareUpgradePolicy**](XiqFirmwareUpgradePolicy.md) | [**XiqFirmwareUpgradePolicy**](XiqFirmwareUpgradePolicy.md) |  | [optional] 
**[firmware_upgrade_versions](#firmware_upgrade_versions)** | list, tuple,  | tuple,  |  | [optional] 
**firmware_activate_option** | [**XiqFirmwareActivateOption**](XiqFirmwareActivateOption.md) | [**XiqFirmwareActivateOption**](XiqFirmwareActivateOption.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firmware_upgrade_versions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqFirmwareUpgradeVersion**](XiqFirmwareUpgradeVersion.md) | [**XiqFirmwareUpgradeVersion**](XiqFirmwareUpgradeVersion.md) | [**XiqFirmwareUpgradeVersion**](XiqFirmwareUpgradeVersion.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

