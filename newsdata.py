#!/usr/bin/env python3
#
# Create reports for a news-website

import psycopg2

DBNAME = "news"


def get_report():
    """Most popular articles of all times in order of their popularity."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql_str1 = """select sim_articles.title, count(log.path) as views
    from sim_articles left join log on sim_articles.path=log.path where
    log.status = '200 OK' group by sim_articles.title order
    by views desc limit 3"""
    c.execute(sql_str1)
    print("\r\n The three most popular articles of all times are listed in",
          "order of their popularity \r\n")
    for row in c:
        title = row[0]
        views = row[1]
        print(title, " - ", views, " views \r\n")

    sql_str2 = """select sim_articles.author, count(log.path) as views from
    sim_articles left join log on sim_articles.path=log.path
    where log.status = '200 OK' group by sim_articles.author
    order by views desc"""
    c.execute(sql_str2)
    print("\r\n The most popular authors in order of their popularity \r\n")
    for row in c:
        author = row[0]
        views = row[1]
        print(author, " - ", views, " views \r\n")

    sql_str3 = """select to_char(AllT.view_date,'Month DD,YYYY'), AllT.views,
    ErrorT.error_views, round(100.0 * ErrorT.error_views/AllT.views,2)
    as Perc_errors from (select date(time) as view_date, count(*) as views
    from log group by date(time)) as AllT join (select date(time)
    as view_date, count(*) as error_views from log
    where status='404 NOT FOUND' group by date(time)) as ErrorT
    on AllT.view_date=ErrorT.view_date where
    100.0 * ErrorT.error_views/AllT.views >=1
    order by ErrorT.error_views desc"""
    c.execute(sql_str3)
    print("\r\n Days on which more than 1% requests led to errors \r\n")
    for row in c:
        daten = row[0]
        error = row[3]
        print(daten, " - ", error, "% errors \r\n")

    db.close()

get_report()
