from mongoengine import *

'''MongoDB/pymongo

Field types
  BinaryField, BooleanField, ComplexDateTimeField, DateTimeField, DecimalField,
  DictField, DynamicField, EmailField, EmbeddedDocumentField, FileField, FloatField,
  GenericEmbeddedDocumentField, GenericReferenceField, GeoPointField, ImageField,
  IntField, ListField, MapField, ObjectIdField, ReferenceField, SequenceField,
  SortedListField, StringField, URLField, UUIDField

Field arguemnts
  db_field, name, required, default, unique, unique_with, primary_key, choices, help_text, verbose_name
'''

connect('pyws', host='localhost', port=27017, username='', password='')

class User(Document):
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)

class Post(Document):
    title = StringField(max_length=50, required=True, unique=True)
    author = ReferenceField(User, dbref=True)

# EOF
