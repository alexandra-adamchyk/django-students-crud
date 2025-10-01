## Thursday Sep. 18

CRUD => Create, Read, Update, delete

goal: support CRUD operations in `projects` application during ILP session.

- Handling forms the Django Way

* Django Forms API


















## Wednesday Sep. 17

# Learning goals
- Identify and use the Django ORM model manager
- Create database records using the Manager
- Query with the Manager and eventually understanding QuerySets
- Use `.filter()` for making conditional queries
- Update and delete records

[Migration related task]
- Add new fields to a table in a databse



- Every model in Django has a Manager
-- this manager can be used to handle "CRUD"

There are about 3 different ways one can create a record for a database table
(a.k.a. INSERT in SQL)

Method 1:
1) `student1 = Student.objects.create(**kwargs)`

Method 2:
2) two steps (2 lines of code)

```
student2 = Student(**kwargs) # no id is avaialble
student2.save() # new id is returned #INSERT INTO
```

3) bulk creation (we need to many things at once)


```
Student.objects.bulk_create([ Student(**kwargs), Student(**kwargs)])
```


## QuerySet
- a collection of database records
- lazy evaluation: not executed until it is used
- can be chained (hint: method chaining)

The results of a the methods we chain on the Manager e.g. all(), get(), filter()

```
Student.objects.all()
```
In the example above, it shows a "preview" of a SELECT statement but does not commit that statement.

However, if you try to access something or load all the data, then it will be committed. Execute the query and fetch the results

e.g.

```
list(Student.objects.all())
students = Student.objects.all()
students[1:10]
students.first()
students.last()
```


## Update a student

_Method 1_

- get the student
- change the values of the student
- save the changes

e.g.

```
student = Student.objects.get(*arg) or .get(**kwargs) or .filter(**kwargs).first()
# in case more than one record exists, you can use a filter()
# it is better to be specific when making updates so you 
# do not update the wrong detail.

# update the individual column values
student.first_name = "bla blah"
#syntax: student.<column name> = <values>

# then save
student.save() # UPDATE SQL
```

_Method 2_

```
Student.objects.filter(first_name='William').update(last_name = "Bah bah")
```

Hints: It might be wiser to use primary keys
- id
- SSN (social security number)
- tax number
- passport number
- SKU or Barcode



# Delete a student

- get the item or items 
- call .delete()

```
Student.objects.get(id=2).delete()

Student.objects.filter(first_name='Joe').delete()

Student.objects.all().delete()
```



















# Tuesday Sept. 16: models ORM (part 1)

## Goals:
- Understand what ORM (object relational map) is and the problems it solves.
- Know the pros and cons of ORM.
- Be able to define Django models and sync them with PostgreSQL.
- Run migrations and see generated SQL with sqlmigrate.
- Write basic ORM queries.
- Convert existing DB tables into Django models using inspectdb.


Technology (breakdown)
- software developer / software engineer have to keep so much in their heads when they are working.
* LLMs (keeping up with AI and AI workflows)
* Python
* a database (SQL)
* CSS
* HTML
* Javascript
    * Frameworks/library: React, Svelte, angular, etc.


Multilingual! 

"Context Switching"

- Python (Today)

def function():
    pass

- Javascript (Tomorrow)

function testSome() {

}
- SQL (Friday)

INSERT INTO users ();

- Python (Monday)

def function_b():
   pass


ORM -> write one language for everything 
- logic (python)   
- database (python)
70% of your code will Python
30% => HTML, Javascript, CSS

ORM are a bridge between objects (Python classes) and relational tables



# Small challenge
Create an application called:
`students`

command: `python manage.py startapp ???`

Create a model called: `Student` with following fields:
- first_name
- last_name
- nickname

After creating the model, add the app to `INSTALLED_APPS`, make migrations and the run the migrate command.

command hints:

1) `python manage.py makemigrations`
2) `python manage.py migrate`


## Play with the Django ORM API
- `python manage.py shell`
- create a student in Python manage shell

## Play with the PSQL cli
select the students in PSQL

`SELECT * FROM <table name>;`

hint: For table names, `\dt` can give you a clue

Summary:
- it is important to check for spellings in django
- check that new applications are added to `INSTALLED_APPS`
- when changes are made to the `models.py` file, always make migrations and migrate (this actually creates the tables)
- Relax, this stuff takes time to learn (practicing)

Files we touched:
- models.py
- settings.py

Other technicalities:
- switching to the postgres database
- make sure to install database dependencies


