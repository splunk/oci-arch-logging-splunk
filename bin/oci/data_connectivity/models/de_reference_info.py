# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeReferenceInfo(object):
    """
    Represents de-reference details of a DCMS artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeReferenceInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DeReferenceInfo.
        :type model_type: str

        :param key:
            The value to assign to the key property of this DeReferenceInfo.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DeReferenceInfo.
        :type model_version: str

        :param name:
            The value to assign to the name property of this DeReferenceInfo.
        :type name: str

        :param description:
            The value to assign to the description property of this DeReferenceInfo.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DeReferenceInfo.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this DeReferenceInfo.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this DeReferenceInfo.
        :type identifier: str

        :param dcms_artifact_id:
            The value to assign to the dcms_artifact_id property of this DeReferenceInfo.
        :type dcms_artifact_id: str

        :param service_artifact_id:
            The value to assign to the service_artifact_id property of this DeReferenceInfo.
        :type service_artifact_id: str

        :param reference_count:
            The value to assign to the reference_count property of this DeReferenceInfo.
        :type reference_count: int

        :param registry_metadata:
            The value to assign to the registry_metadata property of this DeReferenceInfo.
        :type registry_metadata: oci.data_connectivity.models.RegistryMetadata

        :param metadata:
            The value to assign to the metadata property of this DeReferenceInfo.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'dcms_artifact_id': 'str',
            'service_artifact_id': 'str',
            'reference_count': 'int',
            'registry_metadata': 'RegistryMetadata',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'dcms_artifact_id': 'dcmsArtifactId',
            'service_artifact_id': 'serviceArtifactId',
            'reference_count': 'referenceCount',
            'registry_metadata': 'registryMetadata',
            'metadata': 'metadata'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._dcms_artifact_id = None
        self._service_artifact_id = None
        self._reference_count = None
        self._registry_metadata = None
        self._metadata = None

    @property
    def model_type(self):
        """
        Gets the model_type of this DeReferenceInfo.
        The type of the ReferenceInfo.


        :return: The model_type of this DeReferenceInfo.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DeReferenceInfo.
        The type of the ReferenceInfo.


        :param model_type: The model_type of this DeReferenceInfo.
        :type: str
        """
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this DeReferenceInfo.
        Generated key that can be used in API calls to identify the referenceinfo.


        :return: The key of this DeReferenceInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DeReferenceInfo.
        Generated key that can be used in API calls to identify the referenceinfo.


        :param key: The key of this DeReferenceInfo.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DeReferenceInfo.
        The model version of an object.


        :return: The model_version of this DeReferenceInfo.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DeReferenceInfo.
        The model version of an object.


        :param model_version: The model_version of this DeReferenceInfo.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this DeReferenceInfo.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DeReferenceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeReferenceInfo.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DeReferenceInfo.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DeReferenceInfo.
        User-defined description of the referenceInfo.


        :return: The description of this DeReferenceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeReferenceInfo.
        User-defined description of the referenceInfo.


        :param description: The description of this DeReferenceInfo.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this DeReferenceInfo.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DeReferenceInfo.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DeReferenceInfo.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DeReferenceInfo.
        :type: int
        """
        self._object_status = object_status

    @property
    def object_version(self):
        """
        Gets the object_version of this DeReferenceInfo.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DeReferenceInfo.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DeReferenceInfo.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DeReferenceInfo.
        :type: int
        """
        self._object_version = object_version

    @property
    def identifier(self):
        """
        Gets the identifier of this DeReferenceInfo.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :return: The identifier of this DeReferenceInfo.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DeReferenceInfo.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DeReferenceInfo.
        :type: str
        """
        self._identifier = identifier

    @property
    def dcms_artifact_id(self):
        """
        **[Required]** Gets the dcms_artifact_id of this DeReferenceInfo.
        The unique ID of the DCMS artifact that is getting referenced.


        :return: The dcms_artifact_id of this DeReferenceInfo.
        :rtype: str
        """
        return self._dcms_artifact_id

    @dcms_artifact_id.setter
    def dcms_artifact_id(self, dcms_artifact_id):
        """
        Sets the dcms_artifact_id of this DeReferenceInfo.
        The unique ID of the DCMS artifact that is getting referenced.


        :param dcms_artifact_id: The dcms_artifact_id of this DeReferenceInfo.
        :type: str
        """
        self._dcms_artifact_id = dcms_artifact_id

    @property
    def service_artifact_id(self):
        """
        **[Required]** Gets the service_artifact_id of this DeReferenceInfo.
        The unique ID of the service that is referencing a DCMS artifact.


        :return: The service_artifact_id of this DeReferenceInfo.
        :rtype: str
        """
        return self._service_artifact_id

    @service_artifact_id.setter
    def service_artifact_id(self, service_artifact_id):
        """
        Sets the service_artifact_id of this DeReferenceInfo.
        The unique ID of the service that is referencing a DCMS artifact.


        :param service_artifact_id: The service_artifact_id of this DeReferenceInfo.
        :type: str
        """
        self._service_artifact_id = service_artifact_id

    @property
    def reference_count(self):
        """
        Gets the reference_count of this DeReferenceInfo.
        The number of times a DCMS artifact has been registered by a service.


        :return: The reference_count of this DeReferenceInfo.
        :rtype: int
        """
        return self._reference_count

    @reference_count.setter
    def reference_count(self, reference_count):
        """
        Sets the reference_count of this DeReferenceInfo.
        The number of times a DCMS artifact has been registered by a service.


        :param reference_count: The reference_count of this DeReferenceInfo.
        :type: int
        """
        self._reference_count = reference_count

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this DeReferenceInfo.

        :return: The registry_metadata of this DeReferenceInfo.
        :rtype: oci.data_connectivity.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this DeReferenceInfo.

        :param registry_metadata: The registry_metadata of this DeReferenceInfo.
        :type: oci.data_connectivity.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    @property
    def metadata(self):
        """
        Gets the metadata of this DeReferenceInfo.

        :return: The metadata of this DeReferenceInfo.
        :rtype: oci.data_connectivity.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DeReferenceInfo.

        :param metadata: The metadata of this DeReferenceInfo.
        :type: oci.data_connectivity.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
