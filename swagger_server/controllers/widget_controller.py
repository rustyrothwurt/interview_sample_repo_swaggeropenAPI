import connexion
import six

from swagger_server.models.customer_prices import CustomerPrices  # noqa: E501
from swagger_server.models.supplier_costs import SupplierCosts  # noqa: E501
from swagger_server.models.widget import Widget  # noqa: E501
from swagger_server.models.widget_packaging import WidgetPackaging  # noqa: E501
from swagger_server import util


def add_widget(body):  # noqa: E501
    """Add a widget

     # noqa: E501

    :param body: Widget object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Widget.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_widget_packaging(widgetId, desc, container, quantity):  # noqa: E501
    """Creates a packaging for a widget

     # noqa: E501

    :param widgetId: ID of widget to add a packaging for
    :type widgetId: int
    :param desc: Packaging description
    :type desc: str
    :param container: Packaging container
    :type container: str
    :param quantity: Packaging description
    :type quantity: str

    :rtype: None
    """
    return 'do some magic!'


def delete_widget(widgetId):  # noqa: E501
    """Deletes a widget

     # noqa: E501

    :param widgetId: widget id to delete
    :type widgetId: int

    :rtype: None
    """
    return 'do some magic!'


def get_widget_by_id(widgetId):  # noqa: E501
    """Find widget by ID

    Returns a single widget # noqa: E501

    :param widgetId: ID of widget to return
    :type widgetId: int

    :rtype: Widget
    """
    return 'do some magic!'


def get_widget_costs_by_id(widgetId):  # noqa: E501
    """Get widget costs by ID

    Returns costs # noqa: E501

    :param widgetId: ID of widget to return
    :type widgetId: int

    :rtype: SupplierCosts
    """
    return 'do some magic!'


def get_widget_packaging_by_id(widgetId):  # noqa: E501
    """Get widget packagings by ID

    Returns packagings # noqa: E501

    :param widgetId: ID of widget to return
    :type widgetId: int

    :rtype: WidgetPackaging
    """
    return 'do some magic!'


def get_widget_packagings_by_id(widgetId, packagingId):  # noqa: E501
    """Get widget packagings by ID and packaging ID

    Returns packagings by ID # noqa: E501

    :param widgetId: ID of widget to return
    :type widgetId: int
    :param packagingId: ID of widget packagings to return
    :type packagingId: int

    :rtype: WidgetPackaging
    """
    return 'do some magic!'


def get_widget_packagings_prices_by_id(widgetId, packagingId):  # noqa: E501
    """Get widget prices for customers by ID and packaging ID

    Returns packagings prices by ID # noqa: E501

    :param widgetId: ID of widget to return
    :type widgetId: int
    :param packagingId: ID of widget packagings to return
    :type packagingId: int

    :rtype: CustomerPrices
    """
    return 'do some magic!'


def get_widgets():  # noqa: E501
    """Get widgets

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_widget_with_form(widgetId, name=None):  # noqa: E501
    """Updates a widget in the store with form data

     # noqa: E501

    :param widgetId: ID of widget that needs to be updated
    :type widgetId: int
    :param name: Updated name of the widget
    :type name: str

    :rtype: None
    """
    return 'do some magic!'
