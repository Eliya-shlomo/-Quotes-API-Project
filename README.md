# Quotes API Project

## Overview

This is a Flask-based REST API for managing quotes from philosophers. It allows users to:

- Retrieve all quotes by a specific philosopher.
- Add new quotes for a philosopher.
- Validate inputs to prevent duplicates or invalid entries.

## Features

- Input validation to ensure only valid data is accepted.
- Duplicate prevention for quotes by the same philosopher.
- Comprehensive error handling.

---

## API Endpoints

### 1. Get Quotes by Philosopher

**URL**: `/quotes/philosopher/<name>`  
**Method**: `GET`  
**Description**: Fetch all quotes for the specified philosopher.

#### Example Request:

```bash
GET /quotes/philosopher/nietzsche
[
    {
        "id": 1,
        "philosopher": "Nietzsche",
        "quote": "He who has a why to live can bear almost any how."
    }
]
```

#### example error:

```bash
{
    "error": "No quotes found for the philosopher."
}
```

### 1. Add a New Quote

**URL**: `/quotes/philosopher/<name>`  
**Method**: `POST`  
**Description**: Add a new quote for the specified philosopher.

#### Request Body:

```bash
{
    "quote": "To live is to suffer; to survive is to find some meaning in the suffering."
}
```

#### Success Response:

```bash
{
    {
    "message": "Quote successfully added",
    "quote_entry": {
        "id": 2,
        "philosopher": "Nietzsche",
        "quote": "To live is to suffer; to survive is to find some meaning in the suffering."
    }
}
```

#### Validation error:

##### Missing quote Field:

```bash
{
    "error": "The 'quote' field is required."
}
```

##### Empty quote Field:

```bash
{
    "error": "The quote cannot be empty."
}
```

##### Duplicate Quote:

```bash
{
    "error": "This quote already exists for the philosopher."
}
```

### Testing

#### Running Unit Tests:

The project includes unit tests to ensure the API works as expected.

##### Run All Tests:

```bash
python test_app.py
```

##### Expected Output: If all tests pass:

```plaintext
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

### Installation:

#### Prerequisites:

Python 3.8+
`pip`

##### Clone the Repository:

```bash
git clone https://github.com/Eliya-shlomo/quotes-api.git
cd quotes-api
```
