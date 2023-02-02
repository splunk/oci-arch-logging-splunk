# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportKeyDetails(object):
    """
    The details of the key that you want to wrap and export.
    """

    #: A constant which can be used with the algorithm property of a ExportKeyDetails.
    #: This constant has a value of "RSA_OAEP_AES_SHA256"
    ALGORITHM_RSA_OAEP_AES_SHA256 = "RSA_OAEP_AES_SHA256"

    #: A constant which can be used with the algorithm property of a ExportKeyDetails.
    #: This constant has a value of "RSA_OAEP_SHA256"
    ALGORITHM_RSA_OAEP_SHA256 = "RSA_OAEP_SHA256"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_id:
            The value to assign to the key_id property of this ExportKeyDetails.
        :type key_id: str

        :param key_version_id:
            The value to assign to the key_version_id property of this ExportKeyDetails.
        :type key_version_id: str

        :param algorithm:
            The value to assign to the algorithm property of this ExportKeyDetails.
            Allowed values for this property are: "RSA_OAEP_AES_SHA256", "RSA_OAEP_SHA256"
        :type algorithm: str

        :param public_key:
            The value to assign to the public_key property of this ExportKeyDetails.
        :type public_key: str

        :param logging_context:
            The value to assign to the logging_context property of this ExportKeyDetails.
        :type logging_context: dict(str, str)

        """
        self.swagger_types = {
            'key_id': 'str',
            'key_version_id': 'str',
            'algorithm': 'str',
            'public_key': 'str',
            'logging_context': 'dict(str, str)'
        }

        self.attribute_map = {
            'key_id': 'keyId',
            'key_version_id': 'keyVersionId',
            'algorithm': 'algorithm',
            'public_key': 'publicKey',
            'logging_context': 'loggingContext'
        }

        self._key_id = None
        self._key_version_id = None
        self._algorithm = None
        self._public_key = None
        self._logging_context = None

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this ExportKeyDetails.
        The OCID of the master encryption key associated with the key version you want to export.


        :return: The key_id of this ExportKeyDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this ExportKeyDetails.
        The OCID of the master encryption key associated with the key version you want to export.


        :param key_id: The key_id of this ExportKeyDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_version_id(self):
        """
        Gets the key_version_id of this ExportKeyDetails.
        The OCID of the specific key version to export. If not specified, the service exports the current key version.


        :return: The key_version_id of this ExportKeyDetails.
        :rtype: str
        """
        return self._key_version_id

    @key_version_id.setter
    def key_version_id(self, key_version_id):
        """
        Sets the key_version_id of this ExportKeyDetails.
        The OCID of the specific key version to export. If not specified, the service exports the current key version.


        :param key_version_id: The key_version_id of this ExportKeyDetails.
        :type: str
        """
        self._key_version_id = key_version_id

    @property
    def algorithm(self):
        """
        **[Required]** Gets the algorithm of this ExportKeyDetails.
        The encryption algorithm to use to encrypt exportable key material from a software-backed key. Specifying `RSA_OAEP_AES_SHA256`
        invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the RSA public
        wrapping key provided along with the request, creating a wrapped temporary AES key. The temporary AES key is also used to wrap
        the exportable key material. The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing
        concatenated blob output that jointly represents them. Specifying `RSA_OAEP_SHA256` means that the software key is wrapped by
        the RSA public wrapping key provided along with the request.

        Allowed values for this property are: "RSA_OAEP_AES_SHA256", "RSA_OAEP_SHA256"


        :return: The algorithm of this ExportKeyDetails.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """
        Sets the algorithm of this ExportKeyDetails.
        The encryption algorithm to use to encrypt exportable key material from a software-backed key. Specifying `RSA_OAEP_AES_SHA256`
        invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the RSA public
        wrapping key provided along with the request, creating a wrapped temporary AES key. The temporary AES key is also used to wrap
        the exportable key material. The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing
        concatenated blob output that jointly represents them. Specifying `RSA_OAEP_SHA256` means that the software key is wrapped by
        the RSA public wrapping key provided along with the request.


        :param algorithm: The algorithm of this ExportKeyDetails.
        :type: str
        """
        allowed_values = ["RSA_OAEP_AES_SHA256", "RSA_OAEP_SHA256"]
        if not value_allowed_none_or_none_sentinel(algorithm, allowed_values):
            raise ValueError(
                "Invalid value for `algorithm`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._algorithm = algorithm

    @property
    def public_key(self):
        """
        **[Required]** Gets the public_key of this ExportKeyDetails.
        The PEM format of the 2048-bit, 3072-bit, or 4096-bit RSA wrapping key in your possession that you want to use to encrypt the key.


        :return: The public_key of this ExportKeyDetails.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this ExportKeyDetails.
        The PEM format of the 2048-bit, 3072-bit, or 4096-bit RSA wrapping key in your possession that you want to use to encrypt the key.


        :param public_key: The public_key of this ExportKeyDetails.
        :type: str
        """
        self._public_key = public_key

    @property
    def logging_context(self):
        """
        Gets the logging_context of this ExportKeyDetails.
        Information that provides context for audit logging. You can provide this additional
        data as key-value pairs to include in the audit logs when audit logging is enabled.


        :return: The logging_context of this ExportKeyDetails.
        :rtype: dict(str, str)
        """
        return self._logging_context

    @logging_context.setter
    def logging_context(self, logging_context):
        """
        Sets the logging_context of this ExportKeyDetails.
        Information that provides context for audit logging. You can provide this additional
        data as key-value pairs to include in the audit logs when audit logging is enabled.


        :param logging_context: The logging_context of this ExportKeyDetails.
        :type: dict(str, str)
        """
        self._logging_context = logging_context

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other