import connexion
import six

from swagger_server.models.supplier import Supplier  # noqa: E501
from swagger_server.models.supplier_costs import SupplierCosts  # noqa: E501
from swagger_server import util


def create_supplier(body):  # noqa: E501
    """Create supplier

    This can only be done by the logged in supplier. # noqa: E501

    :param body: Created supplier object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Supplier.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_supplier_costs(supplierId, widgetId, warehouse, quantity, min_quantity, cost):  # noqa: E501
    """Create supplier cost by widget id

    This can only be done by the logged in supplier. # noqa: E501

    :param supplierId: ID of supplier to add a cost for
    :type supplierId: int
    :param widgetId: ID of widget to add a cost for
    :type widgetId: int
    :param warehouse: warehouse code
    :type warehouse: str
    :param quantity: quantity
    :type quantity: 
    :param min_quantity: min_quantity
    :type min_quantity: 
    :param cost: cost
    :type cost: 

    :rtype: SupplierCosts
    """
    return 'do some magic!'


def delete_supplier(supplierId):  # noqa: E501
    """Delete supplier

    Delete # noqa: E501

    :param supplierId: The id that needs to be deleted
    :type supplierId: str

    :rtype: None
    """
    return 'do some magic!'


def get_supplier_by_id(supplierId):  # noqa: E501
    """Get supplier by supplier ID

     # noqa: E501

    :param supplierId: The id that needs to be fetched. Use supplier1 for testing.
    :type supplierId: 

    :rtype: Supplier
    """
    return 'do some magic!'


def get_supplier_costs_by_id(widgetId, supplierId):  # noqa: E501
    """Get supplier costs by supplier ID

     # noqa: E501

    :param widgetId: ID of widget to add a cost for
    :type widgetId: int
    :param supplierId: The id that needs to be fetched. Use supplier1 for testing.
    :type supplierId: 

    :rtype: SupplierCosts
    """
    return 'do some magic!'


def get_suppliers():  # noqa: E501
    """Get suppliers

     # noqa: E501


    :rtype: Supplier
    """
    return 'do some magic!'


def update_supplier(supplierId):  # noqa: E501
    """Updated supplier

    Update a supplier # noqa: E501

    :param supplierId: The id that needs to be fetched. Use supplier1 for testing.
    :type supplierId: 

    :rtype: None
    """
    return 'do some magic!'
