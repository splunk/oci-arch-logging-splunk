# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateByoipRangeDetails(object):
    """
    The information used to create a `ByoipRange` resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateByoipRangeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this CreateByoipRangeDetails.
        :type cidr_block: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateByoipRangeDetails.
        :type compartment_id: str

        :param ipv6_cidr_block:
            The value to assign to the ipv6_cidr_block property of this CreateByoipRangeDetails.
        :type ipv6_cidr_block: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateByoipRangeDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateByoipRangeDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateByoipRangeDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'compartment_id': 'str',
            'ipv6_cidr_block': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'ipv6_cidr_block': 'ipv6CidrBlock',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags'
        }

        self._cidr_block = None
        self._compartment_id = None
        self._ipv6_cidr_block = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this CreateByoipRangeDetails.
        The BYOIP CIDR block. You can assign some or all of it to a public IP pool after it is validated.
        Example: `10.0.1.0/24`


        :return: The cidr_block of this CreateByoipRangeDetails.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this CreateByoipRangeDetails.
        The BYOIP CIDR block. You can assign some or all of it to a public IP pool after it is validated.
        Example: `10.0.1.0/24`


        :param cidr_block: The cidr_block of this CreateByoipRangeDetails.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateByoipRangeDetails.
        The `OCID`__ of the compartment containing the BYOIP CIDR block.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateByoipRangeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateByoipRangeDetails.
        The `OCID`__ of the compartment containing the BYOIP CIDR block.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateByoipRangeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ipv6_cidr_block(self):
        """
        Gets the ipv6_cidr_block of this CreateByoipRangeDetails.
        The BYOIPv6 CIDR block. You can assign some or all of it to a VCN after it is validated.


        :return: The ipv6_cidr_block of this CreateByoipRangeDetails.
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """
        Sets the ipv6_cidr_block of this CreateByoipRangeDetails.
        The BYOIPv6 CIDR block. You can assign some or all of it to a VCN after it is validated.


        :param ipv6_cidr_block: The ipv6_cidr_block of this CreateByoipRangeDetails.
        :type: str
        """
        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateByoipRangeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateByoipRangeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateByoipRangeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateByoipRangeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateByoipRangeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateByoipRangeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateByoipRangeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateByoipRangeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateByoipRangeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateByoipRangeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateByoipRangeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateByoipRangeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other