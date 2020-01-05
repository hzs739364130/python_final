# coding: utf-8
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Feile(db.Model):
    __tablename__ = 'feile'

    name = db.Column(db.String(255, 'utf8mb4_unicode_ci'))
    f_2002 = db.Column('f_2002', db.String(255, 'utf8mb4_unicode_ci'))
    f_2007 = db.Column('f_2007', db.String(255, 'utf8mb4_unicode_ci'))
    f_2012 = db.Column('f_2012', db.String(255, 'utf8mb4_unicode_ci'))
    f_2017 = db.Column('f_2017', db.String(255, 'utf8mb4_unicode_ci'))
    type = db.Column(db.Integer)  # 1gdp，2难民数， 3旅游， 4移民数据
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return 'role:%s' % self.name

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
