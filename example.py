#!/usr/bin/env python
from decouple import config
import simple_stripe_client

print(config('STRIPE_SECRET_KEY'))

stripe_api = simple_stripe_client.Api(config('STRIPE_SECRET_KEY'), debug_http=True)

# print(stripe_api.charges.get)
print(stripe_api.charges.get())
# data = stripe_api.charges.get()
print("\n\n\n")
# print(data)
