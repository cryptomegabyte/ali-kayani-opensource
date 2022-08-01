import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter, Route, Routes } from 'react-router-dom';
import './index.css';
import App from './App';

import Landing from './components/landing/Landing';
import LogIn from './components/login/Login';
import SignUp from './components/signup/SignUp';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <HashRouter>
      <Routes>
        <Route path='/' element={<App />} />
        {/* new begin */}
        <Route index element={<Landing />} />
        <Route path='sign-up' element={<SignUp />} />
        <Route path='log-in' element={<LogIn />} />
        {/* new end */}
      </Routes>
    </HashRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();