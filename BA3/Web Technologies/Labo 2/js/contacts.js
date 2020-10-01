/* 
Activity : Managing Contacts
*/

// Global Variables
let running = true;

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
            console.log("Here are all your contacts :")
            for (let i = 0; i < this.numberOfContacts; i++){
                console.log(this.contactList[i].showInfo());
            }
        }
    }
    addNewContact(firstname, name){
        let newContact = new Contact(firstname, name);
        this.contactList.push(newContact);
        this.numberOfContacts += 1;
    }
}

class Contact{
    constructor(firstname, name){
        this.firstname = firstname;
        this.name = name;
    }
    showInfo(){
        console.log(this.firstname + " " + this.name);
    }
}

function showMenu(){
    console.log("1 : Show Contact List");
    console.log("2 : Add New Contact");
    console.log("0 : Quit");
}

function input(){
    document.getElementById("validateButton").addEventListener("click", onClick);
}

function onClick(){
    console.log("you clicked");
}

function main(){
    let myContactList = new ContactList;
    myContactList.addNewContact("Carole", "Lévisse");
    myContactList.addNewContact("Mélodie", "Nelsonne");
    console.log("Welcome !")

    while(running){
        showMenu();
        let input = document.getElementById("textInput").value;
        switch (input){
            case "1":
                myContactList.showAllContacts();
                break;
            case "2":
                let name = document.getElementById("textInput").value;
                let surname = document.getElementById("textInput").value;
                myContactList.addNewContact([name, surname]);
                myContactList.showAllContacts();
                break;
            case "0":
                running = False;
                break;
        }
    }
}

showMenu();
let myContactList = new ContactList;
myContactList.addNewContact("Carole", "Lévisse");
myContactList.addNewContact("Mélodie", "Nelsonne");
console.log(myContactList[0]);
myContactList.showAllContacts;