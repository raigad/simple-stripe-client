# simple-stripe-client
A simple lightweight api client for awesome stripe


Quick Usage
-----------

```python
import simple_stripe_client

# blocking client
stripe_api = simple_stripe_client.Api('api_key', debug_http=True)

DUMMY_PLAN = {
    'amount': 200,
    'interval': 'month',
    'name': 'Amazing Stripe test Basic Plan',
    'currency': 'gbp',
    'id': 'stripe-test-plan-basic'
}

# Creating Stripe plan
stripe_api.plans.post(**DUMMY_PLAN)

# Fetching Stripe plan
plan = stripe_api.plans.id(DUMMY_PLAN['id']).get()

```
