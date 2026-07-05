/**
 * Type definitions for the LIBRAS App
 */

export interface User {
  id: number;
  email: string;
  full_name: string;
  is_active: boolean;
  role: 'student' | 'instructor' | 'admin';
  created_at: string;
  updated_at: string;
}

export interface Course {
  id: number;
  title: string;
  slug: string;
  description?: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  thumbnail_url?: string;
  order_index: number;
  is_published: boolean;
  modules: Module[];
  created_at: string;
  updated_at: string;
}

export interface Module {
  id: number;
  course_id: number;
  title: string;
  slug: string;
  description?: string;
  order_index: number;
  is_published: boolean;
  lessons: Lesson[];
  created_at: string;
  updated_at: string;
}

export interface Lesson {
  id: number;
  module_id: number;
  title: string;
  slug: string;
  description?: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  duration_minutes: number;
  order_index: number;
  is_published: boolean;
  steps: LessonStep[];
  created_at: string;
  updated_at: string;
}

export interface LessonStep {
  id: number;
  title: string;
  content_type: 'video' | 'text' | 'image' | 'sign';
  content_url?: string;
  description?: string;
  order_index: number;
}

export interface Exercise {
  id: number;
  lesson_id: number;
  exercise_type: string;
  question: string;
  explanation?: string;
  order_index: number;
  points: number;
  options: ExerciseOption[];
  created_at: string;
  updated_at: string;
}

export interface ExerciseOption {
  id: number;
  text: string;
  image_url?: string;
  video_url?: string;
  is_correct: boolean;
  order_index: number;
}

export interface UserProgress {
  id: number;
  user_id: number;
  lesson_id: number;
  score: number;
  is_completed: boolean;
  completed_at?: string;
  created_at: string;
  updated_at: string;
}

export interface UserStreak {
  id: number;
  user_id: number;
  current_streak: number;
  longest_streak: number;
  last_activity_date?: string;
  created_at: string;
  updated_at: string;
}

export interface AuthToken {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface SignupData {
  email: string;
  full_name: string;
  password: string;
}
