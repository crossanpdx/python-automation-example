### Python Automation Example

#### Tests

* Title field limit
* Release date acceptance
  * Positive and negative checks
* Rating input
  * Positive and negative checks

#### Additional test opportunities

* Additional assertions and range tests for field validations
* Use of data sheets with csv import or pandas to read in data 
  * Data sheets allow updating values to test with vs code changes
* Python supports sql connection queries 
  * Additional tests to query and validate data submitted
* Test white spacing in field
* Test strings on integer fields
* Test special characters

#### Notes
``````
For this exercise I used PyCharm, however I am in favor of portable
packages. Dockerize or configuring in pipeline setup for flexibility
in where to run, who can run, and remove local setup constraints. This 
can take additional setup time to implement, but saves time in the 
long run.

