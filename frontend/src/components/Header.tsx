import { Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import './Header.css';

export default function Header() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    setIsAuthenticated(!!token);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setIsAuthenticated(false);
    navigate('/');
  };

  return (
    <header className="header">
      <div className="header-container">
        <Link to="/" className="header-logo">
          📚 LIBRAS App
        </Link>

        <nav className={`header-nav ${isMobileMenuOpen ? 'active' : ''}`}>
          <Link to="/" className="nav-link">Início</Link>
          <Link to="/cursos" className="nav-link">Cursos</Link>

          {isAuthenticated ? (
            <>
              <Link to="/progresso" className="nav-link">Meu Progresso</Link>
              <button onClick={handleLogout} className="btn btn-outline">
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="nav-link">Login</Link>
              <Link to="/signup" className="btn btn-primary">
                Registrar
              </Link>
            </>
          )}
        </nav>

        <button
          className="header-menu-toggle"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        >
          ☰
        </button>
      </div>
    </header>
  );
}
