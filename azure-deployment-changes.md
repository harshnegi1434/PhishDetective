# Code Changes

## in backend/app.py (line 11)

**development:**
```python
CORS(app, resources={r"/check-url": {"origins": "http://localhost:3000"}})
```

**production:**
```python
CORS(app, resources={r"/check-url": {"origins": "http://phishdetective.centralindia.azurecontainer.io:3000"}})
```

## in frontend/check/page.tsx (line 28)

**development:**
```javascript
const apiUrl = 'http://localhost:5000/check-url';
```
**production:**
```javascript
const apiUrl = 'http://phishdetective-backend.centralindia.azurecontainer.io:5000/check-url';
```