# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .channel_target import ChannelTarget
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChannelTargetDbSystem(ChannelTarget):
    """
    Core properties of a DB System Channel target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChannelTargetDbSystem object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.ChannelTargetDbSystem.target_type` attribute
        of this class is ``DBSYSTEM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this ChannelTargetDbSystem.
            Allowed values for this property are: "DBSYSTEM"
        :type target_type: str

        :param db_system_id:
            The value to assign to the db_system_id property of this ChannelTargetDbSystem.
        :type db_system_id: str

        :param channel_name:
            The value to assign to the channel_name property of this ChannelTargetDbSystem.
        :type channel_name: str

        :param applier_username:
            The value to assign to the applier_username property of this ChannelTargetDbSystem.
        :type applier_username: str

        :param filters:
            The value to assign to the filters property of this ChannelTargetDbSystem.
        :type filters: list[oci.mysql.models.ChannelFilter]

        """
        self.swagger_types = {
            'target_type': 'str',
            'db_system_id': 'str',
            'channel_name': 'str',
            'applier_username': 'str',
            'filters': 'list[ChannelFilter]'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'db_system_id': 'dbSystemId',
            'channel_name': 'channelName',
            'applier_username': 'applierUsername',
            'filters': 'filters'
        }

        self._target_type = None
        self._db_system_id = None
        self._channel_name = None
        self._applier_username = None
        self._filters = None
        self._target_type = 'DBSYSTEM'

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this ChannelTargetDbSystem.
        The OCID of the source DB System.


        :return: The db_system_id of this ChannelTargetDbSystem.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this ChannelTargetDbSystem.
        The OCID of the source DB System.


        :param db_system_id: The db_system_id of this ChannelTargetDbSystem.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def channel_name(self):
        """
        **[Required]** Gets the channel_name of this ChannelTargetDbSystem.
        The case-insensitive name that identifies the replication channel. Channel names
        must follow the rules defined for `MySQL identifiers`__.
        The names of non-Deleted Channels must be unique for each DB System.

        __ https://dev.mysql.com/doc/refman/8.0/en/identifiers.html


        :return: The channel_name of this ChannelTargetDbSystem.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """
        Sets the channel_name of this ChannelTargetDbSystem.
        The case-insensitive name that identifies the replication channel. Channel names
        must follow the rules defined for `MySQL identifiers`__.
        The names of non-Deleted Channels must be unique for each DB System.

        __ https://dev.mysql.com/doc/refman/8.0/en/identifiers.html


        :param channel_name: The channel_name of this ChannelTargetDbSystem.
        :type: str
        """
        self._channel_name = channel_name

    @property
    def applier_username(self):
        """
        **[Required]** Gets the applier_username of this ChannelTargetDbSystem.
        The username for the replication applier of the target MySQL DB System.


        :return: The applier_username of this ChannelTargetDbSystem.
        :rtype: str
        """
        return self._applier_username

    @applier_username.setter
    def applier_username(self, applier_username):
        """
        Sets the applier_username of this ChannelTargetDbSystem.
        The username for the replication applier of the target MySQL DB System.


        :param applier_username: The applier_username of this ChannelTargetDbSystem.
        :type: str
        """
        self._applier_username = applier_username

    @property
    def filters(self):
        """
        Gets the filters of this ChannelTargetDbSystem.
        Replication filter rules to be applied at the DB System Channel target.


        :return: The filters of this ChannelTargetDbSystem.
        :rtype: list[oci.mysql.models.ChannelFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this ChannelTargetDbSystem.
        Replication filter rules to be applied at the DB System Channel target.


        :param filters: The filters of this ChannelTargetDbSystem.
        :type: list[oci.mysql.models.ChannelFilter]
        """
        self._filters = filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
