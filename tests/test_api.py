import unittest
import os
import simple_stripe_client

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')


class BuildURLTest(unittest.TestCase):
    def setUp(self):
        self.stripe = simple_stripe_client.Api(STRIPE_SECRET_KEY)
        self.resources = ['balance', 'customers', 'charges', 'invoices']
        self.CHARGE_ID = 'ch_123'

    def test_urls(self):
        for resource in self.resources:
            expected_url = "/{url}".format(url=resource)
            getattr(self.stripe, resource)
            print("expected_url=" + expected_url + ",actual_url=" + self.stripe.url)
            self.assertEqual(self.stripe.url, expected_url)
            self.stripe.get_and_reset_url()

    def test_urls_with_id(self):
        for resource in self.resources:
            id = resource[:2] + '_id'
            expected_url = "/{url}/{id}".format(url=resource, id=id)
            getattr(self.stripe, resource)
            self.stripe.id(id)
            self.assertEqual(self.stripe.url, expected_url)
            self.stripe.get_and_reset_url()
