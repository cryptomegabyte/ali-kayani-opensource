import React, { useState } from "react";
import { Route, Routes } from "react-router-dom";
import axios from "axios";
// Components
import Landing from "./components/landing/Landing";
import LogIn from "./components/login/Login";
import SignUp from "./components/signup/SignUp";
import Layout from "./components/layout/Layout";
import Driver from "./components/driver/Driver";
import Rider from "./components/rider/Rider";

import "./App.css";

function App() {
  const [isLoggedIn, setLoggedIn] = useState(() => {
    return window.localStorage.getItem("taxi.auth") !== null;
  });

  const logIn = async (username, password) => {
    const url = `${process.env.REACT_APP_BASE_URL}/api/log_in/`;
    try {
      const response = await axios.post(url, { username, password });
      window.localStorage.setItem("taxi.auth", JSON.stringify(response.data));
      setLoggedIn(true);
      return { response, isError: false };
    } catch (error) {
      console.error(error);
      return { response: error, isError: true };
    }
  };

  const logOut = () => {
    window.localStorage.removeItem("taxi.auth");
    setLoggedIn(false);
  };

  return (
    <Routes>
      <Route
        path="/"
        element={<Layout isLoggedIn={isLoggedIn} logOut={logOut} />}
      >
        <Route index element={<Landing isLoggedIn={isLoggedIn} />} />
        <Route path="sign-up" element={<SignUp isLoggedIn={isLoggedIn} />} />
        <Route
          path="log-in"
          element={<LogIn isLoggedIn={isLoggedIn} logIn={logIn} />}
        />
      </Route>
      <Route path="rider" element={<Rider />} />
      <Route path="driver" element={<Driver />} />
    </Routes>
  );
}

export default App;
