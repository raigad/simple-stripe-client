import unittest
import os
import simple_stripe_client

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY','')

class BuildURLTest(unittest.TestCase):
    def setUp(self):
        self.stripe = simple_stripe_client.Api(STRIPE_SECRET_KEY)

    def test_urls(self):
        self.assertEqual(self.stripe.charges.url,'/v1/chargesss')
