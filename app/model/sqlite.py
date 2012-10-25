from peewee import *

'''PeeWee

Field types
  CharField, TextField, DateTimeField, IntegerField, BooleanField, FloatField, DoubleField,
  BigIntegerField, DecimalField, PrimaryKeyField, ForeignKeyField, DateField, TimeField

Field arguemnts
  null, index, unique, verbose_name, help_text, db_column, default, choices, primary_key, sequence
  max_length, formats, max_digits, decimal_places, auto_round, rounding, rel_model, related_name, cascade, extra
'''

database = SqliteDatabase('pyws.db')
database.connect()

class CustomModel(Model):

    class Meta:
        database = database

class User(CustomModel):
    first_name = CharField(max_length=50, required=True)
    last_name = CharField(max_length=50, required=True)

class Post(CustomModel):
    title = CharField(max_length=50, required=True, unique=True)
    author = ForeignKeyField(User, related_name='author', required=True)

# EOF
