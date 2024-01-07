# Phase 4 Lecture 1: Introduction to Flask-SQLAlchemy

## Objectives

By the end of today's lecture, you will be able to create a two-model ORM in Flask-SQLAlchemy and connect it to a database. You will also be able to play around with a sandbox environment involving the models.

## Lesson Plan

0. Run `pipenv install` and `pipenv shell` to install the necessary dependencies.
1. Update the config file to connect to the database and allow for migrations. Run `flask db init` to create the database, and `flask db migrate` and `flask db upgrade` to update its schema.
    - What is a **database**?
    - What is a **migration**?
    - What is the advantage of creating a separate file for database connection?
2. Add two models to the models file to represent a student and a homeroom class, following the included database schema.
    - How does the Flask-SQLAlchemy ORM differ from vanilla SQL?
    - What is the `repr` magic method?
    - What is a **primary key**? What is a **foreign key**?
3. Start to populate the database in a sandbox environment using the seed file.

## Looking Ahead

Tomorrow's lesson will discuss how to create a many-to-many relationship in Flask-SQLAlchemy.