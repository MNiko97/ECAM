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
        console.log(this.firstname + " " + this.name);
    }
}

function showMenu(){
    console.log("1 : Show Contact List");
    console.log("2 : Add New Contact");
    console.log("0 : Quit");
}

function main(){
    let myContactList = new ContactList;
    myContactList.addNewContact("Carole", "Lévisse");
    myContactList.addNewContact("Mélodie", "Nelsonne");
    console.log("Welcome !")
    while(running){
        showMenu();
        const input = prompt();
        switch (input){
            case "1":
                myContactList.showAllContacts();
                break;
            case "2":
                console.log("New contact: ");
                console.log("Write name: ");
                const name = prompt();
                console.log("Write Firstname : ");
                const firstname = prompt();
                myContactList.addNewContact([name, firstname]);
                console.log("Contact sucessfully added!")
                myContactList.showAllContacts();
                break;
            case "0":
                running = False;
                break;
        }
    }
}

