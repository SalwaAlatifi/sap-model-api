# SAP Model API Documentation

## Overview

This API is used to predict a student's SGPA using a trained Random Forest machine learning model.

The API receives a student ID, retrieves the student's academic data, and returns the predicted SGPA.

---

# Base URL

https://sap-model-api.onrender.com

---

# Endpoint

## Predict Student SGPA

### Request

```http
GET/predict/student/{student_id}
```

### Example Request

```http
GET https://sap-model-api.onrender.com/predict/student/S1001
```

---

# Available Student IDs

The current mock database contains the following student IDs:

```text
S1001
S1002
S1003
```

---

# Error Response Example

If the provided student ID does not exist:

```json
{
  "error": "Student not found"
}
```

---

# Backend Usage Example

```javascript
async function getPrediction(studentId) {

  const response = await fetch(
    `https://sap-model-api.onrender.com/predict/student/${studentId}`
  );

  const data = await response.json();

  console.log(data.predicted_sgpa);

  return data;
}

getPrediction("S1001");
```

---

# Notes

* The API uses the GET method.
* No request body is required.
* The student ID must be passed in the URL.
* Main endpoint:

```text
/predict/student/{student_id}
```

---

# Deployment

The API is deployed using Render.
