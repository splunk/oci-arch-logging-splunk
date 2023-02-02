# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionSummary(object):
    """
    Database Connection Summary.
    """

    #: A constant which can be used with the database_type property of a ConnectionSummary.
    #: This constant has a value of "MANUAL"
    DATABASE_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the database_type property of a ConnectionSummary.
    #: This constant has a value of "AUTONOMOUS"
    DATABASE_TYPE_AUTONOMOUS = "AUTONOMOUS"

    #: A constant which can be used with the database_type property of a ConnectionSummary.
    #: This constant has a value of "USER_MANAGED_OCI"
    DATABASE_TYPE_USER_MANAGED_OCI = "USER_MANAGED_OCI"

    #: A constant which can be used with the manual_database_sub_type property of a ConnectionSummary.
    #: This constant has a value of "ORACLE"
    MANUAL_DATABASE_SUB_TYPE_ORACLE = "ORACLE"

    #: A constant which can be used with the manual_database_sub_type property of a ConnectionSummary.
    #: This constant has a value of "RDS_ORACLE"
    MANUAL_DATABASE_SUB_TYPE_RDS_ORACLE = "RDS_ORACLE"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ConnectionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ConnectionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ConnectionSummary.
        :type compartment_id: str

        :param database_type:
            The value to assign to the database_type property of this ConnectionSummary.
            Allowed values for this property are: "MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param manual_database_sub_type:
            The value to assign to the manual_database_sub_type property of this ConnectionSummary.
            Allowed values for this property are: "ORACLE", "RDS_ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type manual_database_sub_type: str

        :param is_dedicated:
            The value to assign to the is_dedicated property of this ConnectionSummary.
        :type is_dedicated: bool

        :param display_name:
            The value to assign to the display_name property of this ConnectionSummary.
        :type display_name: str

        :param database_id:
            The value to assign to the database_id property of this ConnectionSummary.
        :type database_id: str

        :param time_created:
            The value to assign to the time_created property of this ConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ConnectionSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConnectionSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ConnectionSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'database_type': 'str',
            'manual_database_sub_type': 'str',
            'is_dedicated': 'bool',
            'display_name': 'str',
            'database_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'database_type': 'databaseType',
            'manual_database_sub_type': 'manualDatabaseSubType',
            'is_dedicated': 'isDedicated',
            'display_name': 'displayName',
            'database_id': 'databaseId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._database_type = None
        self._manual_database_sub_type = None
        self._is_dedicated = None
        self._display_name = None
        self._database_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ConnectionSummary.
        The OCID of the resource


        :return: The id of this ConnectionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionSummary.
        The OCID of the resource


        :param id: The id of this ConnectionSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ConnectionSummary.
        OCID of the compartment


        :return: The compartment_id of this ConnectionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ConnectionSummary.
        OCID of the compartment


        :param compartment_id: The compartment_id of this ConnectionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this ConnectionSummary.
        Database connection type.

        Allowed values for this property are: "MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ConnectionSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ConnectionSummary.
        Database connection type.


        :param database_type: The database_type of this ConnectionSummary.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTONOMOUS", "USER_MANAGED_OCI"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def manual_database_sub_type(self):
        """
        Gets the manual_database_sub_type of this ConnectionSummary.
        Database manual connection subtype. This value can only be specified for manual connections.

        Allowed values for this property are: "ORACLE", "RDS_ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The manual_database_sub_type of this ConnectionSummary.
        :rtype: str
        """
        return self._manual_database_sub_type

    @manual_database_sub_type.setter
    def manual_database_sub_type(self, manual_database_sub_type):
        """
        Sets the manual_database_sub_type of this ConnectionSummary.
        Database manual connection subtype. This value can only be specified for manual connections.


        :param manual_database_sub_type: The manual_database_sub_type of this ConnectionSummary.
        :type: str
        """
        allowed_values = ["ORACLE", "RDS_ORACLE"]
        if not value_allowed_none_or_none_sentinel(manual_database_sub_type, allowed_values):
            manual_database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._manual_database_sub_type = manual_database_sub_type

    @property
    def is_dedicated(self):
        """
        Gets the is_dedicated of this ConnectionSummary.
        True if the Autonomous Connection is dedicated. Not provided for Non-Autonomous Connections.


        :return: The is_dedicated of this ConnectionSummary.
        :rtype: bool
        """
        return self._is_dedicated

    @is_dedicated.setter
    def is_dedicated(self, is_dedicated):
        """
        Sets the is_dedicated of this ConnectionSummary.
        True if the Autonomous Connection is dedicated. Not provided for Non-Autonomous Connections.


        :param is_dedicated: The is_dedicated of this ConnectionSummary.
        :type: bool
        """
        self._is_dedicated = is_dedicated

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ConnectionSummary.
        Database Connection display name identifier.


        :return: The display_name of this ConnectionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConnectionSummary.
        Database Connection display name identifier.


        :param display_name: The display_name of this ConnectionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def database_id(self):
        """
        Gets the database_id of this ConnectionSummary.
        The OCID of the cloud database.


        :return: The database_id of this ConnectionSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this ConnectionSummary.
        The OCID of the cloud database.


        :param database_id: The database_id of this ConnectionSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConnectionSummary.
        The time the Connection resource was created. An RFC3339 formatted datetime string.


        :return: The time_created of this ConnectionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConnectionSummary.
        The time the Connection resource was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this ConnectionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ConnectionSummary.
        The time of the last Connection resource details update. An RFC3339 formatted datetime string.


        :return: The time_updated of this ConnectionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ConnectionSummary.
        The time of the last Connection resource details update. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this ConnectionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConnectionSummary.
        The current state of the Connection resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConnectionSummary.
        The current state of the Connection resource.


        :param lifecycle_state: The lifecycle_state of this ConnectionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ConnectionSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information
        for a resource in Failed state.


        :return: The lifecycle_details of this ConnectionSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ConnectionSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information
        for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ConnectionSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ConnectionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ConnectionSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ConnectionSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ConnectionSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ConnectionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ConnectionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ConnectionSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ConnectionSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ConnectionSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ConnectionSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ConnectionSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ConnectionSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other