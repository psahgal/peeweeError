from playhouse.postgres_ext import *


database = PostgresqlDatabase('postgres', user='postgres', password='myLocalPostgresPass', host='127.0.0.1', port=5432)
database.connect()


class Child(Model):
    class Meta:
        database = database
    name = CharField()


class Parent(Model):
    class Meta:
        database = database
    child = ForeignKeyField(Child)
    name = CharField()


entities = [Parent, Child]
database.drop_tables([Parent, Child])
database.create_tables([Parent, Child])


child1 = Child(name='Bob')
child2 = Child(name='Alice')
parent1 = Parent(child=child1, name='Martin')
parent2 = Parent(child=child2, name='Suzy')

with database.atomic():
    Child.bulk_create([child1, child2])
    Parent.bulk_create([parent1, parent2])

