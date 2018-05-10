function calculate_price(old_score, new_score){
    if (old_score >= new_score) {
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

var id = parseInt(window.location["href"].substr(-2,1)),
    is_custom = false,
    url = 'http://' + location.host + '/packets',
    xmlHttp = new XMLHttpRequest();

xmlHttp.open('GET', url, false);
xmlHttp.send( null );

var textData = xmlHttp.responseText,
    data = JSON.parse(textData);


for (var i=0; i< data.length; i++){
    if (data[i]['pk'] == id){
        if (data[i]["fields"]["type"] == 'C'){
            is_custom = true;
            console.log('is_custom = true');
//            document.getElementById('id_oldScore').oninput = change_price(calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value));
//            document.getElementById('id_newScore').oninput = change_price(calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value));
        }
    }
}

if (is_custom == true){
    document.getElementById('id_oldScore').oninput = function(){ document.getElementById('prod_price').innerHTML = calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value)};
    document.getElementById('id_newScore').oninput = function(){ document.getElementById('prod_price').innerHTML = calculate_price(document.getElementById('id_oldScore').value, document.getElementById('id_newScore').value)};

}
