---
name: libras-app-builder
description: Build and maintain a production-ready educational LIBRAS app using FastAPI, PostgreSQL, Docker, React and TypeScript.
---

# LIBRAS App Builder

Use this skill when the user asks to create, evolve, refactor, test or document an application about LIBRAS, the Brazilian Sign Language.

## Main objective

Build a production-ready educational app for LIBRAS with:

- React + TypeScript frontend
- FastAPI backend
- PostgreSQL database
- Docker and Docker Compose
- Clean architecture
- REST API
- Authentication-ready structure
- Admin-ready content model
- Accessibility-first UI
- Testable and maintainable code

## Important domain rules

LIBRAS is a real language used by the Brazilian deaf community.

When generating app content:

- Do not invent signs as if they were official.
- Do not claim a sign is correct unless the source is explicit.
- Prefer placeholder content when no validated data source is provided.
- Always recommend validation by qualified LIBRAS instructors or deaf community reviewers.
- Avoid treating LIBRAS as a word-for-word translation of Portuguese.
- Include support for video, image, textual explanation and usage context.
- Prioritize accessibility, visual clarity, keyboard navigation and mobile usability.

## Recommended product scope

The initial MVP should include:

1. Public home page
2. Sign dictionary
3. Categories
4. Alphabet module
5. Basic lessons
6. Quiz module
7. User progress model
8. Admin-ready CRUD structure
9. Media support for sign videos/images
10. Seed data with placeholders only

## Architecture

Use this structure unless the user asks otherwise:

```txt
backend/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       └── endpoints/
│   └── tests/
├── alembic/
├── pyproject.toml
└── Dockerfile

frontend/
├── src/
│   ├── app/
│   ├── components/
│   ├── features/
│   │   ├── signs/
│   │   ├── lessons/
│   │   ├── quiz/
│   │   └── progress/
│   ├── lib/
│   ├── services/
│   ├── types/
│   └── main.tsx
├── package.json
└── Dockerfile
```

## Backend requirements

Use:

- Python 3.12+
- FastAPI
- SQLAlchemy 2.x
- Pydantic v2
- PostgreSQL
- Alembic
- pytest
- httpx
- python-dotenv or pydantic-settings

Create models for:

- Sign
- Category
- Lesson
- LessonItem
- QuizQuestion
- UserProgress

Recommended database fields:

Sign:

- id
- slug
- term_pt
- gloss
- description
- handshape
- movement
- location
- facial_expression
- category_id
- difficulty
- video_url
- image_url
- source_url
- verification_status
- created_at
- updated_at

Category:

- id
- name
- slug
- description

Lesson:

- id
- title
- slug
- description
- difficulty
- order_index

LessonItem:

- id
- lesson_id
- sign_id
- order_index
- notes

QuizQuestion:

- id
- sign_id
- question
- options
- correct_answer
- explanation

UserProgress:

- id
- user_id nullable initially
- lesson_id
- completed
- score
- updated_at

## API endpoints

Create REST endpoints:

```txt
GET    /api/v1/health
GET    /api/v1/categories
POST   /api/v1/categories
GET    /api/v1/signs
POST   /api/v1/signs
GET    /api/v1/signs/{slug}
PUT    /api/v1/signs/{id}
DELETE /api/v1/signs/{id}
GET    /api/v1/lessons
GET    /api/v1/lessons/{slug}
GET    /api/v1/quiz
POST   /api/v1/quiz/answer
GET    /api/v1/progress
POST   /api/v1/progress
```

Use pagination, filtering by category, difficulty and search term for signs.

## Frontend requirements

Use:

- React
- TypeScript
- Vite
- React Router
- TanStack Query
- Zod where useful
- Accessible components
- Responsive layout

Pages:

```txt
/
/dicionario
/dicionario/:slug
/aulas
/aulas/:slug
/quiz
/progresso
/admin/sinais
```

Frontend rules:

- Use semantic HTML.
- Use accessible buttons, labels and focus states.
- Avoid relying only on color.
- Support video playback for signs.
- Show placeholder media clearly when no real video exists.
- Keep components small and reusable.
- Use typed API clients.

## Docker requirements

Create:

- docker-compose.yml
- backend Dockerfile
- frontend Dockerfile
- PostgreSQL service
- development-ready volumes
- environment variables through .env.example

Services:

```txt
postgres
backend
frontend
```

## Security requirements

- Validate all request payloads.
- Never trust client input.
- Use CORS configured by environment variable.
- Do not hardcode secrets.
- Prepare structure for future JWT authentication.
- Avoid exposing stack traces in production.
- Keep admin endpoints easy to protect later.

## Testing requirements

Backend:

- health endpoint test
- signs listing test
- sign creation test
- category creation test

Frontend:

- render home page
- render dictionary page
- API client typing where useful

## Output style

When generating code:

1. Explain the strategy briefly.
2. Show the file path.
3. Provide complete file content.
4. Avoid partial snippets unless explicitly requested.
5. Include commands to run the app.
6. Include tests when relevant.
7. Prefer simple maintainable architecture over overengineering.

## Default implementation command

When the user asks to start the project, generate the project in phases:

Phase 1:

- Docker Compose
- Backend base
- Database config
- Health endpoint

Phase 2:

- SQLAlchemy models
- Alembic migrations
- CRUD endpoints

Phase 3:

- Frontend base
- Routing
- Dictionary UI
- Lesson UI

Phase 4:

- Quiz
- Progress
- Admin-ready screens

Phase 5:

- Tests
- README
- Hardening checklist

## Example user requests that should trigger this skill

- Create a LIBRAS app
- Build a Brazilian Sign Language learning app
- Add dictionary feature for LIBRAS
- Add lessons to my LIBRAS project
- Generate FastAPI backend for LIBRAS signs
- Create React frontend for sign language learning
- Refactor my LIBRAS app architecture
