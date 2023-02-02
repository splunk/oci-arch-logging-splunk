# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachVolumeDetails(object):
    """
    AttachVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachVolumeDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.AttachServiceDeterminedVolumeDetails`
        * :class:`~oci.core.models.AttachEmulatedVolumeDetails`
        * :class:`~oci.core.models.AttachIScsiVolumeDetails`
        * :class:`~oci.core.models.AttachParavirtualizedVolumeDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param device:
            The value to assign to the device property of this AttachVolumeDetails.
        :type device: str

        :param display_name:
            The value to assign to the display_name property of this AttachVolumeDetails.
        :type display_name: str

        :param instance_id:
            The value to assign to the instance_id property of this AttachVolumeDetails.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this AttachVolumeDetails.
        :type is_read_only: bool

        :param is_shareable:
            The value to assign to the is_shareable property of this AttachVolumeDetails.
        :type is_shareable: bool

        :param type:
            The value to assign to the type property of this AttachVolumeDetails.
        :type type: str

        :param volume_id:
            The value to assign to the volume_id property of this AttachVolumeDetails.
        :type volume_id: str

        """
        self.swagger_types = {
            'device': 'str',
            'display_name': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
            'is_shareable': 'bool',
            'type': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'device': 'device',
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'is_read_only': 'isReadOnly',
            'is_shareable': 'isShareable',
            'type': 'type',
            'volume_id': 'volumeId'
        }

        self._device = None
        self._display_name = None
        self._instance_id = None
        self._is_read_only = None
        self._is_shareable = None
        self._type = None
        self._volume_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'service_determined':
            return 'AttachServiceDeterminedVolumeDetails'

        if type == 'emulated':
            return 'AttachEmulatedVolumeDetails'

        if type == 'iscsi':
            return 'AttachIScsiVolumeDetails'

        if type == 'paravirtualized':
            return 'AttachParavirtualizedVolumeDetails'
        else:
            return 'AttachVolumeDetails'

    @property
    def device(self):
        """
        Gets the device of this AttachVolumeDetails.
        The device name. To retrieve a list of devices for a given instance, see :func:`list_instance_devices`.


        :return: The device of this AttachVolumeDetails.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this AttachVolumeDetails.
        The device name. To retrieve a list of devices for a given instance, see :func:`list_instance_devices`.


        :param device: The device of this AttachVolumeDetails.
        :type: str
        """
        self._device = device

    @property
    def display_name(self):
        """
        Gets the display_name of this AttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this AttachVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this AttachVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this AttachVolumeDetails.
        The OCID of the instance.


        :return: The instance_id of this AttachVolumeDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this AttachVolumeDetails.
        The OCID of the instance.


        :param instance_id: The instance_id of this AttachVolumeDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def is_read_only(self):
        """
        Gets the is_read_only of this AttachVolumeDetails.
        Whether the attachment was created in read-only mode.


        :return: The is_read_only of this AttachVolumeDetails.
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """
        Sets the is_read_only of this AttachVolumeDetails.
        Whether the attachment was created in read-only mode.


        :param is_read_only: The is_read_only of this AttachVolumeDetails.
        :type: bool
        """
        self._is_read_only = is_read_only

    @property
    def is_shareable(self):
        """
        Gets the is_shareable of this AttachVolumeDetails.
        Whether the attachment should be created in shareable mode. If an attachment
        is created in shareable mode, then other instances can attach the same volume, provided
        that they also create their attachments in shareable mode. Only certain volume types can
        be attached in shareable mode. Defaults to false if not specified.


        :return: The is_shareable of this AttachVolumeDetails.
        :rtype: bool
        """
        return self._is_shareable

    @is_shareable.setter
    def is_shareable(self, is_shareable):
        """
        Sets the is_shareable of this AttachVolumeDetails.
        Whether the attachment should be created in shareable mode. If an attachment
        is created in shareable mode, then other instances can attach the same volume, provided
        that they also create their attachments in shareable mode. Only certain volume types can
        be attached in shareable mode. Defaults to false if not specified.


        :param is_shareable: The is_shareable of this AttachVolumeDetails.
        :type: bool
        """
        self._is_shareable = is_shareable

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AttachVolumeDetails.
        The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".


        :return: The type of this AttachVolumeDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AttachVolumeDetails.
        The type of volume. The only supported values are \"iscsi\" and \"paravirtualized\".


        :param type: The type of this AttachVolumeDetails.
        :type: str
        """
        self._type = type

    @property
    def volume_id(self):
        """
        **[Required]** Gets the volume_id of this AttachVolumeDetails.
        The OCID of the volume.


        :return: The volume_id of this AttachVolumeDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this AttachVolumeDetails.
        The OCID of the volume.


        :param volume_id: The volume_id of this AttachVolumeDetails.
        :type: str
        """
        self._volume_id = volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other