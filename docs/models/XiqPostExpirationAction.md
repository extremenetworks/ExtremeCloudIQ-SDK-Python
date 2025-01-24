# extremecloudiq.model.xiq_post_expiration_action.XiqPostExpirationAction

The type of action to take after the account expiration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The type of action to take after the account expiration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_credentials_renewal** | bool,  | BoolClass,  | The renew user credentials option or null for other option. | [optional] 
**enable_delete_immediately** | bool,  | BoolClass,  | The immediate delete option or null to schedule the delete. | [optional] 
**delete_after_value** | decimal.Decimal, int,  | decimal.Decimal,  | The after expiration scheduled time to delete or null to not delete.. | [optional] value must be a 32 bit integer
**delete_after_unit** | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

