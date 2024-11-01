# API DOCUMENTS
### 1. User To Do List API
This API returns a user's to-do list according to their ID.

#### Request:
- Method: `GET`
- BASE URL: `http://localhost:5000/?user_id={user_id}`
- Endpoint: `/`
- Query Parameters: 
  - `user_id` (string, required): The ID of the user whose to-do list will be retrieved.

#### Request Example:
```
curl -X GET "http://localhost:5000/?user_id=1"
```

#### Response:
- Success (200 OK)
 - Content-Type: `text/html`
 - Description: Renders an HTML page with the list of to-do items.

- Failure (400 Bad Request)
```
{
  "error": "User ID is missing"
}
```


### 2. Add New To-Do Item
Adds a new to-do item for a specified user.

#### Request
- Method: `POST`
- BASE URL: `http://localhost:8000/add_todo`
- Endpoint: `/add_todo`
- Form Data Parameters:
 - `task` (string, required): The task to add to the to-do list.
 - `user_id` (integer, required): The ID of the user who owns the to-do list.

#### Request Example:
```
curl -X POST "http://localhost:5000/add_todo" \
  -d "task=New Task" \
  -d "user_id=1"
```
#### Response (Logged In):
- Success (302 Redirect)
 - Description: Redirects to the to-do list page of the user after adding the task.
- Failure (400 Bad Request)
```
{
  "error": "Task or User ID is missing"
}
```


### 3. Delete To-Do Item
Deletes a specified to-do item.

#### Request
- Method: `POST`
- BASE URL: `http://localhost:8000/delete_todo/<task_id>`
- Endpoint: `/delete_todo/<task_id>`
- Form Data Parameters:
 - `user_id` (integer, required): The ID of the user whose to-do item is being deleted.
- Path Parameters:
 - `task_id` (integer, required): The ID of the to-do item to delete.

#### Request Example:
```
curl -X POST "http://localhost:5000/delete_todo/1" \
  -d "user_id=1"
```

#### Response (Logged In):
- Success (302 Redirect)
 - Description:  Redirects to the user's to-do list after deleting the item.
- Failure (400 Bad Request)
```
{
  "error": "User ID is missing"
}
```