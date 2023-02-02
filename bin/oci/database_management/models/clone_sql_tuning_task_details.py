# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloneSqlTuningTaskDetails(object):
    """
    The request to clone and run a SQL tuning task. The new task uses the same inputs as the one being cloned.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloneSqlTuningTaskDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_name:
            The value to assign to the task_name property of this CloneSqlTuningTaskDetails.
        :type task_name: str

        :param original_task_id:
            The value to assign to the original_task_id property of this CloneSqlTuningTaskDetails.
        :type original_task_id: int

        :param task_description:
            The value to assign to the task_description property of this CloneSqlTuningTaskDetails.
        :type task_description: str

        :param credential_details:
            The value to assign to the credential_details property of this CloneSqlTuningTaskDetails.
        :type credential_details: oci.database_management.models.SqlTuningTaskCredentialDetails

        """
        self.swagger_types = {
            'task_name': 'str',
            'original_task_id': 'int',
            'task_description': 'str',
            'credential_details': 'SqlTuningTaskCredentialDetails'
        }

        self.attribute_map = {
            'task_name': 'taskName',
            'original_task_id': 'originalTaskId',
            'task_description': 'taskDescription',
            'credential_details': 'credentialDetails'
        }

        self._task_name = None
        self._original_task_id = None
        self._task_description = None
        self._credential_details = None

    @property
    def task_name(self):
        """
        **[Required]** Gets the task_name of this CloneSqlTuningTaskDetails.
        The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.


        :return: The task_name of this CloneSqlTuningTaskDetails.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this CloneSqlTuningTaskDetails.
        The name of the SQL tuning task. The name is unique per user in a database, and it is case-sensitive.


        :param task_name: The task_name of this CloneSqlTuningTaskDetails.
        :type: str
        """
        self._task_name = task_name

    @property
    def original_task_id(self):
        """
        **[Required]** Gets the original_task_id of this CloneSqlTuningTaskDetails.
        The identifier of the SQL tuning task being cloned. This is not the `OCID`__.
        It can be retrieved from the following endpoint
        :func:`list_sql_tuning_advisor_tasks`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The original_task_id of this CloneSqlTuningTaskDetails.
        :rtype: int
        """
        return self._original_task_id

    @original_task_id.setter
    def original_task_id(self, original_task_id):
        """
        Sets the original_task_id of this CloneSqlTuningTaskDetails.
        The identifier of the SQL tuning task being cloned. This is not the `OCID`__.
        It can be retrieved from the following endpoint
        :func:`list_sql_tuning_advisor_tasks`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param original_task_id: The original_task_id of this CloneSqlTuningTaskDetails.
        :type: int
        """
        self._original_task_id = original_task_id

    @property
    def task_description(self):
        """
        Gets the task_description of this CloneSqlTuningTaskDetails.
        The description of the SQL tuning task.


        :return: The task_description of this CloneSqlTuningTaskDetails.
        :rtype: str
        """
        return self._task_description

    @task_description.setter
    def task_description(self, task_description):
        """
        Sets the task_description of this CloneSqlTuningTaskDetails.
        The description of the SQL tuning task.


        :param task_description: The task_description of this CloneSqlTuningTaskDetails.
        :type: str
        """
        self._task_description = task_description

    @property
    def credential_details(self):
        """
        **[Required]** Gets the credential_details of this CloneSqlTuningTaskDetails.

        :return: The credential_details of this CloneSqlTuningTaskDetails.
        :rtype: oci.database_management.models.SqlTuningTaskCredentialDetails
        """
        return self._credential_details

    @credential_details.setter
    def credential_details(self, credential_details):
        """
        Sets the credential_details of this CloneSqlTuningTaskDetails.

        :param credential_details: The credential_details of this CloneSqlTuningTaskDetails.
        :type: oci.database_management.models.SqlTuningTaskCredentialDetails
        """
        self._credential_details = credential_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other