#!/usr/bin/env python

import simple_stripe_client


stripe_api = simple_stripe_client.Api(debug_http=True)

stripe_api.get_charge()
