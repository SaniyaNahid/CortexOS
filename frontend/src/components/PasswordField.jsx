import { useState } from "react";

function PasswordField({
  label,
  placeholder,
  value,
  onChange,
}) {

  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="input-group">

      <label>{label}</label>

      <div className="password-container">

        <input
          type={showPassword ? "text" : "password"}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
        />

        <button
          type="button"
          onClick={() => setShowPassword(!showPassword)}
        >
          {showPassword ? "Hide" : "Show"}
        </button>

      </div>

    </div>
  );
}

export default PasswordField;