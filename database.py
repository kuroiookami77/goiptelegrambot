from peewee import *
import pymysql
import content
import datetime

DATABASE_NAME = "main.db"

connection = pymysql.connect(host=content.dbhost,
                             user='root',
                             password=content.dbpass,
                             db='goip',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


db_connection = SqliteDatabase(DATABASE_NAME)


class BaseModel(Model):
    class Meta:
        database = db_connection

class Whitelist(BaseModel):
    phone_number = CharField()
    name = CharField()
    last_name = CharField()

class Sessions(BaseModel):
    user_id = IntegerField()
    phone_number = CharField()

class Simcards(BaseModel):
    simline = CharField()
    simbalance = IntegerField()
    simproject = CharField()

class Transactions(BaseModel):
    id = AutoField()
    summ = IntegerField()
    date = DateField()
    simline = CharField()
    destination = CharField()
    unrealsumm = IntegerField()
    description = CharField()
    project = CharField()

db_connection.create_tables([Sessions, Whitelist, Simcards, Transactions])

class Database:
    def __init__(self):
        pass

    def get_whitelist(self):
        white_list = {}
        db_rows = Whitelist.select()
        for row in db_rows:
            white_list[row.phone_number] = {
                "name": row.name,
                "last_name": row.last_name,
            }

        return white_list

    def get_user_sessions(self):
        sessions = {}
        db_rows = Sessions.select()
        for row in db_rows:
            s = {
                "phone": row.phone_number,
            }
            sessions[row.user_id] = s
        return sessions

    def add_user_session(self, user_id, phone_number):
        with db_connection.atomic():
            Sessions.create(
                user_id=user_id,
                phone_number=phone_number
            )
    def add_transaction(self, summ, simline, project, destination, description, unrealsumm):
        Transactions.create(
                            summ = summ,
                            date = datetime.datetime.now().time(),
                            simline= simline,
                            unrealsumm= unrealsumm,
                            project= project,
                            destination= destination,
                            description= description
                            )
        return True
    def show_transaction(self, quan):
            db_rows = Transactions.select().order_by(-Transactions.id).limit(quan).dicts()
            rows = []
            for row in db_rows:
                rows.append(row)
            return rows


database = Database()
