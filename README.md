# LIBRAS App 📚

Um aplicativo educacional completo para aprender **LIBRAS** (Língua Brasileira de Sinais) com videoaulas curtas, exercícios interativos, streak diário e revisão espaçada.

Inspirado em apps como **Duolingo** e **Lingvano**, mas focado especificamente em LIBRAS com conteúdo criado por professores surdos.

## 🚀 Features

- ✅ **Videoaulas Curtas**: 5-10 minutos por aula
- ✅ **Exercícios Interativos**: Multiple choice, video matching, etc
- ✅ **Streak Diário**: Gamificação com sequências de aprendizado
- ✅ **Revisão Espaçada**: Algoritmo para otimizar memorização
- ✅ **Progresso Rastreado**: Dashboard com estatísticas
- ✅ **Autenticação JWT**: Segurança completa
- ✅ **Admin CMS**: Painel para criar conteúdo
- ✅ **Responsive Design**: Mobile, tablet e desktop
- ✅ **Pronto para Pagamento**: Integração Stripe + RevenueCat

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.12+)
- **Database**: PostgreSQL 16
- **Cache**: Redis 7
- **ORM**: SQLAlchemy 2.0
- **Auth**: JWT + Bcrypt
- **Migrations**: Alembic
- **API Docs**: Swagger/OpenAPI

### Frontend
- **Framework**: React 18 + TypeScript
- **Build**: Vite
- **Router**: React Router 6
- **HTTP Client**: Axios
- **State Management**: TanStack Query
- **Validation**: Zod
- **Styling**: CSS3 + CSS Variables

### DevOps
- **Containerization**: Docker & Docker Compose
- **Environment**: .env configuration
- **Testing**: Pytest (backend), Vitest (frontend)

## 📦 Estrutura do Projeto

```
libras/
├── backend/
│   ├── app/
│   │   ├── main.py                 # Entry point FastAPI
│   │   ├── core/
│   │   │   ├── config.py           # Settings
│   │   │   └── security.py         # Auth utilities
│   │   ├── db/
│   │   │   ├── session.py          # Database session
│   │   │   └── base.py             # SQLAlchemy base
│   │   ├── models/                 # Database models
│   │   ├── schemas/                # Pydantic schemas
│   │   ├── repositories/           # Data access layer
│   │   ├── services/               # Business logic
│   │   ├── api/v1/
│   │   │   ├── router.py           # Routes aggregator
│   │   │   └── endpoints/          # API endpoints
│   │   └── tests/                  # Unit tests
│   ├── alembic/                    # Database migrations
│   ├── pyproject.toml              # Dependencies
│   ├── requirements.txt            # Frozen dependencies
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── main.tsx                # React entry point
│   │   ├── app/
│   │   │   ├── App.tsx             # Main component
│   │   │   └── App.css             # Global styles
│   │   ├── components/             # Reusable components
│   │   ├── features/               # Feature modules
│   │   ├── lib/                    # Utilities & API client
│   │   ├── types/                  # TypeScript types
│   │   └── services/               # External services
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── Dockerfile
│
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose (recomendado)
- Node.js 20+ (para desenvolvimento frontend)
- Python 3.12+ (para desenvolvimento backend)

### Com Docker Compose (Recomendado)

```bash
# 1. Clone e entre no diretório
cd libras

# 2. Copy .env.example to .env
cp .env.example .env

# 3. Start all services
docker-compose up -d

# 4. Run migrations
docker-compose exec backend alembic upgrade head

# 5. Acesse a aplicação
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Sem Docker (Development)

#### Backend

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # ou: venv\Scripts\activate (Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp ../.env.example ../.env

# 5. Run migrations
alembic upgrade head

# 6. Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend

```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start dev server
npm run dev

# App will be at http://localhost:5173
```

## 📚 API Endpoints

### Health
- `GET /api/v1/health` - Health check

### Authentication
- `POST /api/v1/auth/signup` - Register user
- `POST /api/v1/auth/login` - Login user
- `GET /api/v1/auth/me` - Get current user

### Courses
- `GET /api/v1/courses` - List all courses
- `GET /api/v1/courses/{slug}` - Get course details
- `POST /api/v1/courses` - Create course (admin)
- `PUT /api/v1/courses/{id}` - Update course (admin)
- `DELETE /api/v1/courses/{id}` - Delete course (admin)

### Lessons
- `GET /api/v1/lessons` - List lessons
- `GET /api/v1/lessons/{slug}` - Get lesson details
- `POST /api/v1/lessons` - Create lesson (admin)

### Exercises
- `GET /api/v1/exercises` - List exercises
- `POST /api/v1/exercises` - Create exercise (admin)
- `POST /api/v1/exercises/{id}/answer` - Submit answer

### Progress
- `GET /api/v1/progress` - Get user progress
- `POST /api/v1/progress` - Update progress
- `GET /api/v1/progress/streak` - Get streak info

## 🗄️ Database Schema

### Core Tables
- **users** - User accounts
- **courses** - Educational courses
- **modules** - Course sections
- **lessons** - Individual lessons
- **lesson_steps** - Lesson content (videos, text, etc)
- **exercises** - Interactive exercises
- **exercise_options** - Exercise answer options
- **user_progress** - User lesson completion
- **user_streaks** - Daily learning streaks
- **subscriptions** - User subscriptions
- **payments** - Payment transactions

## 🔐 Security

- ✅ JWT authentication with secure tokens
- ✅ Bcrypt password hashing
- ✅ CORS configured by environment
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ XSS protection (React escaping)
- ✅ CSRF ready (token-based auth)
- ✅ Secrets in environment variables only

## 🧪 Testing

### Backend
```bash
cd backend
pytest
pytest --cov=app  # With coverage
```

### Frontend
```bash
cd frontend
npm run test
npm run test:coverage
```

## 📝 Environment Variables

Copy `.env.example` to `.env` and configure:

```env
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/libras_db

# Server
DEBUG=True
SECRET_KEY=your-secret-key
ALGORITHM=HS256

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:5173"]

# Redis
REDIS_URL=redis://localhost:6379

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLIC_KEY=pk_test_...

# AWS S3
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET=libras-videos
```

## 📦 Deployment

### Production Checklist
- [ ] Change `SECRET_KEY` to random value
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_ORIGINS`
- [ ] Setup PostgreSQL backup strategy
- [ ] Configure Redis persistence
- [ ] Setup monitoring/logging
- [ ] Configure SSL/TLS
- [ ] Setup CI/CD pipeline
- [ ] Configure email service
- [ ] Test payment integration

### Deploy to Heroku/Railway/Render
```bash
# Push docker image to registry
docker build -t libras-app .
docker push your-registry/libras-app
```

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] Fase 1: MVP com curso básico (✅ Em andamento)
- [ ] Fase 2: Exercícios e progresso
- [ ] Fase 3: Streak e gamificação
- [ ] Fase 4: Paywall e assinatura
- [ ] Fase 5: CMS completo
- [ ] Fase 6: Push notifications
- [ ] Fase 7: Analytics
- [ ] Fase 8: Conteúdo avançado
- [ ] Fase 9: Certificados
- [ ] Fase 10: IA/câmera para correção

## 📄 License

MIT License - see LICENSE file

## 🙏 Acknowledgments

- LIBRAS community and deaf educators
- Inspired by Duolingo, Babbel, Lingvano
- Special thanks to contributors

## 📧 Contact

- Email: arrumadosvmodas@gmail.com
- GitHub Issues: Report bugs and feature requests

---

**Made with ❤️ for the LIBRAS community**
