# ReferenceDataManagementSystem

The goal of the project is to create a very flexible reference data management system using neo4j as the backend.
This software should support data of bi-temporal nature (covers simple timestamped data) and also data with no time
component.

Tasks to do:
1. Create new node file.
   i. Write test cases.
2. Create new relation file (should support data with time component and without time component).
   i. Write test cases.
3. Create conda setup for this software (manage dependencies).
4. Create module to interact with terminal.
5. Create api to allow simple reads of data from database.
6. Create api to allow create and update operations.
7. Create api to integrate bi-temporal queries in reads.