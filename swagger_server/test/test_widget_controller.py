# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer_prices import CustomerPrices  # noqa: E501
from swagger_server.models.supplier_costs import SupplierCosts  # noqa: E501
from swagger_server.models.widget import Widget  # noqa: E501
from swagger_server.models.widget_packaging import WidgetPackaging  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWidgetController(BaseTestCase):
    """WidgetController integration test stubs"""

    def test_add_widget(self):
        """Test case for add_widget

        Add a widget
        """
        body = Widget()
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_widget_packaging(self):
        """Test case for create_widget_packaging

        Creates a packaging for a widget
        """
        data = dict(desc='desc_example',
                    container='container_example',
                    quantity='quantity_example')
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}/packaging'.format(widgetId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_widget(self):
        """Test case for delete_widget

        Deletes a widget
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}'.format(widgetId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_widget_by_id(self):
        """Test case for get_widget_by_id

        Find widget by ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}'.format(widgetId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_widget_costs_by_id(self):
        """Test case for get_widget_costs_by_id

        Get widget costs by ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}/costs'.format(widgetId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_widget_packaging_by_id(self):
        """Test case for get_widget_packaging_by_id

        Get widget packagings by ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}/packaging'.format(widgetId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_widget_packagings_by_id(self):
        """Test case for get_widget_packagings_by_id

        Get widget packagings by ID and packaging ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}/packaging/{packagingId}'.format(widgetId=789, packagingId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_widget_packagings_prices_by_id(self):
        """Test case for get_widget_packagings_prices_by_id

        Get widget prices for customers by ID and packaging ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}/packaging/{packagingId}/prices'.format(widgetId=789, packagingId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_widgets(self):
        """Test case for get_widgets

        Get widgets
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_widget_with_form(self):
        """Test case for update_widget_with_form

        Updates a widget in the store with form data
        """
        data = dict(name='name_example')
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/widget/{widgetId}'.format(widgetId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
