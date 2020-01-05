import csv, os
from models import Feile
from app import db

basedir = os.path.abspath(os.path.dirname(__file__))
gdp = basedir + '\\data\\gdp.csv'
with open(gdp, newline='', encoding='UTF-8') as  csvfile:
    rows = csv.reader(csvfile)
    num = 0
    for row in rows:
        if num == 0:
            num += 1
            continue
        sql_data = Feile()
        sql_data.name = row[0]
        sql_data.f_2002 = row[1]
        sql_data.f_2007 = row[2]
        sql_data.f_2012 = row[3]
        sql_data.f_2017 = row[4]
        sql_data.type = 1
        db.session.add(sql_data)
        db.session.commit()
        num += 1

# p = basedir + '\\data\\p.csv'
# with open(p, newline='', encoding='UTF-8') as  csvfile:
#     rows = csv.reader(csvfile)
#     num = 0
#     for row in rows:
#         if num == 0:
#             num += 1
#             continue
#         sql_data = Feile()
#         sql_data.name = row[0]
#         sql_data.f_2002 = row[1]
#         sql_data.f_2007 = row[2]
#         sql_data.f_2012 = row[3]
#         sql_data.f_2017 = row[4]
#         sql_data.type = 2
#         db.session.add(sql_data)
#         db.session.commit()
#         print(','.join(row))
# #
#
# t = basedir + '\\data\\t.csv'
# with open(t, newline='', encoding='UTF-8') as  csvfile:
#     rows = csv.reader(csvfile)
#     num = 0
#     for row in rows:
#         if num == 0:
#             num += 1
#             continue
#         sql_data = Feile()
#         sql_data.name = row[0]
#         sql_data.f_2002 = row[1]
#         sql_data.f_2007 = row[2]
#         sql_data.f_2012 = row[3]
#         sql_data.f_2017 = row[4]
#         sql_data.type = 3
#         db.session.add(sql_data)
#         db.session.commit()
#
# ym = basedir + '\\data\\ym.csv'
# with open(ym, newline='', encoding='UTF-8') as  csvfile:
#     rows = csv.reader(csvfile)
#     num = 0
#     for row in rows:
#         if num == 0:
#             num += 1
#             continue
#         sql_data = Feile()
#         sql_data.name = row[0]
#         sql_data.f_2002 = row[1]
#         sql_data.f_2007 = row[2]
#         sql_data.f_2012 = row[3]
#         sql_data.f_2017 = row[4]
#         sql_data.type = 4
#         db.session.add(sql_data)
#         db.session.commit()
