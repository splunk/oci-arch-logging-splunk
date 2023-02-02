# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricBasedHorizontalScaleInConfig(object):
    """
    Configration for a metric based horizontal scale-in policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricBasedHorizontalScaleInConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric:
            The value to assign to the metric property of this MetricBasedHorizontalScaleInConfig.
        :type metric: oci.bds.models.AutoScalePolicyMetricRule

        :param min_node_count:
            The value to assign to the min_node_count property of this MetricBasedHorizontalScaleInConfig.
        :type min_node_count: int

        :param step_size:
            The value to assign to the step_size property of this MetricBasedHorizontalScaleInConfig.
        :type step_size: int

        """
        self.swagger_types = {
            'metric': 'AutoScalePolicyMetricRule',
            'min_node_count': 'int',
            'step_size': 'int'
        }

        self.attribute_map = {
            'metric': 'metric',
            'min_node_count': 'minNodeCount',
            'step_size': 'stepSize'
        }

        self._metric = None
        self._min_node_count = None
        self._step_size = None

    @property
    def metric(self):
        """
        Gets the metric of this MetricBasedHorizontalScaleInConfig.

        :return: The metric of this MetricBasedHorizontalScaleInConfig.
        :rtype: oci.bds.models.AutoScalePolicyMetricRule
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MetricBasedHorizontalScaleInConfig.

        :param metric: The metric of this MetricBasedHorizontalScaleInConfig.
        :type: oci.bds.models.AutoScalePolicyMetricRule
        """
        self._metric = metric

    @property
    def min_node_count(self):
        """
        Gets the min_node_count of this MetricBasedHorizontalScaleInConfig.
        This value is the minimum number of nodes the cluster can be scaled-in to.


        :return: The min_node_count of this MetricBasedHorizontalScaleInConfig.
        :rtype: int
        """
        return self._min_node_count

    @min_node_count.setter
    def min_node_count(self, min_node_count):
        """
        Sets the min_node_count of this MetricBasedHorizontalScaleInConfig.
        This value is the minimum number of nodes the cluster can be scaled-in to.


        :param min_node_count: The min_node_count of this MetricBasedHorizontalScaleInConfig.
        :type: int
        """
        self._min_node_count = min_node_count

    @property
    def step_size(self):
        """
        Gets the step_size of this MetricBasedHorizontalScaleInConfig.
        This value is the number of nodes to remove during a scale-in event.


        :return: The step_size of this MetricBasedHorizontalScaleInConfig.
        :rtype: int
        """
        return self._step_size

    @step_size.setter
    def step_size(self, step_size):
        """
        Sets the step_size of this MetricBasedHorizontalScaleInConfig.
        This value is the number of nodes to remove during a scale-in event.


        :param step_size: The step_size of this MetricBasedHorizontalScaleInConfig.
        :type: int
        """
        self._step_size = step_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other