import React, { useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

function Volunteer() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    message: '',
  });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:3000/api/volunteer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          phoneNumber: formData.phone,
          reason: formData.message,
        }),
      });
      const data = await response.json();
      console.log(data); // log the response for debugging
      setSubmitted(true);
      // Reset form fields after successful submission
      setFormData({
        name: '',
        email: '',
        phone: '',
        message: '',
      });
    } catch (error) {
      console.error('Error:', error);
      // Handle errors if needed
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div>
      <Header />
      <div className='bg-gray-100'>
        {/* Volunteering Form */}
        <div className="max-w-md mx-auto p-4 bg-white relative top-5">
          <h2 className="text-4xl font-bold text-center text-blue-900 mb-5">Volunteer Form</h2>
          <form onSubmit={handleSubmit}>
            <label htmlFor="name">Name:</label>
            <input className='required' type="text" id="name" name="name" value={formData.name} onChange={handleChange} required />

            <label htmlFor="email">Email:</label>
            <input className='required' type="email" id="email" name="email" value={formData.email} onChange={handleChange} required />

            <label htmlFor="phone" >Phone:</label>
            <input className='required' type="tel" id="phone" name="phone" value={formData.phone} onChange={handleChange} required />

            <label htmlFor="message">Why do you want to volunteer?</label>
            <textarea id="message" name="message" rows="4" value={formData.message} onChange={handleChange} required></textarea>

            <button className=' relative left-36 mt-2' id='vol-btn' type="submit">Submit</button>
          </form>
          {submitted && (
            <div className="bg-green-200 text-green-800 p-2 mt-4 text-center">
              Thanks for volunteering!
            </div>
          )}
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Volunteer;
