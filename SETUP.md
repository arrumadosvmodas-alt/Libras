# 🚀 Setup Instructions - LIBRAS App

## Quick Start (5 minutes)

### Option 1: Docker Compose (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/libras.git
cd libras

# 2. Copy environment file
cp .env.example .env

# 3. Start all services
docker-compose up -d

# 4. Run database migrations
docker-compose exec backend alembic upgrade head

# 5. Seed initial data
docker-compose exec backend python seed_data.py

# 6. Access the application
# Frontend: http://localhost:5173
# API Docs: http://localhost:8000/docs
```

**Test Accounts:**
- Admin: `admin@libras.app` / `admin123`
- Student: `student@libras.app` / `student123`

### Option 2: Local Development

#### 2.1 Backend Setup

```bash
# 1. Navigate to backend
cd backend

# 2. Create Python virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Copy .env file to parent directory
cp ../.env.example ../.env

# 6. Start PostgreSQL and Redis locally
# Install using Docker:
docker run -d -p 5432:5432 -e POSTGRES_USER=libras_user -e POSTGRES_PASSWORD=libras_password -e POSTGRES_DB=libras_db postgres:16-alpine

docker run -d -p 6379:6379 redis:7-alpine

# Or install locally on your machine

# 7. Run database migrations
alembic upgrade head

# 8. Seed initial data
python seed_data.py

# 9. Start the backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Server runs at: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

#### 2.2 Frontend Setup

```bash
# 1. Open a new terminal and navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev

# App runs at: http://localhost:5173
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file:

```env
# Database
DATABASE_URL=postgresql://libras_user:libras_password@localhost:5432/libras_db

# Server
DEBUG=True
SECRET_KEY=dev-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:5173"]

# Redis
REDIS_URL=redis://localhost:6379

# Optional: Stripe (for payments)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...

# Optional: AWS S3 (for video storage)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=libras-videos
AWS_REGION=us-east-1
```

## 📊 Database

### Creating Migrations

After modifying models, create a migration:

```bash
cd backend
alembic revision --autogenerate -m "Descriptive message"
alembic upgrade head
```

### Resetting Database (⚠️ Destructive)

```bash
# Drop all tables and recreate
alembic downgrade base
alembic upgrade head

# Re-seed data
python seed_data.py
```

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest                    # Run all tests
pytest -v                # Verbose output
pytest --cov=app         # With coverage report
pytest tests/test_auth.py  # Specific test file
```

### Frontend Tests

```bash
cd frontend
npm test                  # Run tests
npm run test:coverage    # With coverage
```

## 📝 Common Tasks

### Create Admin User

```bash
cd backend
python
>>> from app.models.user import User, UserRole
>>> from app.core.security import get_password_hash
>>> from app.db.session import SessionLocal
>>> 
>>> db = SessionLocal()
>>> admin = User(
...     email="newadmin@libras.app",
...     full_name="Admin Name",
...     hashed_password=get_password_hash("securepassword"),
...     role=UserRole.ADMIN
... )
>>> db.add(admin)
>>> db.commit()
```

### Check Database Connection

```bash
cd backend
python
>>> from app.db.session import engine
>>> connection = engine.connect()
>>> connection.execute("SELECT 1")
>>> print("✅ Database connected!")
```

### View API Documentation

Visit `http://localhost:8000/docs` (Swagger UI)
Or `http://localhost:8000/redoc` (ReDoc)

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>

# Or use different port
uvicorn app.main:app --port 8001
```

### Database Connection Error

```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Check database URL
cat .env | grep DATABASE_URL

# Test connection
psql postgresql://libras_user:libras_password@localhost:5432/libras_db
```

### Redis Connection Error

```bash
# Check Redis is running
docker ps | grep redis

# Or start Redis manually
redis-server
```

### Module Not Found (Python)

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Node Modules Issues

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

## 📚 Frontend Development

### Project Structure

```
frontend/src/
├── app/              # Main app component
├── components/       # Reusable components (Header, etc)
├── features/         # Feature modules (auth, courses, lessons)
├── lib/              # Utilities (api client, helpers)
├── types/            # TypeScript type definitions
└── main.tsx          # React entry point
```

### Adding New Pages

1. Create file in `src/features/{feature}/YourPage.tsx`
2. Add route in `src/app/App.tsx`
3. Add navigation link in `src/components/Header.tsx`

### API Client Usage

```typescript
import { apiClient } from '@/lib/api';

// Get courses
const courses = await apiClient.getCourses();

// Create course (admin)
const newCourse = await apiClient.createCourse({
  title: "New Course",
  slug: "new-course",
  description: "..."
});

// Login
const token = await apiClient.login({
  email: "user@example.com",
  password: "password"
});
```

## 🚀 Deployment

### Pre-deployment Checklist

- [ ] Change `SECRET_KEY` to random value
- [ ] Set `DEBUG=False`
- [ ] Configure production database
- [ ] Configure Redis
- [ ] Setup SSL/TLS certificate
- [ ] Configure email service
- [ ] Setup payment gateway (Stripe)
- [ ] Configure storage (S3/R2)
- [ ] Setup monitoring/logging
- [ ] Enable HTTPS redirects

### Deploy to Heroku/Railway/Render

```bash
# Build Docker image
docker build -t libras-app:latest .

# Push to registry
docker tag libras-app:latest your-registry/libras-app:latest
docker push your-registry/libras-app:latest

# Update deployment
# (Platform-specific instructions)
```

## 📞 Support

- 📧 Email: arrumadosvmodas@gmail.com
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

## 📄 License

MIT License - See LICENSE file
