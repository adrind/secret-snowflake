# Secret-snowflake #

A quick script for hassle free gift swap planning. 
Wrote this in half an hour on Thanksgiving while trying to plan a holiday gift swap among 10 people. 
This seemed like the most painless solution...

The script simply matches up people (making sure not to assign someone herself), e-mails everyone who they're assigned,
and saves a file for each match locally in a provided directory. It's something I threw together really quickly but I know some people 
were interested so I thought I'd post now while the holiday gift swap season is about to start!  

Run
----------
First: edit the code to include your e-mail address and password.  Note that it's configured to work with only g-mail 
sender addresses so if you're sending from a different domain make sure to edit the server stuff. I'll probably work on
this when I'm bored soon and make it so you don't have to hardcode your e-mail info. 

As of now it just takes 2 arguments: a list of names/e-mails of the participants and a directory path where you want 
the files stored. 

__python secretsnowflake.py [list-of-names] [dir-path]__

list-of-names should be formatted as: Name E-mail, Name2 E-mail2, Name3 E-mail3, Name4 E-mail4, ..... , NameN E-mailN

So name followed by one whitespace char followed by e-mail ended with a comma. 

Thanks! 