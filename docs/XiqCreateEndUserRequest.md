# XiqCreateEndUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_id** | **int** | The user group ID | 
**name** | **str** | The user common name | [optional] 
**user_name** | **str** | The designated username, must match either the user&#39;s name, emailAddress, or phoneNumber | 
**organization** | **str** | The organization name | [optional] 
**visit_purpose** | **str** | The purpose of visit | [optional] 
**description** | **str** | The user description | [optional] 
**email_address** | **str** | The user email | [optional] 
**phone_number** | **str** | The user phone number | [optional] 
**password** | **str** | The user password, if null a random password will be generated base on the user group rule | [optional] 
**email_password_delivery** | **str** | The password delivery Email | [optional] 
**sms_password_delivery** | **str** | The password delivery SMS | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


