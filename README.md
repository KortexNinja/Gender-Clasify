# Gender-Clasify
Using Naive Bayes classifier and using @jcharis work I put it all in one script just to make it user friendlier. It ask for an excel sheet with the names and it produces a new one with the genders. This was useful to me at work where we have a bunch of data collected and they made me assign gender for every person based only on the name. I decided to make this, I hope this is useful to somebody else.

## Note/instructions:
The script will look for a column name named "nombre" since I made it to work for a spanish speaking office. You can modify the code to look for "name" easily.

nombres.xlsx is the file with all the names for the model to train.

After it trains, you will be asked for the name of the file that you want to clasify. All names must be in one column.
