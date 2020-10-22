$(document).ready(function(){
    $("#form-user").submit(function(event){
        event.preventDefault();
        if(validate()){
            var userInput = $("#input-zipcode").val();
            $("li#zipcode").text(userInput);
            $("ul#cities").empty();
            search(userInput);
        }
    })
});
const validate = function(event){
    var userInput = $("#input-zipcode").val();
    if (userInput.match('^[1-9]{1}[0-9]{3}$')){
        return true;
    }
    else{
        var errorMessage = "<li>Invalid Zip Code! Try number between 1000 and 9999</li>";
        $("ul#error-message").append(errorMessage);
        return false;
    }
}
function search(input){
    dataURL = 'https://raw.githubusercontent.com/jief/zipcode-belgium/master/zipcode-belgium.json';
    var dataRequest = new XMLHttpRequest();
    dataRequest.open('GET', dataURL);
    dataRequest.onload = function(){
        var data = JSON.parse(dataRequest.responseText);
        data.forEach(element => {
            if (input == element.zip){
                let match = element.city;
                addToList(match);
            } 
        });
    };
    dataRequest.send(); 
}

function addToList(city){
    var newCity = '<li>' + city + '</li>';
    $("ul#cities").append(newCity);
}