# simple-stripe-client
A simple lightweight api client for awesome stripe.

# Example

```python
import simple_stripe_client
import os
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
# create client
stripe_api = simple_stripe_client.Api(STRIPE_SECRET_KEY, debug_http=True)


CHARGE_DATA = {
    'amount': 15921,
    'currency': 'gbp',
    'capture' : False,
    'source': 'tok_amex',
    'metadata': {
        'first_name' : 'Sachin',
        'last_name'  : 'Tendulkar',
    } 
}

# Creating Charge
charge = stripe_api.charges.post(**CHARGE_DATA)

CHARGE_ID = 'ch_xxx'
# Fetching Charge
charge = stripe_api.charges.id(CHARGE_ID).get()

# Update Charge
charge = stripe_api.charges.id(CHARGE_ID).post(description='Test Update')

# Capture Charge
charge = stripe_api.charges.id(CHARGE_ID).capture.post(amount=12000)


```

# Building Stripe's Curl URLs


URLs would match one-to-one to stripe's curl api urls.
For more links please refer to [stripe doc](https://stripe.com/docs/api?lang=curl)

```

stripe_api.charges                                  # == /v1/charges
stripe_api.charges.id(CHARGE_ID)                    # == /v1/charges/{CHARGE_ID}    

stripe_api.customers                                # == /v1/customers
stripe_api.customers.id(CUSTOMER_ID)                # == /v1/customers/{CUSTOMER_ID}

stripe_api.invoices                                 # == /v1/invoices
stripe_api.invoices.id(INVOICE_ID)                  # == /v1/invoices/{INVOICE_ID}

```

# Changelog -

# 0.0.1 (01-02-2019)
 * initial release
