import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom'
import Layout from './Layout'
import Home from './Pages/Home'
import About from './Pages/About'
import Volunteer from './Pages/Volunteer'
import Event from './Pages/Event'
// import Donate from './Pages/Donate'
import Contact from './Pages/Contact'
import SignIn from './components/SignIn'
import SignUp from './components/SignUp'
import PostJob from './Pages/PostJob'
import Portal from './Pages/Portal'
import ChatBox from './Pages/ChatBox'
import PrivacyPolicy from './Pages/PrivacyPolicy'
import TermsAndConditions from './Pages/TermsAndConditions'
// import Example from './Pages/Example'
import { BrowserRouter, Routes } from 'react-router-dom'



const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/dashboard" element={<Home />} />
        {/* <Route path="/about" element={<About />} /> */}
        {/* <Route path="/volunteer" element={<Volunteer />} /> */}
        {/* <Route path="/event" element={<Event />} /> */}
        {/* <Route path="/donate" element={<Donate/>}/> */}
        {/* <Route path="/contact" element={<Contact />} /> */}
        {/* <Route path="/portal" element={<Portal />} /> */}
        <Route path="/" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        {/* <Route path="/example" element={<Example />} /> */}
      </Routes>
    </BrowserRouter>
  )

}
export default App


