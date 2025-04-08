# Simple Web Framework

```
.
├── runserver.py        <-- Script that run server
├── db.json             <-- Database in JSON format
├── app                 <-- Simple Web Framework module
│   ├── settings.py     <= Setting for app
│   ├── wsgi.py         <= WSGI application
│   ├── urls.py         <= URL routes
│   ├── views.py        <= Views for routes
│   ├── db.py           <= Module for work with DB
│   ├── templates.py    <= Module for work with templates
│   ├── responce.py     <= Responce classes
│   └── utils.py        <= Utils 
└── templates           <-- Templates folder
    ├── 404.html        
    ├── added.html
    ├── add.html
    ├── index.html
    └── view.html
```

# Task T28.4

Toys DB Structure:

```json
{
    "toys": [
        {
            "name": str,             // toy name
            "price": str             // toy price
            "age-range": [int, int]  // age range for toy
        },
    ]
}
```
