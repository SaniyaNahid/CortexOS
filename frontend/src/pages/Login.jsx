import { Link } from "react-router-dom";
import LoginForm from "../components/LoginForm";
import "../styles/Login.css";

function Login() {
  return (
    <div className="login-page">

      <div className="login-card">

        <h1>CortexOS-AI</h1>

        <h2>Welcome Back</h2>

        <p>
          Login to access your enterprise knowledge platform.
        </p>

        <LoginForm />

        <div className="back-home">
          <Link to="/">← Back to Home</Link>
        </div>

      </div>

    </div>
  );
}

export default Login;