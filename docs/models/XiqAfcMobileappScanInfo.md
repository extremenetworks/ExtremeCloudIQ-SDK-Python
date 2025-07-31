# extremecloudiq.model.xiq_afc_mobileapp_scan_info.XiqAfcMobileappScanInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ownerId | [optional] value must be a 64 bit integer
**[bssid_list](#bssid_list)** | list, tuple,  | tuple,  | Base radio BSSIDs reported by the mobile application scan | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# bssid_list

Base radio BSSIDs reported by the mobile application scan

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Base radio BSSIDs reported by the mobile application scan | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Base radio BSSIDs reported by the mobile application scan | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

