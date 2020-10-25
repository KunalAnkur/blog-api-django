# blog-api-django

### API Endpoints

- For user registration:
  `http://localhost:8000/rest-auth/registration/`

- For user login:
  `http://localhost:8000/rest-auth/login/`

- For view list of authenticated user articles:
  `http://localhost:8000/api/my-articles/?page=<PAGE_NUM>&limit=<LIMIT>`

- For view details of authenticated user articles:
  `http://localhost:8000/api/<int:pk>/my-article-detail/`

- For view list of articles:
  `http://localhost:8000/api/?page=<PAGE_NUM>&limit=<LIMIT>`

- For view details of article:
  `http://localhost:8000/api/<int:pk>/`
- For create new article:
  `http://localhost:8000/api/create/`

- For update article:
  `http://localhost:8000/api/<int:pk>/update/`

- For delete article:
  `http://localhost:8000/api/<int:pk>/delete/`

- For notification list
  `http://localhost:8000/api/notification/get-notification/?page=<PAGE_NUM>&limit=<LIMIT>`

- For notification for user:
  `http://localhost:8000/api/notification/get-user-notification/?page=<PAGE_NUM>&limit=<LIMIT>`

- For mark notification read by user:
  `http://localhost:8000/api/notification/mark-notification-read/`
