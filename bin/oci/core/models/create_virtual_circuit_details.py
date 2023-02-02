# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVirtualCircuitDetails(object):
    """
    CreateVirtualCircuitDetails model.
    """

    #: A constant which can be used with the routing_policy property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "ORACLE_SERVICE_NETWORK"
    ROUTING_POLICY_ORACLE_SERVICE_NETWORK = "ORACLE_SERVICE_NETWORK"

    #: A constant which can be used with the routing_policy property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "REGIONAL"
    ROUTING_POLICY_REGIONAL = "REGIONAL"

    #: A constant which can be used with the routing_policy property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "MARKET_LEVEL"
    ROUTING_POLICY_MARKET_LEVEL = "MARKET_LEVEL"

    #: A constant which can be used with the routing_policy property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "GLOBAL"
    ROUTING_POLICY_GLOBAL = "GLOBAL"

    #: A constant which can be used with the bgp_admin_state property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "ENABLED"
    BGP_ADMIN_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the bgp_admin_state property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "DISABLED"
    BGP_ADMIN_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the type property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "PUBLIC"
    TYPE_PUBLIC = "PUBLIC"

    #: A constant which can be used with the type property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "PRIVATE"
    TYPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the ip_mtu property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "MTU_1500"
    IP_MTU_MTU_1500 = "MTU_1500"

    #: A constant which can be used with the ip_mtu property of a CreateVirtualCircuitDetails.
    #: This constant has a value of "MTU_9000"
    IP_MTU_MTU_9000 = "MTU_9000"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVirtualCircuitDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bandwidth_shape_name:
            The value to assign to the bandwidth_shape_name property of this CreateVirtualCircuitDetails.
        :type bandwidth_shape_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVirtualCircuitDetails.
        :type compartment_id: str

        :param cross_connect_mappings:
            The value to assign to the cross_connect_mappings property of this CreateVirtualCircuitDetails.
        :type cross_connect_mappings: list[oci.core.models.CrossConnectMapping]

        :param routing_policy:
            The value to assign to the routing_policy property of this CreateVirtualCircuitDetails.
            Allowed values for items in this list are: "ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"
        :type routing_policy: list[str]

        :param bgp_admin_state:
            The value to assign to the bgp_admin_state property of this CreateVirtualCircuitDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type bgp_admin_state: str

        :param is_bfd_enabled:
            The value to assign to the is_bfd_enabled property of this CreateVirtualCircuitDetails.
        :type is_bfd_enabled: bool

        :param customer_bgp_asn:
            The value to assign to the customer_bgp_asn property of this CreateVirtualCircuitDetails.
        :type customer_bgp_asn: int

        :param customer_asn:
            The value to assign to the customer_asn property of this CreateVirtualCircuitDetails.
        :type customer_asn: int

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVirtualCircuitDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateVirtualCircuitDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVirtualCircuitDetails.
        :type freeform_tags: dict(str, str)

        :param gateway_id:
            The value to assign to the gateway_id property of this CreateVirtualCircuitDetails.
        :type gateway_id: str

        :param provider_name:
            The value to assign to the provider_name property of this CreateVirtualCircuitDetails.
        :type provider_name: str

        :param provider_service_id:
            The value to assign to the provider_service_id property of this CreateVirtualCircuitDetails.
        :type provider_service_id: str

        :param provider_service_key_name:
            The value to assign to the provider_service_key_name property of this CreateVirtualCircuitDetails.
        :type provider_service_key_name: str

        :param provider_service_name:
            The value to assign to the provider_service_name property of this CreateVirtualCircuitDetails.
        :type provider_service_name: str

        :param public_prefixes:
            The value to assign to the public_prefixes property of this CreateVirtualCircuitDetails.
        :type public_prefixes: list[oci.core.models.CreateVirtualCircuitPublicPrefixDetails]

        :param region:
            The value to assign to the region property of this CreateVirtualCircuitDetails.
        :type region: str

        :param type:
            The value to assign to the type property of this CreateVirtualCircuitDetails.
            Allowed values for this property are: "PUBLIC", "PRIVATE"
        :type type: str

        :param ip_mtu:
            The value to assign to the ip_mtu property of this CreateVirtualCircuitDetails.
            Allowed values for this property are: "MTU_1500", "MTU_9000"
        :type ip_mtu: str

        """
        self.swagger_types = {
            'bandwidth_shape_name': 'str',
            'compartment_id': 'str',
            'cross_connect_mappings': 'list[CrossConnectMapping]',
            'routing_policy': 'list[str]',
            'bgp_admin_state': 'str',
            'is_bfd_enabled': 'bool',
            'customer_bgp_asn': 'int',
            'customer_asn': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'gateway_id': 'str',
            'provider_name': 'str',
            'provider_service_id': 'str',
            'provider_service_key_name': 'str',
            'provider_service_name': 'str',
            'public_prefixes': 'list[CreateVirtualCircuitPublicPrefixDetails]',
            'region': 'str',
            'type': 'str',
            'ip_mtu': 'str'
        }

        self.attribute_map = {
            'bandwidth_shape_name': 'bandwidthShapeName',
            'compartment_id': 'compartmentId',
            'cross_connect_mappings': 'crossConnectMappings',
            'routing_policy': 'routingPolicy',
            'bgp_admin_state': 'bgpAdminState',
            'is_bfd_enabled': 'isBfdEnabled',
            'customer_bgp_asn': 'customerBgpAsn',
            'customer_asn': 'customerAsn',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'gateway_id': 'gatewayId',
            'provider_name': 'providerName',
            'provider_service_id': 'providerServiceId',
            'provider_service_key_name': 'providerServiceKeyName',
            'provider_service_name': 'providerServiceName',
            'public_prefixes': 'publicPrefixes',
            'region': 'region',
            'type': 'type',
            'ip_mtu': 'ipMtu'
        }

        self._bandwidth_shape_name = None
        self._compartment_id = None
        self._cross_connect_mappings = None
        self._routing_policy = None
        self._bgp_admin_state = None
        self._is_bfd_enabled = None
        self._customer_bgp_asn = None
        self._customer_asn = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._gateway_id = None
        self._provider_name = None
        self._provider_service_id = None
        self._provider_service_key_name = None
        self._provider_service_name = None
        self._public_prefixes = None
        self._region = None
        self._type = None
        self._ip_mtu = None

    @property
    def bandwidth_shape_name(self):
        """
        Gets the bandwidth_shape_name of this CreateVirtualCircuitDetails.
        The provisioned data rate of the connection. To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :return: The bandwidth_shape_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._bandwidth_shape_name

    @bandwidth_shape_name.setter
    def bandwidth_shape_name(self, bandwidth_shape_name):
        """
        Sets the bandwidth_shape_name of this CreateVirtualCircuitDetails.
        The provisioned data rate of the connection. To get a list of the
        available bandwidth levels (that is, shapes), see
        :func:`list_fast_connect_provider_virtual_circuit_bandwidth_shapes`.

        Example: `10 Gbps`


        :param bandwidth_shape_name: The bandwidth_shape_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._bandwidth_shape_name = bandwidth_shape_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateVirtualCircuitDetails.
        The `OCID`__ of the compartment to contain the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVirtualCircuitDetails.
        The `OCID`__ of the compartment to contain the virtual circuit.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cross_connect_mappings(self):
        """
        Gets the cross_connect_mappings of this CreateVirtualCircuitDetails.
        Create a `CrossConnectMapping` for each cross-connect or cross-connect
        group this virtual circuit will run on.


        :return: The cross_connect_mappings of this CreateVirtualCircuitDetails.
        :rtype: list[oci.core.models.CrossConnectMapping]
        """
        return self._cross_connect_mappings

    @cross_connect_mappings.setter
    def cross_connect_mappings(self, cross_connect_mappings):
        """
        Sets the cross_connect_mappings of this CreateVirtualCircuitDetails.
        Create a `CrossConnectMapping` for each cross-connect or cross-connect
        group this virtual circuit will run on.


        :param cross_connect_mappings: The cross_connect_mappings of this CreateVirtualCircuitDetails.
        :type: list[oci.core.models.CrossConnectMapping]
        """
        self._cross_connect_mappings = cross_connect_mappings

    @property
    def routing_policy(self):
        """
        Gets the routing_policy of this CreateVirtualCircuitDetails.
        The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit.
        Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`.
        See `Route Filtering`__ for details.
        By default, routing information is shared for all routes in the same market.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering

        Allowed values for items in this list are: "ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"


        :return: The routing_policy of this CreateVirtualCircuitDetails.
        :rtype: list[str]
        """
        return self._routing_policy

    @routing_policy.setter
    def routing_policy(self, routing_policy):
        """
        Sets the routing_policy of this CreateVirtualCircuitDetails.
        The routing policy sets how routing information about the Oracle cloud is shared over a public virtual circuit.
        Policies available are: `ORACLE_SERVICE_NETWORK`, `REGIONAL`, `MARKET_LEVEL`, and `GLOBAL`.
        See `Route Filtering`__ for details.
        By default, routing information is shared for all routes in the same market.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/routingonprem.htm#route_filtering


        :param routing_policy: The routing_policy of this CreateVirtualCircuitDetails.
        :type: list[str]
        """
        allowed_values = ["ORACLE_SERVICE_NETWORK", "REGIONAL", "MARKET_LEVEL", "GLOBAL"]

        if routing_policy and routing_policy is not NONE_SENTINEL:
            for value in routing_policy:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `routing_policy`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._routing_policy = routing_policy

    @property
    def bgp_admin_state(self):
        """
        Gets the bgp_admin_state of this CreateVirtualCircuitDetails.
        Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The bgp_admin_state of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._bgp_admin_state

    @bgp_admin_state.setter
    def bgp_admin_state(self, bgp_admin_state):
        """
        Sets the bgp_admin_state of this CreateVirtualCircuitDetails.
        Set to `ENABLED` (the default) to activate the BGP session of the virtual circuit, set to `DISABLED` to deactivate the virtual circuit.


        :param bgp_admin_state: The bgp_admin_state of this CreateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(bgp_admin_state, allowed_values):
            raise ValueError(
                "Invalid value for `bgp_admin_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._bgp_admin_state = bgp_admin_state

    @property
    def is_bfd_enabled(self):
        """
        Gets the is_bfd_enabled of this CreateVirtualCircuitDetails.
        Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.


        :return: The is_bfd_enabled of this CreateVirtualCircuitDetails.
        :rtype: bool
        """
        return self._is_bfd_enabled

    @is_bfd_enabled.setter
    def is_bfd_enabled(self, is_bfd_enabled):
        """
        Sets the is_bfd_enabled of this CreateVirtualCircuitDetails.
        Set to `true` to enable BFD for IPv4 BGP peering, or set to `false` to disable BFD. If this is not set, the default is `false`.


        :param is_bfd_enabled: The is_bfd_enabled of this CreateVirtualCircuitDetails.
        :type: bool
        """
        self._is_bfd_enabled = is_bfd_enabled

    @property
    def customer_bgp_asn(self):
        """
        Gets the customer_bgp_asn of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `customerAsn`.
        If you specify values for both, the request will be rejected.


        :return: The customer_bgp_asn of this CreateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_bgp_asn

    @customer_bgp_asn.setter
    def customer_bgp_asn(self, customer_bgp_asn):
        """
        Sets the customer_bgp_asn of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `customerAsn`.
        If you specify values for both, the request will be rejected.


        :param customer_bgp_asn: The customer_bgp_asn of this CreateVirtualCircuitDetails.
        :type: int
        """
        self._customer_bgp_asn = customer_bgp_asn

    @property
    def customer_asn(self):
        """
        Gets the customer_asn of this CreateVirtualCircuitDetails.
        Your BGP ASN (either public or private). Provide this value only if
        there's a BGP session that goes from your edge router to Oracle.
        Otherwise, leave this empty or null.
        Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

        Example: `12345` (2-byte) or `1587232876` (4-byte)


        :return: The customer_asn of this CreateVirtualCircuitDetails.
        :rtype: int
        """
        return self._customer_asn

    @customer_asn.setter
    def customer_asn(self, customer_asn):
        """
        Sets the customer_asn of this CreateVirtualCircuitDetails.
        Your BGP ASN (either public or private). Provide this value only if
        there's a BGP session that goes from your edge router to Oracle.
        Otherwise, leave this empty or null.
        Can be a 2-byte or 4-byte ASN. Uses \"asplain\" format.

        Example: `12345` (2-byte) or `1587232876` (4-byte)


        :param customer_asn: The customer_asn of this CreateVirtualCircuitDetails.
        :type: int
        """
        self._customer_asn = customer_asn

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateVirtualCircuitDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateVirtualCircuitDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateVirtualCircuitDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateVirtualCircuitDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVirtualCircuitDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateVirtualCircuitDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateVirtualCircuitDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateVirtualCircuitDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateVirtualCircuitDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def gateway_id(self):
        """
        Gets the gateway_id of this CreateVirtualCircuitDetails.
        For private virtual circuits only. The `OCID`__ of the :class:`Drg`
        that this virtual circuit uses.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The gateway_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """
        Sets the gateway_id of this CreateVirtualCircuitDetails.
        For private virtual circuits only. The `OCID`__ of the :class:`Drg`
        that this virtual circuit uses.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param gateway_id: The gateway_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._gateway_id = gateway_id

    @property
    def provider_name(self):
        """
        Gets the provider_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :return: The provider_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """
        Sets the provider_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :param provider_name: The provider_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_name = provider_name

    @property
    def provider_service_id(self):
        """
        Gets the provider_service_id of this CreateVirtualCircuitDetails.
        The `OCID`__ of the service offered by the provider (if you're connecting
        via a provider). To get a list of the available service offerings, see
        :func:`list_fast_connect_provider_services`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The provider_service_id of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_id

    @provider_service_id.setter
    def provider_service_id(self, provider_service_id):
        """
        Sets the provider_service_id of this CreateVirtualCircuitDetails.
        The `OCID`__ of the service offered by the provider (if you're connecting
        via a provider). To get a list of the available service offerings, see
        :func:`list_fast_connect_provider_services`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param provider_service_id: The provider_service_id of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_id = provider_service_id

    @property
    def provider_service_key_name(self):
        """
        Gets the provider_service_key_name of this CreateVirtualCircuitDetails.
        The service key name offered by the provider (if the customer is connecting via a provider).


        :return: The provider_service_key_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_key_name

    @provider_service_key_name.setter
    def provider_service_key_name(self, provider_service_key_name):
        """
        Sets the provider_service_key_name of this CreateVirtualCircuitDetails.
        The service key name offered by the provider (if the customer is connecting via a provider).


        :param provider_service_key_name: The provider_service_key_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_key_name = provider_service_key_name

    @property
    def provider_service_name(self):
        """
        Gets the provider_service_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :return: The provider_service_name of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._provider_service_name

    @provider_service_name.setter
    def provider_service_name(self, provider_service_name):
        """
        Sets the provider_service_name of this CreateVirtualCircuitDetails.
        Deprecated. Instead use `providerServiceId`.
        To get a list of the provider names, see
        :func:`list_fast_connect_provider_services`.


        :param provider_service_name: The provider_service_name of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._provider_service_name = provider_service_name

    @property
    def public_prefixes(self):
        """
        Gets the public_prefixes of this CreateVirtualCircuitDetails.
        For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
        advertise across the connection.


        :return: The public_prefixes of this CreateVirtualCircuitDetails.
        :rtype: list[oci.core.models.CreateVirtualCircuitPublicPrefixDetails]
        """
        return self._public_prefixes

    @public_prefixes.setter
    def public_prefixes(self, public_prefixes):
        """
        Sets the public_prefixes of this CreateVirtualCircuitDetails.
        For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
        advertise across the connection.


        :param public_prefixes: The public_prefixes of this CreateVirtualCircuitDetails.
        :type: list[oci.core.models.CreateVirtualCircuitPublicPrefixDetails]
        """
        self._public_prefixes = public_prefixes

    @property
    def region(self):
        """
        Gets the region of this CreateVirtualCircuitDetails.
        The Oracle Cloud Infrastructure region where this virtual
        circuit is located.
        Example: `phx`


        :return: The region of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CreateVirtualCircuitDetails.
        The Oracle Cloud Infrastructure region where this virtual
        circuit is located.
        Example: `phx`


        :param region: The region of this CreateVirtualCircuitDetails.
        :type: str
        """
        self._region = region

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateVirtualCircuitDetails.
        The type of IP addresses used in this virtual circuit. PRIVATE
        means `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16).

        __ https://tools.ietf.org/html/rfc1918

        Allowed values for this property are: "PUBLIC", "PRIVATE"


        :return: The type of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateVirtualCircuitDetails.
        The type of IP addresses used in this virtual circuit. PRIVATE
        means `RFC 1918`__ addresses
        (10.0.0.0/8, 172.16/12, and 192.168/16).

        __ https://tools.ietf.org/html/rfc1918


        :param type: The type of this CreateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["PUBLIC", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def ip_mtu(self):
        """
        Gets the ip_mtu of this CreateVirtualCircuitDetails.
        The layer 3 IP MTU to use with this virtual circuit.

        Allowed values for this property are: "MTU_1500", "MTU_9000"


        :return: The ip_mtu of this CreateVirtualCircuitDetails.
        :rtype: str
        """
        return self._ip_mtu

    @ip_mtu.setter
    def ip_mtu(self, ip_mtu):
        """
        Sets the ip_mtu of this CreateVirtualCircuitDetails.
        The layer 3 IP MTU to use with this virtual circuit.


        :param ip_mtu: The ip_mtu of this CreateVirtualCircuitDetails.
        :type: str
        """
        allowed_values = ["MTU_1500", "MTU_9000"]
        if not value_allowed_none_or_none_sentinel(ip_mtu, allowed_values):
            raise ValueError(
                "Invalid value for `ip_mtu`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ip_mtu = ip_mtu

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other