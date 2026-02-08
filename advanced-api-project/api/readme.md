## Book API Views

### BookListView
- Endpoint: GET /books/
- Access: Public
- Description: Returns a list of all books

### BookCreateView
- Endpoint: POST /books/create/
- Access: Authenticated users only
- Description: Creates a new book instance

### Permissions
- Read-only access is public
- Write operations require authentication
