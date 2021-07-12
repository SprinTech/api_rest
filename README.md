## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [File Structure](#file-structure)

## General info
Create personal diary API that analyse evolution of sentiment through time using NLP.

## Technologies
Project is created with:
* fastapi: 0.65.2
* sqlalchemy: 1.4.15
* pydantic: 1.8.2
* streamlit: 0.84.0

## File structure
```bash
└── api_rest/
    ├── api/
    ├   ├── API_REST.db   # database that store information about client and message
    ├   ├── database.py   # declare database
    ├   ├── main.py       # api requests
    ├   ├── models.py     # tables structure
    ├   ├── schemas.py    # tables schemas
    ├   ├── services.py   # database queries
    ├   └── tests/
    ├       └── test_database.py  # tests api requests
    ├── app/
    ├   └── main.py       # streamlit interface 
    ├── functions/
    ├   └── text_prediction.py    # text cleaning function 
    ├── models/
    ├   ├── enc.joblib    # text encoding
    ├   └── LR_model.pkl  # logistic regression model serialization
    ├── README.md
    └── requirements.txt
```