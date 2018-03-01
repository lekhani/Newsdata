Date : 03/01/2018

**Project Descrption** 
Newsdata.py creates three reports about news website.
First report is the three most popular articles.
Second report is most popular authors in order of thier popularity.
Third report is dates when more that 1% of the web requests failed.

**Dependencies/Pre-requisites**
This program runs on Oracle VM VirtualBox(version 5.1.32) with Vagrant(2.0.2). 
The Virtualbox needs to have Python3 and Postgresql to execute newsdata.py.
It utlizes psycopg2 package for postgresql database connection. 


**Setup/Installation**

$vagrant up  (To start up VM)
$vagrant ssh (To login to VM)
vagrant@vagrant:~$ cd /vagrant (To go the Directory associated with VM)
vagrant@vagrant:/vagrant$ ls   (To make sure this directory has Vagrantfile)
vagrant@vagrant:/vagrant$ psql -d news -f newsdata.sql (To setup news db from downloaded newsdata.sql file)
vagrant@vagrant:/vagrant$ psql -d news -f views.sql  (To create new view required for this program)
 	
**Usage**

**_To view the reports on the shell_**
vagrant@vagrant:~$ python3 newsdata.py


**_To save the reports in a file_**
vagrant@vagrant:~$ python3 newsdata.py >> output.txt
(Above command puts the output in output.txt file in current working directory)

**Known Issues**
None reported.

**Future Plans**
It will have web interface for pulling reports. Also new reports will be added.

**Contribution Guidelines**

If you want to make this project better or see any issues you would like to fix,
feel free to contribute. 

1. Fork the repo on GitHub
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request so that we can review your changes

