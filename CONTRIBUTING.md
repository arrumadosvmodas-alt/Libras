# 🤝 Contributing to LIBRAS App

Thank you for your interest in contributing to LIBRAS App! This guide will help you get started.

## Code of Conduct

We are committed to creating an inclusive and respectful environment for everyone. By participating in this project, you agree to:

- Treat all people with respect and kindness
- Be patient with others learning
- Give credit where it's due
- Respect the LIBRAS community and deaf culture
- Report inappropriate behavior

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/libras.git
cd libras

# Add upstream
git remote add upstream https://github.com/original/libras.git
```

### 2. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bugfix branch
git checkout -b bugfix/issue-description
```

### 3. Follow Conventions

#### Commit Messages
```
[type]: Brief description

- Detailed explanation of changes
- Why this change is needed
- How it improves the project

Types: feat, fix, docs, style, refactor, test, chore
```

Example:
```
feat: add exercise difficulty levels

- Add difficulty enum to Exercise model
- Create migration for difficulty column
- Update API responses to include difficulty
```

#### Branch Names
```
feature/course-management
bugfix/login-validation
docs/api-documentation
chore/update-dependencies
```

## Development Guidelines

### Python/Backend

#### Code Style
```bash
# Format code with Black
black app/

# Lint with Ruff
ruff check app/

# Type check with mypy
mypy app/

# Or all at once
black app/ && ruff check app/ && mypy app/
```

#### Writing Tests
```python
# tests/test_courses.py
import pytest
from app.models.course import Course

def test_create_course(db):
    """Test course creation"""
    course = Course(
        title="Test Course",
        slug="test-course",
        description="A test course"
    )
    db.add(course)
    db.commit()
    
    assert course.id is not None
    assert course.title == "Test Course"

def test_course_validation(db):
    """Test course slug validation"""
    # Invalid slug with uppercase
    course = Course(
        title="Test",
        slug="Test-Course"  # Should be lowercase
    )
    # Would fail validation
```

### TypeScript/Frontend

#### Code Style
```bash
# Format with Prettier
npx prettier --write src/

# Lint with ESLint
npm run lint

# Type check
npm run type-check
```

#### Component Guidelines
```typescript
// Use functional components with hooks
import { useState, useEffect } from 'react';

interface Props {
  courseId: number;
  onComplete?: (progress: number) => void;
}

export default function CourseCard({ courseId, onComplete }: Props) {
  const [course, setCourse] = useState(null);
  
  useEffect(() => {
    // Fetch course data
  }, [courseId]);
  
  return (
    <div className="course-card">
      {/* Component JSX */}
    </div>
  );
}
```

## Contribution Types

### 🐛 Bug Reports

Found a bug? Please report it!

```markdown
# Bug: Login form doesn't validate email

## Description
When entering an invalid email, the form allows submission.

## Steps to Reproduce
1. Go to login page
2. Enter "invalid-email"
3. Click login

## Expected Behavior
Form should show validation error

## Actual Behavior
Form submits with invalid email

## Environment
- Browser: Chrome 120
- OS: Windows 11
- Version: 0.1.0
```

### 💡 Feature Requests

Have a great idea? Share it!

```markdown
# Feature: Dark mode support

## Problem
The app only has a light theme, which is hard on the eyes at night.

## Solution
Add a toggle to switch between light and dark themes.

## Implementation
- Add dark theme CSS variables
- Create theme toggle in header
- Save preference to localStorage

## Additional Context
Similar to Duolingo's dark mode implementation.
```

### 📚 Documentation

Help improve documentation!

- Fix typos
- Clarify confusing sections
- Add examples
- Update outdated information

```bash
# Edit markdown files
# Create PR with changes
```

### ♻️ Code Improvements

Help improve code quality:

- Refactor inefficient code
- Improve type safety
- Add missing error handling
- Simplify complex logic

## Pull Request Process

### 1. Prepare Your Changes

```bash
# Update your branch with latest code
git fetch upstream
git rebase upstream/main

# Run tests
cd backend && pytest
cd ../frontend && npm test

# Fix any issues
```

### 2. Create Pull Request

```bash
# Push your branch
git push origin feature/your-feature-name

# Create PR on GitHub with description
```

### 3. PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation update
- [ ] Code refactor
- [ ] Dependency update

## Related Issues
Fixes #123
Related to #456

## Changes
- Changed X
- Added Y
- Removed Z

## Testing
- [ ] Added/updated tests
- [ ] All tests pass
- [ ] Tested in browser/manually

## Screenshots (if UI changes)
[Add screenshots here]

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code (where necessary)
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests
- [ ] New and existing tests pass
```

### 4. Code Review

- Address feedback constructively
- Ask questions if unclear
- Be patient with the review process
- Update branch as requested

## Project Structure for Contributors

```
Issues to Work On:
├── good first issue  (Start here!)
├── help wanted
├── bug
├── enhancement
└── documentation

Labels:
- priority/critical
- priority/high
- priority/low
- difficulty/beginner
- difficulty/advanced
```

## Development Tips

### Debugging

#### Backend
```python
# Use ipdb for debugging
import ipdb; ipdb.set_trace()

# Or use print for quick debugging
print(f"DEBUG: {variable}")
```

#### Frontend
```typescript
// Use console logging
console.log('debug:', data);

// Use browser DevTools
// F12 -> Console, Network, Elements
```

### Performance Profiling

#### Backend
```bash
# Profile with cProfile
python -m cProfile -s cumulative app/main.py
```

#### Frontend
```bash
# Use React DevTools Chrome extension
# Record performance in DevTools
```

## Community

- 💬 Discussions: GitHub Discussions
- 🐦 Twitter: [@librasapp](https://twitter.com)
- 📧 Email: arrumadosvmodas@gmail.com
- 📱 Discord: [Join our server]

## Recognition

Contributors are recognized:
- In README.md
- In release notes
- In project acknowledgments

## Questions?

- Check existing issues and PRs
- Read documentation (README.md, SETUP.md, ARCHITECTURE.md)
- Ask in GitHub Discussions
- Contact maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making LIBRAS App better! 🙏**
