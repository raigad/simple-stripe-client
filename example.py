#!/usr/bin/env python
from decouple import config
import simple_stripe_client

# print()

STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')

stripe_api = simple_stripe_client.Api(STRIPE_SECRET_KEY, debug_http=False)

print("\n\n\n")
# print(stripe_api.charges.get)

# data = stripe_api.charges.get(limit=1)
data = stripe_api.charges.id('ch_1Dz60xJKzeKazErxinipPnZa').get()
print("\n\n\n")
print(data)
print("\n\n\n")
print(data['metadata'])

##Create new charge
# CHARGE_DATA = {
#     'amount': 2100,
#     'currency': 'gbp',
#     'source': 'tok_amex',
#     'metadata': {
#         'first_name' : 'rohit',
#         'meta_1' : 123,
#     }
# }
#
# charge = stripe_api.charges.post(**CHARGE_DATA)
# print(charge)


# charge_id = 'ch_1A9W9lJKzeKazErx0YGhbt0l'
# result = stripe_api.charges.id(charge_id).get()
# print(result)
