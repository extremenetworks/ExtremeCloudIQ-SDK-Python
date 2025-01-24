# extremecloudiq.model.xiq_viq_license.XiqViqLicense

The license list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The license list | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**status** | [**XiqLicenseStatus**](XiqLicenseStatus.md) | [**XiqLicenseStatus**](XiqLicenseStatus.md) |  | [optional] 
**active_date** | str, datetime,  | str,  | The active date | [optional] value must conform to RFC-3339 date-time
**expire_date** | str, datetime,  | str,  | The expire date | [optional] value must conform to RFC-3339 date-time
**entitlement_key** | str,  | str,  | The entitlement key | [optional] 
**entitlement_type** | [**XiqEntitlementType**](XiqEntitlementType.md) | [**XiqEntitlementType**](XiqEntitlementType.md) |  | [optional] 
**mode** | [**XiqLicenseMode**](XiqLicenseMode.md) | [**XiqLicenseMode**](XiqLicenseMode.md) |  | [optional] 
**devices** | decimal.Decimal, int,  | decimal.Decimal,  | The device number | [optional] value must be a 32 bit integer
**activated** | decimal.Decimal, int,  | decimal.Decimal,  | The activated device number | [optional] value must be a 32 bit integer
**available** | decimal.Decimal, int,  | decimal.Decimal,  | The available device number | [optional] value must be a 32 bit integer
**license_type** | str,  | str,  | The Gemalto license type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

