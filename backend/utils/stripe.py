import os
import stripe

stripe.api_key = os.getenv("STRIPE_API_KEY", "")

def create_customer(email: str):
    if not stripe.api_key:
        raise ValueError("STRIPE_API_KEY not set")
    return stripe.Customer.create(email=email)

def create_subscription(customer_id: str, plan_id: str):
    if not stripe.api_key:
        raise ValueError("STRIPE_API_KEY not set")
    return stripe.Subscription.create(
        customer=customer_id,
        items=[{"plan": plan_id}],
    )
