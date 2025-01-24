# extremecloudiq.model.xiq_ekahau_import_issues.XiqEkahauImportIssues

Any issues related to the import of this floor, eg: why it failed, why an AP was discarded, etc.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Any issues related to the import of this floor, eg: why it failed, why an AP was discarded, etc. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**floor** | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) |  | [optional] 
**background** | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) |  | [optional] 
**[custom_ap_configurations](#custom_ap_configurations)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | If the floor was imported but issues occurred while importing custom AP configurations they will be listed here. | [optional] 
**[discarded_aps](#discarded_aps)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | If the floor was imported but some of the APs were discarded they will be listed here. | [optional] 
**[discarded_walls](#discarded_walls)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | If the floor was imported but some of the walls were discarded they will be listed here. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_ap_configurations

If the floor was imported but issues occurred while importing custom AP configurations they will be listed here.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If the floor was imported but issues occurred while importing custom AP configurations they will be listed here. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type If the floor was imported but issues occurred while importing custom AP configurations they will be listed here. | [optional] 

# any_string_name

If the floor was imported but issues occurred while importing custom AP configurations they will be listed here.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | If the floor was imported but issues occurred while importing custom AP configurations they will be listed here. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) |  | 

# discarded_aps

If the floor was imported but some of the APs were discarded they will be listed here.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If the floor was imported but some of the APs were discarded they will be listed here. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | any string name can be used but the value must be the correct type | [optional] 

# discarded_walls

If the floor was imported but some of the walls were discarded they will be listed here.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If the floor was imported but some of the walls were discarded they will be listed here. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | [**XiqEkahauImportIssue**](XiqEkahauImportIssue.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

