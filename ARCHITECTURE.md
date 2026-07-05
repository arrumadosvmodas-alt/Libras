# 🏗️ Architecture - LIBRAS App

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     User Browser                            │
│                  (React + TypeScript)                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTP/HTTPS
                       │ (REST API)
                       ▼
┌──────────────────────────────────────────────────────────────┐
│                    FastAPI Server                           │
│        (Python 3.12 + SQLAlchemy + Pydantic)               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Authentication  │  Courses  │  Exercises  │ Progress  │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────┬──────────────────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
    ┌────────┐   ┌─────────┐   ┌──────────┐
    │PostgreSQL│ │  Redis  │   │   S3/R2   │
    │(Database)│ │(Cache)  │   │(Videos)  │
    └────────┘   └─────────┘   └──────────┘
```

## Backend Architecture

### Layered Architecture

```
┌─────────────────────────────────────────────┐
│         API Layer (FastAPI Routes)          │
│    /api/v1/auth, /api/v1/courses, etc      │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│         Service Layer (Business Logic)      │
│    CourseService, AuthService, etc         │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│     Repository Layer (Data Access)          │
│    CourseRepository, UserRepository, etc   │
└──────────────────────┬──────────────────────┘
                       │
┌──────────────────────▼──────────────────────┐
│      Database Layer (SQLAlchemy ORM)        │
│    Models, Sessions, Migrations            │
└─────────────────────────────────────────────┘
```

### Directory Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   │
│   ├── core/
│   │   ├── config.py           # Settings from environment
│   │   └── security.py         # JWT, password hashing
│   │
│   ├── db/
│   │   ├── session.py          # Database session factory
│   │   └── base.py             # SQLAlchemy DeclarativeBase
│   │
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── exercise.py
│   │   ├── progress.py
│   │   └── payment.py
│   │
│   ├── schemas/                # Pydantic request/response schemas
│   │   ├── user.py
│   │   ├── course.py
│   │   ├── exercise.py
│   │   └── progress.py
│   │
│   ├── repositories/           # Data access layer
│   │   ├── user_repository.py
│   │   ├── course_repository.py
│   │   └── ...
│   │
│   ├── services/               # Business logic layer
│   │   ├── auth_service.py
│   │   ├── course_service.py
│   │   └── ...
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── router.py       # Route aggregator
│   │       └── endpoints/      # Route handlers
│   │           ├── auth.py
│   │           ├── courses.py
│   │           └── ...
│   │
│   └── tests/                  # Unit tests
│       ├── conftest.py
│       ├── test_health.py
│       └── ...
│
├── alembic/                    # Database migrations
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── pyproject.toml
├── requirements.txt
├── seed_data.py
└── Dockerfile
```

### Key Design Patterns

#### 1. Dependency Injection
```python
# FastAPI automatic dependency injection
@router.get("/courses")
async def list_courses(db: Session = Depends(get_db)):
    # db is automatically provided
    return db.query(Course).all()
```

#### 2. Repository Pattern
```python
# Data access abstraction
class CourseRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_slug(self, slug: str):
        return self.db.query(Course).filter(...).first()
```

#### 3. Service Layer
```python
# Business logic separation
class CourseService:
    def __init__(self, repo: CourseRepository):
        self.repo = repo
    
    def get_course_with_stats(self, slug: str):
        course = self.repo.get_by_slug(slug)
        # Add business logic
        return course
```

#### 4. Schema Validation
```python
# Pydantic schemas for type safety
class CourseCreate(BaseModel):
    title: str
    slug: str
    description: Optional[str] = None
    
    # Validation
    @field_validator('slug')
    def slug_format(cls, v):
        assert v.islower()
        return v
```

## Frontend Architecture

### Component Architecture

```
App
├── Header (Navigation)
├── HomePage
│   ├── Hero
│   ├── Features
│   └── CTA
├── CoursesPage
│   └── CourseCard (List)
├── CoursePage
│   └── ModuleCard
│       └── LessonCard
├── LessonPage
│   ├── VideoPlayer
│   ├── ExerciseComponent
│   └── ProgressBar
├── AuthPage
│   ├── LoginForm
│   └── SignupForm
└── ProgressPage
    └── StreakCounter
```

### State Management

**TanStack Query (React Query)** for server state:
```typescript
// Fetch and cache server data
const { data: courses, isLoading } = useQuery({
  queryKey: ['courses'],
  queryFn: () => apiClient.getCourses()
});
```

**localStorage** for client state:
```typescript
// JWT tokens
localStorage.setItem('access_token', token);
const token = localStorage.getItem('access_token');
```

### API Client Pattern

```typescript
class ApiClient {
  private client: AxiosInstance;
  
  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL
    });
    
    // Add token to all requests
    this.client.interceptors.request.use(config => {
      const token = localStorage.getItem('access_token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });
  }
  
  async getCourses(): Promise<Course[]> {
    const response = await this.client.get<Course[]>('/courses');
    return response.data;
  }
}

// Singleton instance
export const apiClient = new ApiClient();
```

### Type Safety

**TypeScript interfaces for all API responses:**
```typescript
interface Course {
  id: number;
  title: string;
  slug: string;
  modules: Module[];
  // ...
}

// Used everywhere
const courses: Course[] = await apiClient.getCourses();
```

## Database Schema

### Entity Relationships

```
User
├── Progress (1:N)
├── Streaks (1:1)
└── Subscriptions (1:N)

Course
└── Modules (1:N)
    └── Lessons (1:N)
        ├── LessonSteps (1:N)
        └── Exercises (1:N)
            └── ExerciseOptions (1:N)

Subscription
└── Payments (1:N)
```

### Core Tables

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| users | User accounts | email, password_hash, role |
| courses | Learning courses | title, slug, difficulty |
| modules | Course sections | course_id, title, order |
| lessons | Individual lessons | module_id, title, duration |
| exercises | Interactive tasks | lesson_id, question, points |
| user_progress | Completion tracking | user_id, lesson_id, score |
| user_streaks | Daily streaks | user_id, current_streak |
| subscriptions | Billing | user_id, plan, status |
| payments | Transactions | subscription_id, amount, status |

## Data Flow

### Example: User Takes a Lesson

```
1. Frontend requests lesson
   GET /api/v1/lessons/{slug}
        │
        ▼
2. API Router receives request
   lesson.py endpoint
        │
        ▼
3. Service layer applies business logic
   LessonService.get_lesson(slug)
        │
        ▼
4. Repository queries database
   LessonRepository.get_by_slug(slug)
        │
        ▼
5. SQLAlchemy ORM executes query
   db.query(Lesson).filter(...).first()
        │
        ▼
6. Database returns data
   SELECT * FROM lessons WHERE slug = ?
        │
        ▼
7. Response serialized with schema
   LessonResponse.from_orm(lesson)
        │
        ▼
8. JSON returned to client
   { id: 1, title: "...", steps: [...] }
```

## Authentication Flow

```
1. User submits credentials
   POST /api/v1/auth/login
   { email, password }
        │
        ▼
2. Backend verifies password
   bcrypt.verify(password, hashed)
        │
        ▼
3. JWT tokens generated
   access_token, refresh_token
        │
        ▼
4. Client stores tokens
   localStorage.setItem('access_token', token)
        │
        ▼
5. Future requests include token
   Authorization: Bearer {access_token}
        │
        ▼
6. Backend validates token
   decode_token(token) ✓
        │
        ▼
7. Request processed with user context
```

## Performance Considerations

### Caching Strategy

1. **Database Queries**: SQLAlchemy with eager loading
```python
# Avoid N+1 queries
courses = db.query(Course).options(
    selectinload(Course.modules).selectinload(Module.lessons)
).all()
```

2. **Redis Cache**: For frequently accessed data
```python
# Cache course list
cache_key = "courses:all"
cached = redis.get(cache_key)
if not cached:
    courses = db.query(Course).all()
    redis.setex(cache_key, 3600, json.dumps(courses))
```

3. **Frontend Caching**: TanStack Query
```typescript
// Automatic caching and refetching
useQuery({
  queryKey: ['courses'],
  queryFn: getCourses,
  staleTime: 5 * 60 * 1000  // 5 minutes
})
```

### Database Optimization

1. **Indexes** on frequently queried columns:
   - `users.email` (unique)
   - `courses.slug` (unique)
   - `user_progress.user_id`, `lesson_id`

2. **Pagination** for large datasets:
```python
@router.get("/courses")
def list_courses(skip: int = 0, limit: int = 20):
    return db.query(Course).offset(skip).limit(limit).all()
```

## Security Architecture

### Authentication
- **JWT tokens** with configurable expiry
- **Bcrypt hashing** for passwords
- **Secure tokens** in localStorage (httpOnly in production)

### Authorization
- **Role-based access control** (RBAC):
  - STUDENT: Basic access
  - INSTRUCTOR: Can create content
  - ADMIN: Full access

- **Route protection**:
```python
def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403)
    return current_user
```

### Data Validation
- **Pydantic schemas** validate all inputs
- **SQLAlchemy** prevents SQL injection
- **CORS** restricts cross-origin access

### Environment Security
- **No secrets in code**: All in `.env`
- **Docker secrets**: For production
- **Encrypted credentials**: For sensitive data

## Deployment Architecture

```
┌─────────────────────────────────────────────┐
│          Load Balancer (Nginx/HAProxy)      │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┼───────┐
       ▼       ▼       ▼
   ┌──────┐ ┌──────┐ ┌──────┐
   │Cont.1│ │Cont.2│ │Cont.3│  (FastAPI)
   └──┬───┘ └──┬───┘ └──┬───┘
      │        │        │
      └────────┼────────┘
               │
      ┌────────▼────────┐
      │  PostgreSQL     │
      │  (RDS/Managed)  │
      └────────┬────────┘
               │
      ┌────────▼────────┐
      │  Redis Cache    │
      │  (ElastiCache)  │
      └─────────────────┘
```

## Monitoring & Logging

### Application Metrics
- Request latency
- Error rates
- Database query performance
- Cache hit ratio

### Structured Logging
```python
logger.info("User login successful", extra={
    "user_id": user.id,
    "timestamp": datetime.utcnow(),
    "ip": request.client.host
})
```

### Health Checks
```python
GET /api/v1/health  # Application health
GET /metrics        # Prometheus metrics
GET /readiness      # Ready to accept traffic
```

## Testing Strategy

### Unit Tests
- Test individual functions in isolation
- Mock external dependencies

### Integration Tests
- Test API endpoints
- Use test database

### E2E Tests
- Test complete user workflows
- Use selenium/playwright

### Load Testing
- Locust for load testing
- Artillery for API testing

## Future Improvements

1. **Microservices**: Split into separate services
2. **Message Queue**: RabbitMQ/Celery for async tasks
3. **GraphQL**: Alternative API layer
4. **WebSocket**: Real-time notifications
5. **Machine Learning**: AI-powered sign recognition
6. **Mobile App**: React Native iOS/Android

---

**See SETUP.md for development instructions**
