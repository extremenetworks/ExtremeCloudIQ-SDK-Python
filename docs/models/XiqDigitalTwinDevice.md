# extremecloudiq.model.xiq_digital_twin_device.XiqDigitalTwinDevice

The Digital Twin device to onboard.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Digital Twin device to onboard. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**os_version** | str,  | str,  | The Digital Twin device OS version. | 
**model** | [**XiqDigitalTwinModel**](XiqDigitalTwinModel.md) | [**XiqDigitalTwinModel**](XiqDigitalTwinModel.md) |  | 
**make** | [**XiqDigitalTwinMake**](XiqDigitalTwinMake.md) | [**XiqDigitalTwinMake**](XiqDigitalTwinMake.md) |  | 
**os_type** | str,  | str,  | The Digital Twin device OS type. | [optional] 
**[vim_modules](#vim_modules)** | list, tuple,  | tuple,  | The Digital Twin VIM modules. | [optional] 
**[feat_licenses](#feat_licenses)** | list, tuple,  | tuple,  | The Digital Twin feature licenses. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vim_modules

The Digital Twin VIM modules.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Digital Twin VIM modules. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDigitalTwinVimModule**](XiqDigitalTwinVimModule.md) | [**XiqDigitalTwinVimModule**](XiqDigitalTwinVimModule.md) | [**XiqDigitalTwinVimModule**](XiqDigitalTwinVimModule.md) |  | 

# feat_licenses

The Digital Twin feature licenses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Digital Twin feature licenses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDigitalTwinFeatLicense**](XiqDigitalTwinFeatLicense.md) | [**XiqDigitalTwinFeatLicense**](XiqDigitalTwinFeatLicense.md) | [**XiqDigitalTwinFeatLicense**](XiqDigitalTwinFeatLicense.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

