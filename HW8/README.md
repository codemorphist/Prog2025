# Simple Web Framework

```
├── runserver.py        <<< Script that run server >>>
│
├── db.json             <-- Database in JSON format
├── app                 <-- Simple Web Framework module
│   ├── settings.py     <= Setting for app
│   ├── wsgi.py         <= WSGI application
│   ├── urls.py         <= URL routes
│   ├── views.py        <= Views for routes
│   ├── db.py           <= Module for work with DB
│   ├── templates.py    <= Module for work with templates
│   ├── responce.py     <= Responce classes
│   ├── errors.py       <= HTTP errors generators
│   ├── http.py         <= HTTP constants
│   └── utils.py        <= Utils 
└── templates           <-- Templates folder
    ├── 400.html        
    ├── 404.html        
    ├── 500.html        
    └── ... 
```

# Task T28.4

Toys DB Structure:

```json
{
    "toys": [
        {
            "name": "str",               
            "price": "float"             
            "age": "int"
        },
    ]
}
```
