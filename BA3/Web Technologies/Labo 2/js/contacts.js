/* 
Activity : Managing Contacts
*/

// Global Variables
var running = true;
var newContactOption = false;

class ContactList{
    constructor(){
        this.contactList = [];
        this.numberOfContacts = 0;
    }
    showAllContacts(){
        if (this.numberOfContacts == 0){
            console.log("You have no contacts registered")
        }
        else{
            console.log("Here are all your contacts:")
            for (let i = 0; i < this.numberOfContacts; i++){
                this.contactList[i].showInfo();
            }
        }
    }
    addNewContact(firstname, name){
        let newContact = new Contact(firstname, name);
        this.contactList.push(newContact);
        this.numberOfContacts += 1;
    }
    showList(){
        console.log(this.contactList);
        for (let i = 0; i < this.numberOfContacts; i++){
            console.log(this.contactList[i]);
        }
    }
}
class Contact{
    constructor(firstname, name){
        this.firstname = firstname;
        this.name = name;
    }
    showInfo(){
        console.log("Name: " + this.name + ", first name: " + this.firstname);
    }
}
function showMenu(){
    console.log("");
    console.log("1 : Show Contact List");
    console.log("2 : Add New Contact");
    console.log("0 : Quit");
    console.log("");
}
const init = function(){
    document.getElementById('button-submit').addEventListener('click', send);
}
const send = function(e){
    e.preventDefault();
    e.stopPropagation();
    let currentOption = validateOption();
    if (currentOption && running && !newContactOption){
        inputOption = document.getElementById("input-option").value;
        if (inputOption == "1"){
            myContactList.showAllContacts();
            document.getElementById("option-info").innerHTML = "Show Contacts";
            showMenu();
        }
        if (inputOption == "2"){
            document.getElementById("option-info").innerHTML = "New Contact";
            document.getElementById("input-name").disabled = false;
            document.getElementById("input-firstname").disabled = false;
            document.getElementById("input-option").disabled = true;
            let firstname = document.getElementById('input-firstname').value;
            let name = document.getElementById('input-name').value;
            let newContact = [];
            if (firstname.match('^[A-Za-z ]+$') && firstname.length != 0){
                newContact.push(firstname);
            }
            if (name.match('^[A-Za-z ]+$') && name.length != 0){
                newContact.push(name);
            }
            if (newContact.length == 2){
                myContactList.addNewContact(firstname, name);
                console.log("New contact successfully added !");
                showMenu();
                document.getElementById("form-user").reset();
                document.getElementById("option-info").innerHTML = "Option";
                document.getElementById("input-name").disabled = true;
                document.getElementById("input-firstname").disabled = true;
                document.getElementById("input-option").disabled = false;
                newContactOption = false;
            }
        }
        if (inputOption == "0"){
            running = false;
            document.getElementById("form-user").style.visibility = "hidden";
            document.getElementById("main-title").innerHTML = "Thank you for using our App!";
            console.log("You quit the contact manager, bye!");          
        }
    }
    else if (!currentOption){
        console.log("Wrong Input!");
        showMenu();
    }
}
const validateOption = function(e){
    let input = document.getElementById("input-option").value;
    if (input.match('^[0-2]{1}$')){
        return true;
    }
    else{
        return false;
    }
}
document.addEventListener("DOMContentLoaded", init);
let myContactList = new ContactList;
myContactList.addNewContact("Carole", "Lévisse");
myContactList.addNewContact("Mélodie", "Nelsonne");
console.log("Welcome to Contact Manager App!");
showMenu()