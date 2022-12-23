# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.3
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Cluster(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'earliest_story': 'datetime',
        'id': 'int',
        'latest_story': 'datetime',
        'location': 'Location',
        'representative_story': 'RepresentativeStory',
        'story_count': 'int',
        'time': 'datetime'
    }

    attribute_map = {
        'earliest_story': 'earliest_story',
        'id': 'id',
        'latest_story': 'latest_story',
        'location': 'location',
        'representative_story': 'representative_story',
        'story_count': 'story_count',
        'time': 'time'
    }

    def __init__(self, earliest_story=None, id=None, latest_story=None, location=None, representative_story=None, story_count=None, time=None, local_vars_configuration=None):  # noqa: E501
        """Cluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._earliest_story = None
        self._id = None
        self._latest_story = None
        self._location = None
        self._representative_story = None
        self._story_count = None
        self._time = None
        self.discriminator = None

        if earliest_story is not None:
            self.earliest_story = earliest_story
        if id is not None:
            self.id = id
        if latest_story is not None:
            self.latest_story = latest_story
        if location is not None:
            self.location = location
        if representative_story is not None:
            self.representative_story = representative_story
        if story_count is not None:
            self.story_count = story_count
        if time is not None:
            self.time = time

    @property
    def earliest_story(self):
        """Gets the earliest_story of this Cluster.  # noqa: E501

        Publication date of the earliest story in cluster  # noqa: E501

        :return: The earliest_story of this Cluster.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_story

    @earliest_story.setter
    def earliest_story(self, earliest_story):
        """Sets the earliest_story of this Cluster.

        Publication date of the earliest story in cluster  # noqa: E501

        :param earliest_story: The earliest_story of this Cluster.  # noqa: E501
        :type earliest_story: datetime
        """

        self._earliest_story = earliest_story

    @property
    def id(self):
        """Gets the id of this Cluster.  # noqa: E501

        ID of the cluster which is a unique identification  # noqa: E501

        :return: The id of this Cluster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cluster.

        ID of the cluster which is a unique identification  # noqa: E501

        :param id: The id of this Cluster.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def latest_story(self):
        """Gets the latest_story of this Cluster.  # noqa: E501

        Publication date of the latest story in cluster  # noqa: E501

        :return: The latest_story of this Cluster.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_story

    @latest_story.setter
    def latest_story(self, latest_story):
        """Sets the latest_story of this Cluster.

        Publication date of the latest story in cluster  # noqa: E501

        :param latest_story: The latest_story of this Cluster.  # noqa: E501
        :type latest_story: datetime
        """

        self._latest_story = latest_story

    @property
    def location(self):
        """Gets the location of this Cluster.  # noqa: E501


        :return: The location of this Cluster.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Cluster.


        :param location: The location of this Cluster.  # noqa: E501
        :type location: Location
        """

        self._location = location

    @property
    def representative_story(self):
        """Gets the representative_story of this Cluster.  # noqa: E501


        :return: The representative_story of this Cluster.  # noqa: E501
        :rtype: RepresentativeStory
        """
        return self._representative_story

    @representative_story.setter
    def representative_story(self, representative_story):
        """Sets the representative_story of this Cluster.


        :param representative_story: The representative_story of this Cluster.  # noqa: E501
        :type representative_story: RepresentativeStory
        """

        self._representative_story = representative_story

    @property
    def story_count(self):
        """Gets the story_count of this Cluster.  # noqa: E501

        Number of stories associated with the cluster  # noqa: E501

        :return: The story_count of this Cluster.  # noqa: E501
        :rtype: int
        """
        return self._story_count

    @story_count.setter
    def story_count(self, story_count):
        """Sets the story_count of this Cluster.

        Number of stories associated with the cluster  # noqa: E501

        :param story_count: The story_count of this Cluster.  # noqa: E501
        :type story_count: int
        """

        self._story_count = story_count

    @property
    def time(self):
        """Gets the time of this Cluster.  # noqa: E501

        Time of the event  # noqa: E501

        :return: The time of this Cluster.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Cluster.

        Time of the event  # noqa: E501

        :param time: The time of this Cluster.  # noqa: E501
        :type time: datetime
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Cluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cluster):
            return True

        return self.to_dict() != other.to_dict()
