# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyticsClusterNode(object):
    """
    DEPRECATED -- please use HeatWave API instead.
    An Analytics Cluster Node is a compute host that is part of an Analytics Cluster.
    """

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AnalyticsClusterNode.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyticsClusterNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param node_id:
            The value to assign to the node_id property of this AnalyticsClusterNode.
        :type node_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AnalyticsClusterNode.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this AnalyticsClusterNode.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AnalyticsClusterNode.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'node_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'node_id': 'nodeId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._node_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def node_id(self):
        """
        **[Required]** Gets the node_id of this AnalyticsClusterNode.
        The ID of the node within MySQL Analytics Cluster.


        :return: The node_id of this AnalyticsClusterNode.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this AnalyticsClusterNode.
        The ID of the node within MySQL Analytics Cluster.


        :param node_id: The node_id of this AnalyticsClusterNode.
        :type: str
        """
        self._node_id = node_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AnalyticsClusterNode.
        The current state of the MySQL Analytics Cluster node.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AnalyticsClusterNode.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AnalyticsClusterNode.
        The current state of the MySQL Analytics Cluster node.


        :param lifecycle_state: The lifecycle_state of this AnalyticsClusterNode.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this AnalyticsClusterNode.
        The date and time the MySQL Analytics Cluster node was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this AnalyticsClusterNode.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AnalyticsClusterNode.
        The date and time the MySQL Analytics Cluster node was created, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this AnalyticsClusterNode.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this AnalyticsClusterNode.
        The date and time the MySQL Analytics Cluster node was updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this AnalyticsClusterNode.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AnalyticsClusterNode.
        The date and time the MySQL Analytics Cluster node was updated, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this AnalyticsClusterNode.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other