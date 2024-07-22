# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.customer import Customer  # noqa: E501
from swagger_server.models.customer_prices import CustomerPrices  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCustomerController(BaseTestCase):
    """CustomerController integration test stubs"""

    def test_create_customer(self):
        """Test case for create_customer

        Create customer
        """
        body = Customer()
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/customer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_customer_prices_by_packaging_id(self):
        """Test case for create_customer_prices_by_packaging_id

        Create customer costs
        """
        data = dict(price=8.14)
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/customer/{customerId}/prices/{widgetPackagingId}'.format(customerId=789, widgetPackagingId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_customer(self):
        """Test case for delete_customer

        Delete customer
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/customer/{customername}'.format(customername='customername_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_by_name(self):
        """Test case for get_customer_by_name

        Get customer by customer name
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/customer/{customername}'.format(customername='customername_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_customer_prices_by_packaging_id(self):
        """Test case for get_customer_prices_by_packaging_id

        Get customer costs
        """
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/customer/{customerId}/prices/{widgetPackagingId}'.format(customerId=789, widgetPackagingId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_customer(self):
        """Test case for update_customer

        Updated customer
        """
        body = Customer()
        response = self.client.open(
            '/rustyrothwurt/WidgetStore/1.0.0/customer/{customername}'.format(customername='customername_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
