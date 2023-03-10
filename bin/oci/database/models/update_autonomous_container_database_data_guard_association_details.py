# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutonomousContainerDatabaseDataGuardAssociationDetails(object):
    """
    The configuration details for updating a Autonomous Container DatabaseData Guard association for a Autonomous Container Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutonomousContainerDatabaseDataGuardAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_automatic_failover_enabled:
            The value to assign to the is_automatic_failover_enabled property of this UpdateAutonomousContainerDatabaseDataGuardAssociationDetails.
        :type is_automatic_failover_enabled: bool

        """
        self.swagger_types = {
            'is_automatic_failover_enabled': 'bool'
        }

        self.attribute_map = {
            'is_automatic_failover_enabled': 'isAutomaticFailoverEnabled'
        }

        self._is_automatic_failover_enabled = None

    @property
    def is_automatic_failover_enabled(self):
        """
        Gets the is_automatic_failover_enabled of this UpdateAutonomousContainerDatabaseDataGuardAssociationDetails.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :return: The is_automatic_failover_enabled of this UpdateAutonomousContainerDatabaseDataGuardAssociationDetails.
        :rtype: bool
        """
        return self._is_automatic_failover_enabled

    @is_automatic_failover_enabled.setter
    def is_automatic_failover_enabled(self, is_automatic_failover_enabled):
        """
        Sets the is_automatic_failover_enabled of this UpdateAutonomousContainerDatabaseDataGuardAssociationDetails.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :param is_automatic_failover_enabled: The is_automatic_failover_enabled of this UpdateAutonomousContainerDatabaseDataGuardAssociationDetails.
        :type: bool
        """
        self._is_automatic_failover_enabled = is_automatic_failover_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
