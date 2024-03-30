document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
  
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
  
      const email = document.getElementById('login-email').value;
      const password = document.getElementById('login-password').value;
  
      try {
        const response = await fetch('http://localhost:8000/auth/token', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });
  
        if (response.ok) {
          const data = await response.json();
          console.log('Login Successful', data);
          // Store the token and redirect to the dashboard
        } else {
          console.error('Login Failed');
        }
      } catch (error) {
        console.error('Network error', error);
      }
    });
  });
  