# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_create_user_group_request import XiqCreateUserGroupRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateUserGroupRequest(unittest.TestCase):
    """XiqCreateUserGroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateUserGroupRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_user_group_request.XiqCreateUserGroupRequest()  # noqa: E501
        if include_optional :
            return XiqCreateUserGroupRequest(
                name = '0', 
                description = '0', 
                password_db_location = 'CLOUD', 
                ppsk_use_only = True, 
                password_type = 'PPSK', 
                enable_max_clients_per_ppsk = True, 
                max_clients_per_ppsk = 56, 
                pcg_use_only = True, 
                pcg_type = 'AP_BASED', 
                enable_cwp_reg = True, 
                password_settings = extremecloudiq.models.xiq_password_settings.XiqPasswordSettings(
                    enable_letters = True, 
                    enable_numbers = True, 
                    enable_special_characters = True, 
                    password_concat_string = '0', 
                    psk_generation_method = 'PASSWORD_ONLY', 
                    password_character_types = 'INCLUDE_ALL_CHARACTER_TYPE_ENABLED', 
                    password_length = 56, ), 
                expiration_settings = extremecloudiq.models.xiq_expiration_settings.XiqExpirationSettings(
                    expiration_type = 'NEVER_EXPIRE', 
                    valid_during_dates = extremecloudiq.models.xiq_valid_during_date_settings.XiqValidDuringDateSettings(
                        start_date_time = extremecloudiq.models.xiq_date_time_type.XiqDateTimeType(
                            day_of_month = 56, 
                            month = 56, 
                            year = 56, 
                            hour_of_day = 56, 
                            minute_of_hour = 56, ), 
                        end_date_time = extremecloudiq.models.xiq_date_time_type.XiqDateTimeType(
                            day_of_month = 56, 
                            month = 56, 
                            year = 56, 
                            hour_of_day = 56, 
                            minute_of_hour = 56, ), 
                        time_zone = '0', ), 
                    valid_for_time_period = extremecloudiq.models.xiq_valid_for_time_period_settings.XiqValidForTimePeriodSettings(
                        valid_time_period_after = 'ID_CREATION', 
                        after_id_creation_settings = extremecloudiq.models.xiq_valid_time_period_after_id_creation.XiqValidTimePeriodAfterIdCreation(
                            valid_time_period = 56, 
                            valid_time_period_unit = 'MINUTE', ), 
                        after_first_login_settings = extremecloudiq.models.xiq_valid_time_period_after_first_login.XiqValidTimePeriodAfterFirstLogin(
                            valid_time_period = 56, 
                            valid_time_period_unit = 'MINUTE', 
                            first_login_within = 56, 
                            first_login_within_unit = 'MINUTE', ), ), 
                    valid_daily = extremecloudiq.models.xiq_valid_daily_settings.XiqValidDailySettings(
                        daily_start_hour = 56, 
                        daily_start_minute = 56, 
                        daily_end_hour = 56, 
                        daily_end_minute = 56, ), 
                    expiration_action = 'SHOW_MESSAGE', 
                    post_expiration_action = extremecloudiq.models.xiq_post_expiration_action.XiqPostExpirationAction(
                        enable_credentials_renewal = True, 
                        enable_delete_immediately = True, 
                        delete_after_value = 56, 
                        delete_after_unit = 'MINUTE', ), ), 
                delivery_settings = extremecloudiq.models.xiq_delivery_settings.XiqDeliverySettings(
                    email_template_id = 56, 
                    sms_template_id = 56, )
            )
        else :
            return XiqCreateUserGroupRequest(
                name = '0',
                password_db_location = 'CLOUD',
                password_type = 'PPSK',
                password_settings = extremecloudiq.models.xiq_password_settings.XiqPasswordSettings(
                    enable_letters = True, 
                    enable_numbers = True, 
                    enable_special_characters = True, 
                    password_concat_string = '0', 
                    psk_generation_method = 'PASSWORD_ONLY', 
                    password_character_types = 'INCLUDE_ALL_CHARACTER_TYPE_ENABLED', 
                    password_length = 56, ),
                expiration_settings = extremecloudiq.models.xiq_expiration_settings.XiqExpirationSettings(
                    expiration_type = 'NEVER_EXPIRE', 
                    valid_during_dates = extremecloudiq.models.xiq_valid_during_date_settings.XiqValidDuringDateSettings(
                        start_date_time = extremecloudiq.models.xiq_date_time_type.XiqDateTimeType(
                            day_of_month = 56, 
                            month = 56, 
                            year = 56, 
                            hour_of_day = 56, 
                            minute_of_hour = 56, ), 
                        end_date_time = extremecloudiq.models.xiq_date_time_type.XiqDateTimeType(
                            day_of_month = 56, 
                            month = 56, 
                            year = 56, 
                            hour_of_day = 56, 
                            minute_of_hour = 56, ), 
                        time_zone = '0', ), 
                    valid_for_time_period = extremecloudiq.models.xiq_valid_for_time_period_settings.XiqValidForTimePeriodSettings(
                        valid_time_period_after = 'ID_CREATION', 
                        after_id_creation_settings = extremecloudiq.models.xiq_valid_time_period_after_id_creation.XiqValidTimePeriodAfterIdCreation(
                            valid_time_period = 56, 
                            valid_time_period_unit = 'MINUTE', ), 
                        after_first_login_settings = extremecloudiq.models.xiq_valid_time_period_after_first_login.XiqValidTimePeriodAfterFirstLogin(
                            valid_time_period = 56, 
                            valid_time_period_unit = 'MINUTE', 
                            first_login_within = 56, 
                            first_login_within_unit = 'MINUTE', ), ), 
                    valid_daily = extremecloudiq.models.xiq_valid_daily_settings.XiqValidDailySettings(
                        daily_start_hour = 56, 
                        daily_start_minute = 56, 
                        daily_end_hour = 56, 
                        daily_end_minute = 56, ), 
                    expiration_action = 'SHOW_MESSAGE', 
                    post_expiration_action = extremecloudiq.models.xiq_post_expiration_action.XiqPostExpirationAction(
                        enable_credentials_renewal = True, 
                        enable_delete_immediately = True, 
                        delete_after_value = 56, 
                        delete_after_unit = 'MINUTE', ), ),
                delivery_settings = extremecloudiq.models.xiq_delivery_settings.XiqDeliverySettings(
                    email_template_id = 56, 
                    sms_template_id = 56, ),
        )

    def testXiqCreateUserGroupRequest(self):
        """Test XiqCreateUserGroupRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
