import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import Header from '../../components/Header';
import { apiClient } from '../../lib/api';
import './AuthPage.css';

export default function SignupPage() {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirm, setPasswordConfirm] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (password !== passwordConfirm) {
      setError('As senhas não coincidem.');
      return;
    }

    if (password.length < 6) {
      setError('A senha deve ter pelo menos 6 caracteres.');
      return;
    }

    setLoading(true);

    try {
      await apiClient.signup({
        email,
        full_name: fullName,
        password,
      });
      navigate('/cursos');
    } catch (err: any) {
      setError(
        err.response?.data?.detail || 'Erro ao registrar. Tente novamente.'
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Header />
      <main className="auth-page">
        <div className="auth-container">
          <div className="auth-card">
            <h1>Registrar</h1>
            <p className="auth-subtitle">Comece a aprender LIBRAS hoje!</p>

            {error && <div className="error-message">{error}</div>}

            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="fullName">Nome Completo</label>
                <input
                  id="fullName"
                  type="text"
                  placeholder="Seu nome completo"
                  value={fullName}
                  onChange={(e) => setFullName(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>

              <div className="form-group">
                <label htmlFor="email">Email</label>
                <input
                  id="email"
                  type="email"
                  placeholder="seu@email.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>

              <div className="form-group">
                <label htmlFor="password">Senha</label>
                <input
                  id="password"
                  type="password"
                  placeholder="Crie uma senha"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>

              <div className="form-group">
                <label htmlFor="passwordConfirm">Confirmar Senha</label>
                <input
                  id="passwordConfirm"
                  type="password"
                  placeholder="Confirme sua senha"
                  value={passwordConfirm}
                  onChange={(e) => setPasswordConfirm(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>

              <button
                type="submit"
                className="btn btn-primary"
                disabled={loading}
                style={{ width: '100%' }}
              >
                {loading ? 'Criando conta...' : 'Registrar'}
              </button>
            </form>

            <p className="auth-footer">
              Já tem conta? <Link to="/login">Login aqui</Link>
            </p>
          </div>
        </div>
      </main>
    </>
  );
}
