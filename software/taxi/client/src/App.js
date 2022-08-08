import React, { useState } from 'react';
import { Route, Routes } from 'react-router-dom';
// Components
import Landing from './components/landing/Landing';
import LogIn from './components/login/Login';
import SignUp from './components/signup/SignUp';
import Layout from './components/layout/Layout';

import './App.css';

// changed
function App () {

  const [isLoggedIn, setLoggedIn] = useState(false);
  const logIn = (username, password) => setLoggedIn(true);

  return (
    <Routes>
    <Route path='/' element={<Layout isLoggedIn={isLoggedIn}/>}>
      <Route index element={<Landing />} />
      <Route path='sign-up' element={<SignUp />} />
      <Route path='log-in' element={<LogIn logIn={logIn} />} />
    </Route>
  </Routes>
  );
}

export default App;
