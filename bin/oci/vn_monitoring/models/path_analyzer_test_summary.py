# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PathAnalyzerTestSummary(object):
    """
    Defines the summary of a `PathAnalyzerTest` resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PathAnalyzerTestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PathAnalyzerTestSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this PathAnalyzerTestSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PathAnalyzerTestSummary.
        :type compartment_id: str

        :param protocol:
            The value to assign to the protocol property of this PathAnalyzerTestSummary.
        :type protocol: int

        :param source_endpoint:
            The value to assign to the source_endpoint property of this PathAnalyzerTestSummary.
        :type source_endpoint: oci.vn_monitoring.models.Endpoint

        :param destination_endpoint:
            The value to assign to the destination_endpoint property of this PathAnalyzerTestSummary.
        :type destination_endpoint: oci.vn_monitoring.models.Endpoint

        :param protocol_parameters:
            The value to assign to the protocol_parameters property of this PathAnalyzerTestSummary.
        :type protocol_parameters: oci.vn_monitoring.models.ProtocolParameters

        :param query_options:
            The value to assign to the query_options property of this PathAnalyzerTestSummary.
        :type query_options: oci.vn_monitoring.models.QueryOptions

        :param time_created:
            The value to assign to the time_created property of this PathAnalyzerTestSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PathAnalyzerTestSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PathAnalyzerTestSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PathAnalyzerTestSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PathAnalyzerTestSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PathAnalyzerTestSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'protocol': 'int',
            'source_endpoint': 'Endpoint',
            'destination_endpoint': 'Endpoint',
            'protocol_parameters': 'ProtocolParameters',
            'query_options': 'QueryOptions',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'protocol': 'protocol',
            'source_endpoint': 'sourceEndpoint',
            'destination_endpoint': 'destinationEndpoint',
            'protocol_parameters': 'protocolParameters',
            'query_options': 'queryOptions',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._protocol = None
        self._source_endpoint = None
        self._destination_endpoint = None
        self._protocol_parameters = None
        self._query_options = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PathAnalyzerTestSummary.
        A unique identifier established when the resource is created. The identifier can't be changed later.


        :return: The id of this PathAnalyzerTestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PathAnalyzerTestSummary.
        A unique identifier established when the resource is created. The identifier can't be changed later.


        :param id: The id of this PathAnalyzerTestSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PathAnalyzerTestSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this PathAnalyzerTestSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PathAnalyzerTestSummary.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this PathAnalyzerTestSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PathAnalyzerTestSummary.
        The `OCID`__ of the `PathAnalyzerTest` resource's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PathAnalyzerTestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PathAnalyzerTestSummary.
        The `OCID`__ of the `PathAnalyzerTest` resource's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PathAnalyzerTestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this PathAnalyzerTestSummary.
        The IP protocol to use for the `PathAnalyzerTest` resource.


        :return: The protocol of this PathAnalyzerTestSummary.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this PathAnalyzerTestSummary.
        The IP protocol to use for the `PathAnalyzerTest` resource.


        :param protocol: The protocol of this PathAnalyzerTestSummary.
        :type: int
        """
        self._protocol = protocol

    @property
    def source_endpoint(self):
        """
        **[Required]** Gets the source_endpoint of this PathAnalyzerTestSummary.

        :return: The source_endpoint of this PathAnalyzerTestSummary.
        :rtype: oci.vn_monitoring.models.Endpoint
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """
        Sets the source_endpoint of this PathAnalyzerTestSummary.

        :param source_endpoint: The source_endpoint of this PathAnalyzerTestSummary.
        :type: oci.vn_monitoring.models.Endpoint
        """
        self._source_endpoint = source_endpoint

    @property
    def destination_endpoint(self):
        """
        **[Required]** Gets the destination_endpoint of this PathAnalyzerTestSummary.

        :return: The destination_endpoint of this PathAnalyzerTestSummary.
        :rtype: oci.vn_monitoring.models.Endpoint
        """
        return self._destination_endpoint

    @destination_endpoint.setter
    def destination_endpoint(self, destination_endpoint):
        """
        Sets the destination_endpoint of this PathAnalyzerTestSummary.

        :param destination_endpoint: The destination_endpoint of this PathAnalyzerTestSummary.
        :type: oci.vn_monitoring.models.Endpoint
        """
        self._destination_endpoint = destination_endpoint

    @property
    def protocol_parameters(self):
        """
        Gets the protocol_parameters of this PathAnalyzerTestSummary.

        :return: The protocol_parameters of this PathAnalyzerTestSummary.
        :rtype: oci.vn_monitoring.models.ProtocolParameters
        """
        return self._protocol_parameters

    @protocol_parameters.setter
    def protocol_parameters(self, protocol_parameters):
        """
        Sets the protocol_parameters of this PathAnalyzerTestSummary.

        :param protocol_parameters: The protocol_parameters of this PathAnalyzerTestSummary.
        :type: oci.vn_monitoring.models.ProtocolParameters
        """
        self._protocol_parameters = protocol_parameters

    @property
    def query_options(self):
        """
        **[Required]** Gets the query_options of this PathAnalyzerTestSummary.

        :return: The query_options of this PathAnalyzerTestSummary.
        :rtype: oci.vn_monitoring.models.QueryOptions
        """
        return self._query_options

    @query_options.setter
    def query_options(self, query_options):
        """
        Sets the query_options of this PathAnalyzerTestSummary.

        :param query_options: The query_options of this PathAnalyzerTestSummary.
        :type: oci.vn_monitoring.models.QueryOptions
        """
        self._query_options = query_options

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PathAnalyzerTestSummary.
        The date and time the `PathAnalyzerTest` resource was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PathAnalyzerTestSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PathAnalyzerTestSummary.
        The date and time the `PathAnalyzerTest` resource was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PathAnalyzerTestSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PathAnalyzerTestSummary.
        The date and time the `PathAnalyzerTest` resource was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this PathAnalyzerTestSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PathAnalyzerTestSummary.
        The date and time the `PathAnalyzerTest` resource was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this PathAnalyzerTestSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PathAnalyzerTestSummary.
        The current state of the `PathAnalyzerTest` resource.


        :return: The lifecycle_state of this PathAnalyzerTestSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PathAnalyzerTestSummary.
        The current state of the `PathAnalyzerTest` resource.


        :param lifecycle_state: The lifecycle_state of this PathAnalyzerTestSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PathAnalyzerTestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PathAnalyzerTestSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PathAnalyzerTestSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PathAnalyzerTestSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PathAnalyzerTestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PathAnalyzerTestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PathAnalyzerTestSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PathAnalyzerTestSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PathAnalyzerTestSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this PathAnalyzerTestSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PathAnalyzerTestSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this PathAnalyzerTestSummary.
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