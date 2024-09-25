## With Flask or Django

- https://testdriven.io/blog/flask-stripe-tutorial/
- https://www.youtube.com/watch?v=cC9jK3WntR8
- https://www.youtube.com/watch?v=g96MJj2pPg8

## Horror stories

- [My Stripe Tax Story](https://gist.github.com/humandoing/5ec7c224691282532db0b9dc37797d7c)

## Usage scenario: SEPA Direct Debit payments in Flask

References: 
- https://docs.stripe.com/payments/sepa-debit

Here are the steps (planning, configuration and integration) needed to implement SEPA Direct Debit payments in a Python/Flask web application using Stripe:

### Enable SEPA Direct Debit in Stripe Dashboard:

- Log in to your Stripe account.
- Navigate to the **Payment Methods** settings.
- Enable SEPA Direct Debit.
- Complete any additional identity verification steps as prompted.

### Collect Customer Information and Authorization:

- During checkout, collect the customer's full name and IBAN.
- Present a mandate authorization to the customer, which gives you permission to debit their account. Stripe can generate this mandate for you.

### Integrate Stripe's Front-End Components:

- Use Stripe's prebuilt UI components like **Stripe Checkout** or **Stripe Elements** to handle the front-end payment flow.
    - **Stripe Checkout**: A hosted payment page that you can redirect customers to.
    - **Stripe Elements**: Prebuilt UI components you can embed in your application.
- These tools will handle collecting the IBAN and mandate authorization seamlessly.

### Implement Server-Side Logic with Flask:

- Install the Stripe Python SDK: `pip install stripe`
- Configure your Flask application to create a PaymentIntent with SEPA Direct Debit as the payment method.

```python
import stripe

stripe.api_key = 'your_secret_key'

@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
     data = json.loads(request.data)
     intent = stripe.PaymentIntent.create(
         amount=data['amount'],
         currency='eur',
         payment_method_types=['sepa_debit'],
         confirm=True,
         payment_method_data={
             'type': 'sepa_debit',
             'sepa_debit': {
                 'iban': data['iban'],
             },
             'billing_details': {
                 'name': data['name'],
             },
         },
         mandate_data={
             'customer_acceptance': {
                 'type': 'online',
                 'online': {
                     'ip_address': request.remote_addr,
                     'user_agent': request.headers.get('User-Agent'),
                 },
             },
         },
     )
     return jsonify({'client_secret': intent.client_secret})
```

### Handle Webhooks for Asynchronous Events:

- Set up webhook endpoints in your Flask application to listen for Stripe events like `payment_intent.succeeded`, `payment_intent.payment_failed`, and `charge.dispute.created`.
- Use these webhooks to update your application's order status and handle failures or disputes.

```python
@app.route('/webhook', methods=['POST'])
def stripe_webhook():
     payload = request.data
     sig_header = request.headers.get('Stripe-Signature')
     event = None
    
     try:
         event = stripe.Webhook.construct_event(
             payload, sig_header, 'your_webhook_secret'
         )
     except ValueError:
         # Invalid payload
         return '', 400
     except stripe.error.SignatureVerificationError:
         # Invalid signature
         return '', 400
    
     # Handle the event
     if event['type'] == 'payment_intent.succeeded':
         payment_intent = event['data']['object']
         # Fulfill the purchase, e.g., update order status
     elif event['type'] == 'payment_intent.payment_failed':
         payment_intent = event['data']['object']
         # Notify the customer that payment failed
     # ... handle other event types
 return '', 200
```

### Configure Debit Notification Emails:

- By default, Stripe sends debit notification emails to customers.
- If you prefer to send custom emails:
 - Turn off Stripe emails in the Dashboard under Email settings.
 - Use the `payment_intent.processing` event to trigger your custom email.
 - Ensure your email includes all required information:
   - Last 4 digits of the debtor’s bank account
   - Mandate reference
   - Amount to be debited
   - Your SEPA Creditor Identifier
   - Your contact information

### Caveats

1. **Consider Creditor Identifier (Creditor ID):**

    - By default, Stripe uses its own Creditor ID.
    - If you're based in the EU, it's recommended to obtain and use your own Creditor ID for better customer recognition and reduced dispute rates.
    - Configure your Creditor ID in the Payment Method Settings on the Stripe Dashboard.

2. **Handle Payment Failures and Disputes:**

    - Implement logic to manage failed payments based on the failure codes provided by Stripe.
    - Understand that SEPA Direct Debit disputes are final and cannot be appealed.
    - Monitor for `charge.dispute.created` webhook events to handle disputes appropriately.

3. **Manage Refunds Carefully:**

    - Refunds must be issued within 180 days of the original payment.
    - Be cautious, as customers can still dispute a payment even after a refund.
    - Communicate with your customers when issuing refunds to avoid confusion.

4. **Be Aware of Processing Times and Limits:**

    - SEPA Direct Debit payments can take up to 14 business days to be confirmed, though it usually takes 7-8 days.
    - There's a per-transaction limit of 10,000 EUR and a weekly limit for new users.
    - Payouts for SEPA transactions are subject to a 5-business-day timing until you reach a certain processing volume.

### Key Considerations:

- **Compliance:** Ensure you're compliant with SEPA regulations, especially regarding mandate acceptance and customer notifications.
- **Security:** Handle customer data securely and in accordance with GDPR and other data protection laws.
- **Testing:** Use Stripe's test environment to simulate SEPA Direct Debit payments before going live.
- **Customer Experience:** Use clear statement descriptors and consider using your own Creditor ID for better recognition.

### Resources:

- **Stripe SEPA Direct Debit Quickstart Guides:**
      - [Checkout Quickstart](https://stripe.com/docs/payments/checkout)
      - [Elements Quickstart](https://stripe.com/docs/payments/elements)
- **Stripe API Reference:**
      - [PaymentIntents](https://stripe.com/docs/api/payment_intents)
      - [Webhooks](https://stripe.com/docs/webhooks)
- **Flask Integration Example:**
      - [Stripe's Flask Sample Application](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow/server/python)
