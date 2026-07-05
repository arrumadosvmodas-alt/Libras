import Header from '../../components/Header';
import { Link } from 'react-router-dom';

export default function LessonPage() {
  return (
    <>
      <Header />
      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem' }}>
        <h1>Página de Lição</h1>
        <p>Esta é a página onde os usuários assistem às videoaulas e fazem exercícios.</p>

        <div style={{ marginTop: '2rem', padding: '2rem', background: 'white', borderRadius: '0.75rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
          <h2>Vídeo da Lição</h2>
          <div style={{ background: '#000', height: '400px', borderRadius: '0.5rem', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'white' }}>
            [Video player aqui]
          </div>
        </div>

        <div style={{ marginTop: '2rem', padding: '2rem', background: 'white', borderRadius: '0.75rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
          <h2>Exercício</h2>
          <p>Próximas aulas incluirão exercícios interativos.</p>
        </div>

        <div style={{ marginTop: '2rem' }}>
          <Link to="/cursos" className="btn btn-primary">
            Voltar aos Cursos
          </Link>
        </div>
      </main>
    </>
  );
}
