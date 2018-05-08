paypal.Button.render({

            env: 'sandbox', // sandbox | production

            // PayPal Client IDs - replace with your own
            // Create a PayPal app: https://developer.paypal.com/developer/applications/create
            client: {
                sandbox:    'Aa76bd7adj8uZNnCepaldq0wxLsLub838QwC2AJTPR3JgFvh0hU_wylhGDvInz04sTIiyka-f7F0g3ei',
                production: 'AWIx9vwr9TxI-GIU6rCrREaI0MlCbt919tIuyz6Yki2I4RtNMQMbTSRia7aiaZ-vpAzmiUcuIA8VCrF1'
            },

            // Show the buyer a 'Pay Now' button in the checkout flow
            commit: true,

            style: {
                color: 'gold',
                shape: 'pill',
                size: 'large',
                label: 'buynow'
            },

            // payment() is called when the button is clicked
            payment: function(data, actions) {

                // Make a call to the REST api to create the payment
                return actions.payment.create({
                    payment: {
                        transactions: [
                            {
                                amount: {
                                    total: document.getElementById('prod_price').innerHTML,
                                    currency: 'USD'
                                }
                            }
                        ]
                    }
                });
            },

            // onAuthorize() is called when the buyer approves the payment
            onAuthorize: function(data, actions) {

                // Make a call to the REST api to execute the payment
                return actions.payment.execute().then(function() {
                    document.getElementById("buying_product_form").submit();
                });
            }

}, '#paypal-button-container');
