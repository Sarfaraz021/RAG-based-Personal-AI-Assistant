document.addEventListener('DOMContentLoaded', () => {
    const signInForm = document.getElementById('sign-in-form');
  
    signInForm.addEventListener('submit', async (e) => {
      e.preventDefault();
  
      const email = document.getElementById('sign-in-email').value;
      const password = document.getElementById('sign-in-password').value;
  
      try {
        const response = await fetch('http://localhost:8000/auth/signup/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email, password })
        });
  
        if (response.ok) {
          console.log('Sign-In Successful');
          // Redirect to login page or dashboard
        } else {
          console.error('Sign-In Failed');
        }
      } catch (error) {
        console.error('Network error', error);
      }
    });
  });
  