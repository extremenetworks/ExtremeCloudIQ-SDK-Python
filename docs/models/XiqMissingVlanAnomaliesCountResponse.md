# extremecloudiq.model.xiq_missing_vlan_anomalies_count_response.XiqMissingVlanAnomaliesCountResponse

Copilot Missing vlan anomalies count details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Missing vlan anomalies count details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_anomalies_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[anomalies_count_by_site](#anomalies_count_by_site)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# anomalies_count_by_site

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqMissingVlanSiteAnomalyCountDetails**](XiqMissingVlanSiteAnomalyCountDetails.md) | [**XiqMissingVlanSiteAnomalyCountDetails**](XiqMissingVlanSiteAnomalyCountDetails.md) | [**XiqMissingVlanSiteAnomalyCountDetails**](XiqMissingVlanSiteAnomalyCountDetails.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

