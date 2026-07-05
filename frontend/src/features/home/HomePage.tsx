import { Link } from 'react-router-dom';
import Header from '../../components/Header';
import './HomePage.css';

export default function HomePage() {
  return (
    <>
      <Header />
      <main className="home-page">
        {/* Hero Section */}
        <section className="hero">
          <div className="hero-content">
            <h1>Aprenda LIBRAS com Aulas Curtas e Divertidas</h1>
            <p>
              Descubra a beleza da Língua Brasileira de Sinais com videoaulas
              de professores surdos, exercícios interativos e uma comunidade
              acolhedora.
            </p>
            <div className="hero-buttons">
              <Link to="/cursos" className="btn btn-primary">
                Começar Agora
              </Link>
              <Link to="#sobre" className="btn btn-outline">
                Saiba Mais
              </Link>
            </div>
          </div>
          <div className="hero-image">
            <div className="placeholder-image">🤟</div>
          </div>
        </section>

        {/* Features Section */}
        <section className="features" id="sobre">
          <h2>Por que escolher LIBRAS App?</h2>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">📺</div>
              <h3>Videoaulas Curtas</h3>
              <p>Aprenda em 5-10 minutos com vídeos de alta qualidade.</p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">👨‍🏫</div>
              <h3>Professores Surdos</h3>
              <p>Aprenda com nativos da comunidade surda brasileira.</p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">🎯</div>
              <h3>Exercícios Interativos</h3>
              <p>Pratique através de desafios divertidos e educativos.</p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">🔥</div>
              <h3>Streak Diário</h3>
              <p>Mantenha sua sequência de aprendizado e ganhe recompensas.</p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">📊</div>
              <h3>Progresso Rastreado</h3>
              <p>Acompanhe seu progresso em tempo real.</p>
            </div>

            <div className="feature-card">
              <div className="feature-icon">📱</div>
              <h3>Disponível em Tudo</h3>
              <p>Use no celular, tablet ou computador quando quiser.</p>
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="cta">
          <h2>Pronto para começar sua jornada?</h2>
          <p>Junte-se a milhares de pessoas aprendendo LIBRAS.</p>
          <Link to="/signup" className="btn btn-primary btn-large">
            Registrar Gratuitamente
          </Link>
        </section>

        {/* Footer */}
        <footer className="footer">
          <div className="footer-content">
            <p>&copy; 2024 LIBRAS App. Todos os direitos reservados.</p>
            <p>Feito com ❤️ pela comunidade LIBRAS</p>
          </div>
        </footer>
      </main>
    </>
  );
}
