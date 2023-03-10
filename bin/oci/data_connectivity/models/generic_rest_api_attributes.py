# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_operation_attributes import AbstractOperationAttributes
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericRestApiAttributes(AbstractOperationAttributes):
    """
    Generic rest api specific attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericRestApiAttributes object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.GenericRestApiAttributes.model_type` attribute
        of this class is ``GENERIC_REST_API_ATTRIBUTES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this GenericRestApiAttributes.
            Allowed values for this property are: "GENERIC_REST_API_ATTRIBUTES"
        :type model_type: str

        :param server_url:
            The value to assign to the server_url property of this GenericRestApiAttributes.
        :type server_url: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'server_url': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'server_url': 'serverUrl'
        }

        self._model_type = None
        self._server_url = None
        self._model_type = 'GENERIC_REST_API_ATTRIBUTES'

    @property
    def server_url(self):
        """
        Gets the server_url of this GenericRestApiAttributes.
        The server Url serving operation.


        :return: The server_url of this GenericRestApiAttributes.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """
        Sets the server_url of this GenericRestApiAttributes.
        The server Url serving operation.


        :param server_url: The server_url of this GenericRestApiAttributes.
        :type: str
        """
        self._server_url = server_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
