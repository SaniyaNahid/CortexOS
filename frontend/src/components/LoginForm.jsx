import { useState } from "react";
import { useNavigate } from "react-router-dom";

import InputField from "./InputField";
import PasswordField from "./PasswordField";


function LoginForm() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");

  const navigate = useNavigate();



  const handleLogin = (e) => {

    e.preventDefault();


    // Validation

    if (!email || !password) {

      setError("Please enter email and password");

      return;

    }


    setError("");


    console.log({
      email,
      password,
    });



    // Temporary login session

    localStorage.setItem(
      "isLoggedIn",
      "true"
    );


    navigate("/dashboard");

  };



  return (
    <form onSubmit={handleLogin}>


      {
        error && (
          <p className="login-error">
            {error}
          </p>
        )
      }



      <InputField
        label="Email Address"
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />



      <PasswordField
        label="Password"
        placeholder="Enter your password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />



      <button type="submit">
        Login
      </button>


    </form>
  );
}


export default LoginForm;