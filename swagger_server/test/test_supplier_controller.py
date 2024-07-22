# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.supplier import Supplier  # noqa: E501
from swagger_server.models.supplier_costs import SupplierCosts  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSupplierController(BaseTestCase):
    """SupplierController integration test stubs"""

    def test_create_supplier(self):
        """Test case for create_supplier

        Create supplier
        """
        body = Supplier()
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_supplier_costs(self):
        """Test case for create_supplier_costs

        Create supplier cost by widget id
        """
        data = dict(warehouse='warehouse_example',
                    quantity=8.14,
                    min_quantity=8.14,
                    cost=8.14)
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier/{supplierId}/costs/{widgetId}'.format(supplierId=789, widgetId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_supplier(self):
        """Test case for delete_supplier

        Delete supplier
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier/{supplierId}'.format(supplierId='supplierId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_supplier_by_id(self):
        """Test case for get_supplier_by_id

        Get supplier by supplier ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier/{supplierId}'.format(supplierId=8.14),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_supplier_costs_by_id(self):
        """Test case for get_supplier_costs_by_id

        Get supplier costs by supplier ID
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier/{supplierId}/costs/{widgetId}'.format(widgetId=789, supplierId=8.14),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_suppliers(self):
        """Test case for get_suppliers

        Get suppliers
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_supplier(self):
        """Test case for update_supplier

        Updated supplier
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/supplier/{supplierId}'.format(supplierId=8.14),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
