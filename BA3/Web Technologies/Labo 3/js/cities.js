$(document).ready(function(){
    $("#form-user").submit(function(event){
        event.preventDefault();
        if(validate()){
            var userInput = $("#input-zipcode").val();
            $("li#zipcode").text(userInput);
            $("ul#cities").empty();
            //search(userInput);
            loadJSON(userInput);
        }
    })
});
const validate = function(event){
    var userInput = $("#input-zipcode").val();
    if (userInput.match('^[1-9]{1}[0-9]{3}$')){
        return true;
    }
    else{
        $("ul#error-message").empty();
        var errorMessage = "<li>Invalid Zip Code Input! Try number between 1000 and 9992</li>";
        $("ul#error-message").append(errorMessage);
        return false;
    }
}
function loadJSON(input) {
    dataURL = 'https://raw.githubusercontent.com/jief/zipcode-belgium/master/zipcode-belgium.json';
    var dataRequest = new XMLHttpRequest();
    dataRequest.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) { 
            //readyState 4: request finished and response is ready
            //status 200: OK
            var statusMessage = "<li>Ready</li>";
            $("ul#error-message").empty();
            $("ul#error-message").append(statusMessage);
            search(this, input);
        }
    };
    dataRequest.open("GET", dataURL, true);
    dataRequest.send();
  }
function search(dataRequest, input){
    var data = JSON.parse(dataRequest.responseText);
    var count = 0;
    data.forEach(element => {
        if (input == element.zip){
            count ++;
            let match = element.city;
            addToList(match);
        } 
    });
    if (count == 0){
        var errorMessage = "<li>0 city found</li>";
        $("ul#error-message").append(errorMessage);
    }
    else{
        var errorMessage = "<li>" + count + " city(ies) found(s)</li>";
        $("ul#error-message").append(errorMessage);
     }
  }
function addToList(city){
    var newCity = '<li>' + city + '</li>';
    $("ul#cities").append(newCity);
}