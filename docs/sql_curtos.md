```python
@router.post("/", response_model=ContactResponse, status_code=201)
def create_contact(contact: ContactSchema):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (contact.first_name, contact.last_name, contact.phone_number)
        )
        conn.commit()
        contact_id = cursor.lastrowid
        return {**contact.dict(), "id": contact_id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
```

---

## 1️⃣ Route Declaration

```python
@router.post("/", response_model=ContactResponse, status_code=201)
```

* **`@router.post("/")`**
  Declares this function as a **POST endpoint** at the root of the router (`/`).
  It will respond to HTTP POST requests.

* **`response_model=ContactResponse`**
  Tells FastAPI to **validate and serialize the response** according to the `ContactResponse` Pydantic model.
  Ensures the API always returns data in a consistent format.

* **`status_code=201`**
  Returns HTTP **201 Created** when the request succeeds, indicating a new resource was created.

---

## 2️⃣ Function Parameters

```python
def create_contact(contact: ContactSchema):
```

* **`contact`** is automatically parsed from the **JSON request body**.
* FastAPI uses the **Pydantic model `ContactSchema`** to validate:

  * `first_name` must be a string
  * `last_name` must be a string
  * `phone_number` must be a string
* If the input doesn’t match the schema, FastAPI automatically returns **422 Unprocessable Entity**.

---

## 3️⃣ Establish Database Connection

```python
conn = get_connection()
cursor = conn.cursor()
```

* `get_connection()` returns a **new MySQL connection**.
* `conn.cursor()` creates a **cursor object**, which is used to execute SQL queries.
* Each request **gets its own connection**, which ensures safe, isolated operations.

---

## 4️⃣ Execute the SQL Query

```python
cursor.execute(
    "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
    (contact.first_name, contact.last_name, contact.phone_number)
)
```

* **`INSERT INTO contacts (...) VALUES (%s, %s, %s)`**

  * SQL statement to insert a new row into the `contacts` table.
  * `%s` are placeholders to **safely pass values**, preventing SQL injection.

* **Tuple `(contact.first_name, contact.last_name, contact.phone_number)`**

  * These are the actual values inserted into the placeholders.

---

## 5️⃣ Commit the Transaction

```python
conn.commit()
```

* MySQL operations are **transactional**.
* `commit()` permanently saves the changes to the database.
* If `commit()` is not called, the insert will **not persist**.

---

## 6️⃣ Retrieve the Inserted ID

```python
contact_id = cursor.lastrowid
```

* `cursor.lastrowid` returns the **auto-incremented primary key** of the newly inserted row.
* Useful to **return the created resource ID** to the client.

---

## 7️⃣ Return Response

```python
return {**contact.dict(), "id": contact_id}
```

* `contact.dict()` converts the Pydantic model into a **Python dictionary**.
* `{**contact.dict(), "id": contact_id}` merges the input data with the generated `id`.
* FastAPI then **serializes this dict to JSON** to send as the HTTP response.

**Example Response:**

```json
{
  "id": 5,
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "123456789"
}
```

---

## 8️⃣ Error Handling

```python
except Exception as e:
    conn.rollback()
    raise HTTPException(status_code=500, detail=str(e))
```

* **`except Exception as e`** catches any error during execution.
* **`conn.rollback()`** undoes any partial changes if an error occurs, keeping the database **consistent**.
* **`HTTPException`** returns an HTTP **500 Internal Server Error** with the error message to the client.

---

## 9️⃣ Cleanup

```python
finally:
    cursor.close()
    conn.close()
```

* Ensures the **cursor and connection are always closed**, even if an error occurs.
* Prevents **connection leaks** which can exhaust database resources.

---

## 🔑 Key Concepts Illustrated

| Concept             | How It’s Used                                   |
| ------------------- | ----------------------------------------------- |
| Pydantic validation | `ContactSchema` ensures proper input            |
| SQL placeholders    | `%s` prevents SQL injection                     |
| Transactions        | `commit()` / `rollback()` ensure data integrity |
| Resource cleanup    | `finally` closes connections and cursors        |
| Error handling      | HTTPException sends proper error response       |

---

This endpoint is a **classic FastAPI + MySQL CRUD example**:

* Validates input
* Safely inserts into DB
* Handles errors
* Returns a clean, consistent response

