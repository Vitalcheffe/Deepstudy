# Dans utils/stripe.py
import stripe

stripe.api_key = "votre-clé-stripe"

def create_customer(email: str):
    return stripe.Customer.create(email=email)

def create_subscription(customer_id: str, plan_id: str):
    return stripe.Subscription.create(
        customer=customer_id,
        items=[{"plan": plan_id}],
    )