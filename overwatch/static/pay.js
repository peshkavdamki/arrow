
var id = parseInt(window.location["href"].substr(-2,1)),
    is_custom = false,
    url = 'http://' + location.host + '/packets',
    xmlHttp = new XMLHttpRequest();

xmlHttp.open('GET', url, false);
xmlHttp.send( null );

var textData = xmlHttp.responseText,
    data = JSON.parse(textData);


// Определение цены для Custom

function calculate_price(old_score, new_score){
    old_score = parseFloat(old_score);
    new_score = parseFloat(new_score);
    if (old_score > new_score) {
        return 150;
    }
    else {    
        let price = 0;
        let point = [0, 1500, 2000, 2500, 3000, 3500, 3800, 4000, 4100, 4200, 4300, 4400];
        let coef =  [0, 0.02, 0.03, 0.04, 0.05, 0.09, 0.22, 0.26, 0.5, 0.8, 1.3, 1.7];
        let score = old_score;
        for (var i = 0; i < point.length; i++){
            if (score >= new_score) {
                break;
            }
            else{
                if (score < point[i]) {
                    let diff = 0;
                    if (point[i] < new_score) {
                        diff = point[i] - score;
                    }
                    else {
                        diff = new_score - score;
                    }
                    price += diff*coef[i]
                    if (point[i] < new_score) {
                        score = point[i];
                    }
                    else {
                        score = new_score;
                    }
                }
            }
        }
        price = Math.ceil(price*10)/10;
        return price;
    }
}

// Отображение цены для Custom

for (var i=0; i< data.length; i++){
    if (data[i]['pk'] == id){
        if (data[i]["fields"]["type"] == 'C'){
            is_custom = true;
        }
    }
}

if (is_custom == true){
    document.getElementById('id_oldScore').oninput = function(){ document.getElementById('prod_price').innerHTML = calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value)};
    document.getElementById('id_newScore').oninput = function(){ document.getElementById('prod_price').innerHTML = calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value)};

}

// Определение цены для PayPal

function price_for_paypal(){
    if (is_custom == true) {
        return calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value).toString();
    }
    else {
        for (var i=0; i< data.length; i++){
            if (data[i]['pk'] == id){
                return data[i]["fields"]["price"].toString();
            }
        }
    }
};


// Функция кнопки

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
                                    total: price_for_paypal(),
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
