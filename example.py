#!/usr/bin/env python
from decouple import config
import simple_stripe_client


print(config('STRIPE_SECRET_KEY'))

stripe_api = simple_stripe_client.Api(debug_http=True)

result = stripe_api.charges

print(result.url)
