import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Header from '../../components/Header';
import { apiClient } from '../../lib/api';
import { Course } from '../../types';
import './CoursesPage.css';

export default function CoursesPage() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const data = await apiClient.getCourses();
        setCourses(data);
      } catch (err) {
        setError('Erro ao carregar cursos. Tente novamente.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  return (
    <>
      <Header />
      <main className="courses-page">
        <div className="page-header">
          <h1>Nossos Cursos</h1>
          <p>Escolha um curso e comece a aprender LIBRAS</p>
        </div>

        {loading && <div className="loading">Carregando cursos...</div>}

        {error && <div className="error-message">{error}</div>}

        {!loading && courses.length === 0 && (
          <div className="empty-state">
            <p>Nenhum curso disponível no momento.</p>
            <Link to="/" className="btn btn-primary">
              Voltar para Início
            </Link>
          </div>
        )}

        {!loading && courses.length > 0 && (
          <div className="courses-container">
            <div className="courses-grid">
              {courses.map((course) => (
                <Link
                  key={course.id}
                  to={`/cursos/${course.slug}`}
                  className="course-card"
                >
                  <div className="course-thumbnail">
                    {course.thumbnail_url ? (
                      <img
                        src={course.thumbnail_url}
                        alt={course.title}
                      />
                    ) : (
                      <div className="placeholder">📚</div>
                    )}
                  </div>
                  <div className="course-content">
                    <h3>{course.title}</h3>
                    <p className="course-description">
                      {course.description || 'Sem descrição'}
                    </p>
                    <div className="course-meta">
                      <span className="badge">{course.difficulty}</span>
                      <span className="lesson-count">
                        {course.modules.length} módulos
                      </span>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        )}
      </main>
    </>
  );
}
