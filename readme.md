# cuppa


## Overview

A tool aimed at making administration tasks relating to uploading and downloading files from servers quicker
and encourage us to use best practice by automating it. We tend to do the tasks covered by these commands 
relatively frequently and as a result spend a large amount of time. 

The push/pull functionality is taken from git (which we use). As a result the concepts should be very quick to grasp.

It can be used on the desktop but also a tool used in the gitlab pipelines. Windows 10 and Ubuntu 18.04+ 
are supported.

It's also something which we should integrate with our pipeline system to allow for database uploads
when the database is committed to the repository.

In an ideal case, the push functionality would never be used locally. This instead would be used in
the pipeline script. However, until all sites use the pipeline system (which seems unrealistic) the
push commands can be used locally.

So for instance the cuppa push db.. command would be ran when the database is committed and merged to the
'database' branch which triggers the overwriting of the database on the remote server.

'Remote' refers to live/staging depending on context.

Why's it called cuppa? These tasks can be long  (usually 1 - 10 min), so it reminds you to go get a 
cup of tea once it starts running!

## Quickstart

TODO

Python 3.8+ is required along with pipenv.

    pipenv install
    pipenv shell

Create a distributed exe file:

    cd cuppa
    pyinstaller cuppa.py --onefile

## Testing

This project uses TDD practices so whenever new functionality is developed, a test
case should be added or the existing one amended first.

Please note that all references to username and password are ssh details.

## Functionality

All commands need to be ran in the root of the project so make sure that your current directory
is the project of interest.

### Bundle up a full project

This bundles up a site in a zip file and includes both the database and files.
This is good to use if someone asks for a full backup of the site. It returns a
link on the server to the full backup of the site. This means the person requesting
the backup can be just given the link.

    cuppa bundle full example.com --username test --password pass123

### Bundle up a database and save it

This exports the local database from the mysql server and saves it to the SQL folder. Great
if you want to just commit the database or merge the database to the 'database' branch and have it 
push to the preview.

    cuppa bundle db

### Pull database

This pulls the database from a server and replaces the existing one locally in both
the SQL file on the repository and the mysql server. 
Good to use if you would like to use a remote database.

    cuppa pull db example.com --username test --password pass123

### Push database

If you want to overwrite a remote database with the one on your local machine.

    cuppa push db example.com --username test --password pass123

### Pull files

This is if you are starting work and want to get your local copy to to match the remote site.

    cuppa pull files example.com --username test --password pass123

### Push files

This is if you have finished working locally and want to update the remote site.

    cuppa push files example.com --username test --password pass123

## Use case examples

### Sharing development and content work

NB has worked on a site and has got as far along as he can. TM has content and would like to add
it to the remote site.

NB runs:

    cuppa push db example.com --username test --password pass123
    cuppa push files example.com --username test --password pass123    

This pushes all his work to the remote server and means that TM is working on the most up to date
database and files.

A few days later TM has completed adding content. NB is ready to work on the site again. NB
explains to TM that he is going to work on the site again and to hold off on modifying the remote
site for the time being.

NB runs 

    cuppa pull db example.com --username test --password pass123
    cuppa pull files example.com --username test --password pass123    

He has pulled all the changes from the remote server, and set up the database
locally and continues developing.

### A customer wants a full backup of their site.

RS runs the following command with the customers server details:

    cuppa bundle example.com --username test --password pass123

This returns a url with the backup:
    
    https://example.com/full-backup-23094sdjfkj345h3kj5.zip

RS sends this to the customer which they use to download the full site.

### Customer gets in touch wanting some work on an existing site.

Customer has got in touch and wants some work done on their existing site. NB
checks out the repository for the project and then runs the following two commands

    cuppa pull db example.com --username test --password pass123
    cuppa pull files example.com --username test --password pass123

This pulls all the latest files from the remote server. NB then commits these changes to the repository
and is ready to start.


### Updating the databse through the pipeline

RS has finished working locally and is ready to overwrite the remote databse. He runs:

    cuppa bundle db

Commits the work and then merges the changes to 'database' and 'staging' which triggers the update
of the files and database on the remote server.

