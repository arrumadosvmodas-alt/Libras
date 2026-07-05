import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import { apiClient } from '../lib/api';
import HomePage from '../features/home/HomePage';
import LoginPage from '../features/auth/LoginPage';
import SignupPage from '../features/auth/SignupPage';
import CoursesPage from '../features/courses/CoursesPage';
import CoursePage from '../features/courses/CoursePage';
import LessonPage from '../features/lessons/LessonPage';
import './App.css';

export default function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check API health and user authentication
    const checkAuth = async () => {
      try {
        await apiClient.healthCheck();
        const token = localStorage.getItem('access_token');
        setIsAuthenticated(!!token);
      } catch (error) {
        console.error('API health check failed:', error);
      } finally {
        setIsLoading(false);
      }
    };

    checkAuth();
  }, []);

  if (isLoading) {
    return (
      <div className="loading-container">
        <div className="loader"></div>
        <p>Carregando LIBRAS App...</p>
      </div>
    );
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/cursos" element={<CoursesPage />} />
        <Route path="/cursos/:slug" element={<CoursePage />} />
        <Route path="/licoes/:slug" element={<LessonPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
