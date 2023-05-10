py -3 -m venv venv

uvicorn main:app --reload


--- ORM
Object Relational Mapper
Layer of abstraction that sits between the db and app
Can perform all db operations through traditional python code. No SQL !!

Use python models to define tables 

Sqlalchemy is one of the most popular python ORMS