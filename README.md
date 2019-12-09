# Escalation Reviewer
> To create a clear view of escalation processes

[![NPM Version][npm-image]][npm-url]

Frontend: Vue.js + Vuetify

Backend: Djange RESTful Framework

Database: Sqlite

Host: Azure Web App

![](header.png)

## Installation



```sh
# Frontend
npm run serve # service start at localhost:8080

# Backend (in a new terminal)
python manage.py runserver # service start at localhost:8000
```


## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [example] folder._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
# Frontend
cd client
npm install
npm run serve # service start at localhost:8080

# Backend (open a new terminal or
# pull docker image from dockerhub)
source env/bin/activate
python manage.py runserver # service start at localhost:8000
```

## Database Design

Engineer

|      | item  | kind                     | appendix |
| ---- | ----- | ------------------------ | -------- |
| PK   | _id   |                          |          |
|      | name  | CharField(max_length=20) |          |
|      | title | CharField(max_length=3)  |          |



Process

|      | item     | kind                    | appendix |
| ---- | -------- | ----------------------- | -------- |
| PK   | _id      |                         |          |
|      | title    | CharField(max_length=3) |          |
|      | created  | DateTimeField           |          |
| FK   | engineer | ForeignKey(Engineer)    |          |
|      | status   | CharField(max_length=7) |          |

Stage

|      | item    | kind                    | appendix |
| ---- | ------- | ----------------------- | -------- |
| PK   | _id     |                         |          |
|      | title   | CharField(max_length=3) |          |
|      | created | DateTimeField           |          |
| FK   | process | ForeignKey(Process)     |          |
|      | status  | CharField(max_length=7) |          |

Comment

|      | item         | kind                       | appendix |
| ---- | ------------ | -------------------------- | -------- |
| PK   | _id          |                            |          |
|      | created      | DateTimeField              |          |
| FK   | stage        | ForeignKey(Stage)          |          |
| FK   | author       | ForeignKey(Engineer)       |          |
|      | result       | CharField(max_length=7)    |          |
|      | comment_text | CharField(max_length=1000) |          |



## Release History


* 0.1.0
    * The first proper backend release
    * CHANGE: Enable CURD with Django RESTful API
* 0.0.1
    * Work with Django

## Meta

Juncheng Zhu – [@Feo-0134](https://github.com/feo-0134) – t-junzhu@microsoft.com

Distributed under the MIT license. 
<!-- See ``LICENSE`` for more information. -->

[https://github.com/feo-0134](https://github.com/feo-0134/)

## Contributing

1. Fork it <!-- (<https://github.com/yourname/yourproject/fork>) -->
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/vue-cli
[npm-url]: https://npmjs.org/package/vue-cli

