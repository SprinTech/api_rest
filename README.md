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
    |── api/
    |   ├── API_REST.db
    |   ├── database.py
    |   ├── main.py
    |   ├── models.py
    |   ├── schemas.py
    |   ├── services.py
    |   └── test/
    |       └── test_database.py
    ├── app/
    |   └── main.py
    ├── functions/
    |   └── text_prediction.py
    └── models/
    |   ├── enc.joblib
    |   └── LR_model.pkl
    ├── README.md
    └── requirements.txt
```