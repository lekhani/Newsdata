--
-- PostgreSQL View creation for newsdata.py
--

CREATE VIEW view sim_articles as 
select articles.id, authors.name as author, articles.title, 
'/article/'||articles.slug as path 
from articles join authors 
on authors.id=articles.author;
