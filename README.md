# Backend Assignment

Users Database REST API

- list users (`/api/users GET`)
- search for a user by name
- sort list by field name
- pagination of users list
- create new user (`/api/users - POST`)
- get detail of a user (`/api/users/<id> - GET`)
- update details of a user (`/api/users - PUT`)
- delete a user (`/api/users - DELETE`)

## Setup 

- API built in Django and Djangorestframework
- API hosted on pythonanywhere.com as [kcmail823.pythonanywhere.com](https://kcmail823.pythonanywhere.com)
- postman api doc link [documenter.getpostman.com/view/22943771/VUxNRTZU](https://documenter.getpostman.com/view/22943771/VUxNRTZU)
- create a web app in pythonanywhere and use the inbuilt sqlite3 database
- create a django project named myWebsite
- create an app named API in the myWebsite project
- create an user model for the Users database
- create serializers for the model 
- create custom pagination for the json response 
- add Search filter in views for name
- add ordering filter in view for ascending adn descending order
- define urls for api access
- map urls with views and templates
- create request handler views in views of API app
- add default rest_framework settings in settings of myWebsite
- set query parameters for API app in settings of myWebsite 
- create templates , static adn media folders
- create template for API
- test api in postman by CRUD operations
- create API documentation in postman 

## Resources:

- For sample data [https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json](https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json)

## **Instructions**

- [x] README.md should have all the details and instructions like how to setup and run the project
- [x] Repo should not contain irrelevant folders/files like cache files, build/dist directories etc.
- [x] Create API documentation using Swagger or similar framework
- [ ] Follow these steps for submission:
  1. Fork the repository
  1. Create issues and work on them in their respective branches
  1. Complete the tasks while following all instructions
  1. Create MRs and merge into main branch
  1. When done, Test if all task requirements are met and instructions followed
  1. Push code to github
  1. Deploy/Host your solution
  1. Reply to the same email with the URLs for **repo**, **hosted API** and **hosted documentation** 
- For any queries please email us at [hiring@truevalueaccess.com](mailto:hiring@truevalueaccess.com)
