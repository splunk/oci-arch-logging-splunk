# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMonitoredResourceDetails(object):
    """
    The information about updating a monitored resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMonitoredResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMonitoredResourceDetails.
        :type display_name: str

        :param host_name:
            The value to assign to the host_name property of this UpdateMonitoredResourceDetails.
        :type host_name: str

        :param resource_time_zone:
            The value to assign to the resource_time_zone property of this UpdateMonitoredResourceDetails.
        :type resource_time_zone: str

        :param properties:
            The value to assign to the properties property of this UpdateMonitoredResourceDetails.
        :type properties: list[oci.stack_monitoring.models.MonitoredResourceProperty]

        :param database_connection_details:
            The value to assign to the database_connection_details property of this UpdateMonitoredResourceDetails.
        :type database_connection_details: oci.stack_monitoring.models.ConnectionDetails

        :param credentials:
            The value to assign to the credentials property of this UpdateMonitoredResourceDetails.
        :type credentials: oci.stack_monitoring.models.MonitoredResourceCredential

        :param aliases:
            The value to assign to the aliases property of this UpdateMonitoredResourceDetails.
        :type aliases: oci.stack_monitoring.models.MonitoredResourceAliasCredential

        """
        self.swagger_types = {
            'display_name': 'str',
            'host_name': 'str',
            'resource_time_zone': 'str',
            'properties': 'list[MonitoredResourceProperty]',
            'database_connection_details': 'ConnectionDetails',
            'credentials': 'MonitoredResourceCredential',
            'aliases': 'MonitoredResourceAliasCredential'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'host_name': 'hostName',
            'resource_time_zone': 'resourceTimeZone',
            'properties': 'properties',
            'database_connection_details': 'databaseConnectionDetails',
            'credentials': 'credentials',
            'aliases': 'aliases'
        }

        self._display_name = None
        self._host_name = None
        self._resource_time_zone = None
        self._properties = None
        self._database_connection_details = None
        self._credentials = None
        self._aliases = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMonitoredResourceDetails.
        Monitored resource display name.


        :return: The display_name of this UpdateMonitoredResourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMonitoredResourceDetails.
        Monitored resource display name.


        :param display_name: The display_name of this UpdateMonitoredResourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def host_name(self):
        """
        Gets the host_name of this UpdateMonitoredResourceDetails.
        Host name of the monitored resource


        :return: The host_name of this UpdateMonitoredResourceDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this UpdateMonitoredResourceDetails.
        Host name of the monitored resource


        :param host_name: The host_name of this UpdateMonitoredResourceDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def resource_time_zone(self):
        """
        Gets the resource_time_zone of this UpdateMonitoredResourceDetails.
        Time zone in the form of tz database canonical zone ID.


        :return: The resource_time_zone of this UpdateMonitoredResourceDetails.
        :rtype: str
        """
        return self._resource_time_zone

    @resource_time_zone.setter
    def resource_time_zone(self, resource_time_zone):
        """
        Sets the resource_time_zone of this UpdateMonitoredResourceDetails.
        Time zone in the form of tz database canonical zone ID.


        :param resource_time_zone: The resource_time_zone of this UpdateMonitoredResourceDetails.
        :type: str
        """
        self._resource_time_zone = resource_time_zone

    @property
    def properties(self):
        """
        Gets the properties of this UpdateMonitoredResourceDetails.
        List of monitored resource properties


        :return: The properties of this UpdateMonitoredResourceDetails.
        :rtype: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this UpdateMonitoredResourceDetails.
        List of monitored resource properties


        :param properties: The properties of this UpdateMonitoredResourceDetails.
        :type: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        self._properties = properties

    @property
    def database_connection_details(self):
        """
        Gets the database_connection_details of this UpdateMonitoredResourceDetails.

        :return: The database_connection_details of this UpdateMonitoredResourceDetails.
        :rtype: oci.stack_monitoring.models.ConnectionDetails
        """
        return self._database_connection_details

    @database_connection_details.setter
    def database_connection_details(self, database_connection_details):
        """
        Sets the database_connection_details of this UpdateMonitoredResourceDetails.

        :param database_connection_details: The database_connection_details of this UpdateMonitoredResourceDetails.
        :type: oci.stack_monitoring.models.ConnectionDetails
        """
        self._database_connection_details = database_connection_details

    @property
    def credentials(self):
        """
        Gets the credentials of this UpdateMonitoredResourceDetails.

        :return: The credentials of this UpdateMonitoredResourceDetails.
        :rtype: oci.stack_monitoring.models.MonitoredResourceCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this UpdateMonitoredResourceDetails.

        :param credentials: The credentials of this UpdateMonitoredResourceDetails.
        :type: oci.stack_monitoring.models.MonitoredResourceCredential
        """
        self._credentials = credentials

    @property
    def aliases(self):
        """
        Gets the aliases of this UpdateMonitoredResourceDetails.

        :return: The aliases of this UpdateMonitoredResourceDetails.
        :rtype: oci.stack_monitoring.models.MonitoredResourceAliasCredential
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this UpdateMonitoredResourceDetails.

        :param aliases: The aliases of this UpdateMonitoredResourceDetails.
        :type: oci.stack_monitoring.models.MonitoredResourceAliasCredential
        """
        self._aliases = aliases

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
