import connexion
import six

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_prices import CustomerPrices  # noqa: E501
from swagger_server import util


def create_customer(body):  # noqa: E501
    """Create customer

    This can only be done by the logged in customer. # noqa: E501

    :param body: Created customer object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_customer_prices_by_packaging_id(customerId, widgetPackagingId, price):  # noqa: E501
    """Create customer costs

    customer costs # noqa: E501

    :param customerId: ID of supplier to add a cost for
    :type customerId: int
    :param widgetPackagingId: ID of packaging widget to add a cost for
    :type widgetPackagingId: int
    :param price: price
    :type price: 

    :rtype: CustomerPrices
    """
    return 'do some magic!'


def delete_customer(customername):  # noqa: E501
    """Delete customer

    This can only be done by the logged in customer. # noqa: E501

    :param customername: The name that needs to be deleted
    :type customername: str

    :rtype: None
    """
    return 'do some magic!'


def get_customer_by_name(customername):  # noqa: E501
    """Get customer by customer name

     # noqa: E501

    :param customername: The name that needs to be fetched. Use customer1 for testing.
    :type customername: str

    :rtype: Customer
    """
    return 'do some magic!'


def get_customer_prices_by_packaging_id(customerId, widgetPackagingId):  # noqa: E501
    """Get customer costs

     # noqa: E501

    :param customerId: ID of supplier to add a cost for
    :type customerId: int
    :param widgetPackagingId: ID of packaging widget to add a cost for
    :type widgetPackagingId: int

    :rtype: CustomerPrices
    """
    return 'do some magic!'


def update_customer(customername, body):  # noqa: E501
    """Updated customer

    This can only be done by the logged in customer. # noqa: E501

    :param customername: name that need to be updated
    :type customername: str
    :param body: Updated customer object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Customer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
