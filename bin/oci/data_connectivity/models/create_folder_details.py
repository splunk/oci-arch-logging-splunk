# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFolderDetails(object):
    """
    Properties used in the create operations of the folder.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFolderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateFolderDetails.
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateFolderDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateFolderDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateFolderDetails.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateFolderDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateFolderDetails.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this CreateFolderDetails.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this CreateFolderDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateFolderDetails.
        :type identifier: str

        :param data_assets:
            The value to assign to the data_assets property of this CreateFolderDetails.
        :type data_assets: list[oci.data_connectivity.models.DataAsset]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'data_assets': 'list[DataAsset]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'data_assets': 'dataAssets'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._data_assets = None

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateFolderDetails.
        The type of the folder.


        :return: The model_type of this CreateFolderDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateFolderDetails.
        The type of the folder.


        :param model_type: The model_type of this CreateFolderDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateFolderDetails.
        Generated key that can be used in API calls to identify the folder. In scenarios where reference to the folder is required, a value can be passed in create.


        :return: The key of this CreateFolderDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateFolderDetails.
        Generated key that can be used in API calls to identify the folder. In scenarios where reference to the folder is required, a value can be passed in create.


        :param key: The key of this CreateFolderDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateFolderDetails.
        The model version of an object.


        :return: The model_version of this CreateFolderDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateFolderDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateFolderDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateFolderDetails.

        :return: The parent_ref of this CreateFolderDetails.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateFolderDetails.

        :param parent_ref: The parent_ref of this CreateFolderDetails.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateFolderDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateFolderDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateFolderDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateFolderDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateFolderDetails.
        User-defined description of the folder.


        :return: The description of this CreateFolderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateFolderDetails.
        User-defined description of the folder.


        :param description: The description of this CreateFolderDetails.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this CreateFolderDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CreateFolderDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CreateFolderDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CreateFolderDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateFolderDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateFolderDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateFolderDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateFolderDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateFolderDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateFolderDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateFolderDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateFolderDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def data_assets(self):
        """
        Gets the data_assets of this CreateFolderDetails.
        The list of data assets that belong to the folder.


        :return: The data_assets of this CreateFolderDetails.
        :rtype: list[oci.data_connectivity.models.DataAsset]
        """
        return self._data_assets

    @data_assets.setter
    def data_assets(self, data_assets):
        """
        Sets the data_assets of this CreateFolderDetails.
        The list of data assets that belong to the folder.


        :param data_assets: The data_assets of this CreateFolderDetails.
        :type: list[oci.data_connectivity.models.DataAsset]
        """
        self._data_assets = data_assets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
