#!/usr/bin/env python
from decouple import config
import simple_stripe_client

# print()

STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')

stripe_api = simple_stripe_client.Api(STRIPE_SECRET_KEY, debug_http=True)

CUSTOMER_DATA = {

}

# create customer
# customer = stripe_api.customers.post()

# update customer
customer_id = 'cus_AUVASurSCMYLb7'

# get bank accounts
# accounts = stripe_api.customers.id(customer_id).sources.get(object='bank_account',limit=3)
# accounts = stripe_api.customers.id(customer_id).sources
# print(repr(stripe_api))
# print(accounts)

# customer = stripe_api.customers.id(customer_id).post(description="This is the test customer created",metadata={ 'name' : 'RohitX', 'customer_id' : 123,'last_name':'desf'},email='rohit@example.com')
# print(customer)
#
# DELETE Customer
# customer_del = stripe_api.customers.id(customer_id).delete()
# print("\n\n\n\n")
# print(customer_del)


# print("\n\n\n")
# print(stripe_api.charges.get)
# data = stripe_api.charges.get(limit=1)
# charge_id = 'ch_1Dz60xJKzeKazErxinipPnZa'
# data = stripe_api.charges.id(charge_id).post(description='this is test description x')
# print(data)
# data = stripe_api.charges.id(charge_id).get()
# print("\n\n\n")
# print(data['description'])
# print("\n\n\n")
# print(data['metadata'])

##Create new charge
CHARGE_DATA = {
    'amount': 15921,
    'currency': 'gbp',
    'source': 'tok_amex',
    'capture' : False,
    'metadata': {
        'first_name' : 'rohit',
        'meta_1' : 123,
    }
}
#
charge = stripe_api.charges.post(**CHARGE_DATA)
print(charge)


# charge_id = 'ch_1A9W9lJKzeKazErx0YGhbt0l'
# result = stripe_api.charges.id(charge_id).get()
# print(result)
