# cuppa


## Overview

A tool aimed at making adminstration tasks quicker and encourage us to use best practice by automating it.
The push/pull functionality is taken from git (which we use) so the concepts should be very quick to grasp.

It can be used on the desktop but also a tool used in the gitlab pipelines. Windows 10 and Ubuntu 18.04+ 
are supported.

Why's it called cuppa? These tasks can be long  (usually 3 - 10 min), so it reminds you to go get a 
cup of tea once it starts running!

## Quickstart

TODO

Please note that all references to username and password are ssh details.

## Functionality

### Bundle up a project

This bundles up a site in a zip file and includes both the database and files.
This is good to use if someone asks for a full backup of the site. It returns a
link on the server to the full backup of the site. This means the person requesting
the backup can be just given the link.

    cuppa bundle example.com --username test --password pass123

### Pull database

This pulls the database from a server and replaces the existing one locally.
Good to use if you would like to use a staging database.

    cuppa pull db example.com --username test --password pass123

### Push database

If you want to overwrite a remote database with the one on your local machine.

    cuppa push db example.com --username test --password pass123

### Pull files

    cuppa pull files example.com --username test --password pass123

### Push files
This is if you are starting work and want to get the repo to match the live site.

    cuppa push files example.com --username test --password pass123


## Use case examples

