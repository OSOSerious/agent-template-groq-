import { writable } from 'svelte/store';
import { API_BASE_URL } from '../config';

interface AuthState {
    isAuthenticated: boolean;
    token: string | null;
    user: {
        id: string;
        email: string;
        username: string;
    } | null;
}

const createAuthStore = () => {
    // Initialize from localStorage if available
    const storedToken = localStorage.getItem('token');
    const storedUser = localStorage.getItem('user');
    
    const initialState: AuthState = {
        isAuthenticated: !!storedToken,
        token: storedToken,
        user: storedUser ? JSON.parse(storedUser) : null
    };

    const { subscribe, set, update } = writable<AuthState>(initialState);

    return {
        subscribe,
        login: async (email: string, password: string) => {
            try {
                const response = await fetch(`${API_BASE_URL}/token`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({
                        'username': email,
                        'password': password,
                    }).toString(),
                    credentials: 'same-origin'
                });

                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || 'Login failed');
                }

                const data = await response.json();
                
                // Store in localStorage
                localStorage.setItem('token', data.access_token);
                
                // Update store
                update(state => ({
                    ...state,
                    isAuthenticated: true,
                    token: data.access_token
                }));

                return true;
            } catch (error) {
                console.error('Login error:', error);
                throw error;
            }
        },
        register: async (email: string, username: string, password: string) => {
            try {
                const response = await fetch(`${API_BASE_URL}/register`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email, username, password }),
                    credentials: 'same-origin'
                });

                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || 'Registration failed');
                }

                return true;
            } catch (error) {
                console.error('Registration error:', error);
                throw error;
            }
        },
        logout: () => {
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            set({
                isAuthenticated: false,
                token: null,
                user: null
            });
        }
    };
};

export const authStore = createAuthStore();
