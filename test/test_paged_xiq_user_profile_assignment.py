# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_user_profile_assignment import PagedXiqUserProfileAssignment  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqUserProfileAssignment(unittest.TestCase):
    """PagedXiqUserProfileAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqUserProfileAssignment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_user_profile_assignment.PagedXiqUserProfileAssignment()  # noqa: E501
        if include_optional :
            return PagedXiqUserProfileAssignment(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_user_profile_assignment.XiqUserProfileAssignment(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        name = '0', 
                        description = '0', 
                        authorisation_policy = '0', 
                        folder_ids = [
                            56
                            ], 
                        assignment_radius_attribute = extremecloudiq.models.xiq_user_profile_assignment_radius_attribute.XiqUserProfileAssignmentRadiusAttribute(
                            attribute_type = 'TUNNEL', 
                            attribute_values = '0', ), 
                        user_group = [
                            extremecloudiq.models.xiq_user_group.XiqUserGroup(
                                id = 56, 
                                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                org_id = 56, 
                                name = '0', 
                                description = '0', 
                                predefined = True, 
                                password_db_location = 'CLOUD', 
                                password_type = 'PPSK', 
                                pcg_use_only = True, 
                                pcg_type = 'AP_BASED', 
                                ppsk_use_only = True, 
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
                                    sms_template_id = 56, ), 
                                user_count = 56, 
                                ssids = [
                                    '0'
                                    ], )
                            ], 
                        mac_object_profiles = [
                            extremecloudiq.models.xiq_mac_object.XiqMacObject(
                                id = 56, 
                                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                org_id = 56, 
                                name = '0', 
                                description = '0', 
                                predefined = True, 
                                value = '0', 
                                mac_type = 'MAC_OUI', 
                                defender_defined = True, 
                                mac_address_end = '0', )
                            ], 
                        os_object_dhcp = [
                            extremecloudiq.models.xiq_os_object.XiqOsObject(
                                id = 56, 
                                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '0', )
                            ], 
                        os_object_https = [
                            extremecloudiq.models.xiq_os_object.XiqOsObject(
                                id = 56, 
                                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '0', )
                            ], 
                        schedules = [
                            extremecloudiq.models.xiq_schedule.XiqSchedule(
                                description = '0', 
                                schedule_type = 'ONE_TIME', 
                                start_date = '0', 
                                end_date = '0', 
                                start_time = '0', 
                                end_time = '0', 
                                recurrence_type = 'EVERYDAY', 
                                weekday_from = 'MONDAY', 
                                weekday_to = 'MONDAY', 
                                start_time2 = '0', 
                                end_time2 = '0', )
                            ], )
                    ]
            )
        else :
            return PagedXiqUserProfileAssignment(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqUserProfileAssignment(self):
        """Test PagedXiqUserProfileAssignment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
