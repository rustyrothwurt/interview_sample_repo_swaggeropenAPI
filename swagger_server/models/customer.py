# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Customer(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None):  # noqa: E501
        """Customer - a model defined in Swagger

        :param id: The id of this Customer.  # noqa: E501
        :type id: int
        :param name: The name of this Customer.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Customer':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Customer of this Customer.  # noqa: E501
        :rtype: Customer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Customer.


        :param id: The id of this Customer.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Customer.


        :return: The name of this Customer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Customer.


        :param name: The name of this Customer.
        :type name: str
        """

        self._name = name