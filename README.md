**Introduction** 
Newsdata.py creates three reports about news website.
First report is the three most popular articles.
Second report is most popular authors in order of thier popularity.
Third report is dates when more that 1% of the web requests failed.



**Execution from VM Command Line:**
python3 newsdata.py
(ensure that news database has been updated with the new view)


**Input parameters for execution:**
None


**View Created:** sim_articles

**SQL query for creating the view:** 
create view sim_articles as select articles.id, authors.name as author, 
articles.title, '/article/'||articles.slug as path from articles join authors
on authors.id=articles.author;

