# XiqPostExpirationAction

The type of action to take after the account expiration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_credentials_renewal** | **bool** | The renew user credentials option or null for other option. | [optional] 
**enable_delete_immediately** | **bool** | The immediate delete option or null to schedule the delete. | [optional] 
**delete_after_value** | **int** | The after expiration scheduled time to delete or null to not delete.. | [optional] 
**delete_after_unit** | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


