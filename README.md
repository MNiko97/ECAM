# TODO
## In Code Issues
- AddPart.cs:
Issue #1: fix the minimum quantity. Should be provided so we can later add the write amount when building bike
(Exemple: minimum quantity for wheel is 2 in a bike)
- Order.cs:
Issue #2: comment says "NOT READY YET", investigate
- InternalApp.cs:
Issue #3: we discussed a solution for the password. 
Issue #4: there is two part constructors. One constructor is used to research part but have 0 references. 
We already dissusced about that but there has to be a better solution. Same remark for client search

## GUI Issues
### "Manager" View:
- Fix issue that redirects user to the password form and not the main menu when quitting manager window. The password still remains in the text field. 
This happen when we input "enter" on the keyboard after typing password and not using the confirm button to log on
- Rename tables columns names in "All Bikes" and "Supplier orders" tab
- Fix convention for naming different tabs
- Add button "Back" in every tab to allowing to exit manager view
- Add tab "tabPage4" content
- Remove tab "Planning" and find an alternative way allowing the manager to go into the planning view
- Rename window from "Manager_menus" to "Menu" or "Manager"

### "Add to production" View: 
- Add message to tell us what is happening when adding bike to production if the form is incomplete
- Rename button "Save" to "Add" as we are adding bikes and not saving them
- Add button "Back"

### "Planning" View: 
- Add message to indicate if the procedure was successfull or not when using AutoPlanner
- Rename window from "Manager" to "Planning"
- Rename days in English
- Shorten button "Add bike for production to stock" to "Update Stock" or similar

### "Fitter" View:
- Allow the fitter to view next days (maybe previous also). We discussed this in the past but it could be a good idea
- Remove the "!" on the refresh button text

### "Broken Part" View:
- Fix the part search. It does not work correctly, the full reference need to be written. 
When selecting a part and clicking the "Validate" button, there is an error message "Error, try again". Check Issue #4 for more info
- Rename label "Search part" by "Search part reference" if we only allow to search parts through reference
- Rename columns according to convention
- Rename button "Validate" to "Report"
- Rename label "Broken part :" to "Selected Part:". Maybe remove completely this label and its content

## General Remarks

- Fix a convention for all the labels, tabs, columns names and eventual error messages for the entire application.  Could be different conventions regarding if it is a label or a window name ... but we need to fix those conventions

    Exemple 1: every word starting with a capital letter -> _This is a label convention_
    
    Example 2: only first word starting with a capital letter -> _This Is A Button Convention_

- Remove all obsolete GetDatable and other SQL Methods inside other class. Instead use the public method from InternalApp.cs

## Minor Issues:
- Inside Planning.cs, try to use InternalApp database access methods on VerifyDate, BikeByDay, GetDataTable (redondant name) and UpdateMaker methods
- Inside Order.cs, try to use Bovelo database access methods on Save method
- Inside Client.cs, try to use Bovelo database access methods on Save method
- Inside BuyableItem.cs, try to use Bovelo database access methods on Save method
- As Order.cs, Client.cs and BuyableItem.cs are part of bovelo app, we need to add the same database methods from InternalApp.cs to Bovelo.cs
