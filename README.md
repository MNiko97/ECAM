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
We already dissusced about that but there has to be a better solution. Same remark for client search.

## GUI Issues
### "Manager" View:
- Quitting manager window redirect user to the password form not the main menu.
The password still remains in the text field. 
This always happend when we click enter after typing password and not using the confirm button to log on
- Need to rename column name for the datable in "All Bikes", "Supplier orders" tab
- Fix the convention for naming different tabs
- Add back button in every tab to allowing to exit manager view
- Add the "tabPage4" content
- Remove "Planning" tab. Button is useless, find an alternative allowing the manager to go into the planning view.

### "Add to production" View: 
- When adding bike to production, if the form is incomplete, there is no message to tell us what is happening.
- Change the button text "Save" to "Add" as we are adding bikes and not saving them. 
- Add a back button.

### "Planning" View: 
- When using AutoPlanner button there is no message to indicate if the procedure was successfull or not.
- Rename the window name "Manager" to Planning
- Rename all day in English

### "Fitter" View:
- We discussed in this in the past but allowing the fitter to view next days (maybe previous also) could be a good idea
- Searching part does not work correctly, the full reference need to be written.
- If we only allow to search parts through reference, rename label "Search part" by "Search part reference"
- Rename columns name according to convention
- When selecting a part and clicking the validate button, there is an error message "Error,try again".
Check Issue #4 for more info.

## General Remarks

- Fix a convention for all the labels, tabs, columns names and eventual error messages for the entire application.
Exemple 1: every word starting with a capital letter -> This Is A Label Example
Example 2: only first word starting with a capital letter -> Another example
Could be different conventions regarding if it is a label or a window name but we need to fix those conventions.
- Remove all obsolete GetDatable and other SQL Methods inside other class. Instead use the public method from InternalApp.cs

## Minor Issues:
- Inside Planning.cs, try to use InternalApp database access methods on VerifyDate, BikeByDay, GetDataTable (redondant name) and UpdateMaker methods
- Inside Order.cs, try to use Bovelo database access methods on Save method
- Inside Client.cs, try to use Bovelo database access methods on Save method
- Inside BuyableItem.cs, try to use Bovelo database access methods on Save method
- As Order.cs, Client.cs and BuyableItem.cs are part of bovelo app, we need to add the same database methods from InternalApp.cs to Bovelo.cs
