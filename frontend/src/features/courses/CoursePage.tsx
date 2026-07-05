import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import Header from '../../components/Header';
import { apiClient } from '../../lib/api';
import { Course } from '../../types';

export default function CoursePage() {
  const { slug } = useParams<{ slug: string }>();
  const [course, setCourse] = useState<Course | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchCourse = async () => {
      if (!slug) return;

      try {
        const data = await apiClient.getCourse(slug);
        setCourse(data);
      } catch (err) {
        setError('Erro ao carregar curso. Tente novamente.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchCourse();
  }, [slug]);

  if (loading) {
    return (
      <>
        <Header />
        <div style={{ padding: '2rem', textAlign: 'center' }}>
          Carregando curso...
        </div>
      </>
    );
  }

  if (error || !course) {
    return (
      <>
        <Header />
        <div style={{ padding: '2rem', textAlign: 'center' }}>
          <p>{error || 'Curso não encontrado'}</p>
          <Link to="/cursos" className="btn btn-primary">
            Voltar para Cursos
          </Link>
        </div>
      </>
    );
  }

  return (
    <>
      <Header />
      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        <h1>{course.title}</h1>
        <p>{course.description}</p>

        <div style={{ marginTop: '2rem' }}>
          <h2>Módulos</h2>
          {course.modules.length === 0 ? (
            <p>Nenhum módulo disponível ainda.</p>
          ) : (
            course.modules.map((module) => (
              <div key={module.id} style={{ marginBottom: '2rem', padding: '1.5rem', background: 'white', borderRadius: '0.5rem', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
                <h3>{module.title}</h3>
                <p>{module.description}</p>
                <div style={{ marginTop: '1rem' }}>
                  {module.lessons.map((lesson) => (
                    <div key={lesson.id} style={{ marginBottom: '1rem', padding: '1rem', background: '#f9fafb', borderRadius: '0.375rem' }}>
                      <Link to={`/licoes/${lesson.slug}`} style={{ color: '#6366f1', textDecoration: 'none', fontWeight: 500 }}>
                        {lesson.title}
                      </Link>
                      <p style={{ fontSize: '0.875rem', color: '#6b7280', marginTop: '0.25rem' }}>
                        {lesson.duration_minutes} minutos • {lesson.difficulty}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            ))
          )}
        </div>
      </main>
    </>
  );
}
