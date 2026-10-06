import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/Settings.css";


function Settings() {

  return (
    <DashboardLayout>

      <h1>
        Settings
      </h1>

      <p>
        Manage your account and system preferences.
      </p>


      <div className="settings-container">


        <div className="settings-card">

          <h2>
            Account Settings
          </h2>

          <label>
            Username
          </label>

          <input 
            type="text"
            value="Likitha"
            readOnly
          />


          <label>
            Email
          </label>

          <input
            type="email"
            value="likitha@example.com"
            readOnly
          />

        </div>



        <div className="settings-card">

          <h2>
            Security
          </h2>


          <button>
            Change Password
          </button>


          <button>
            Enable Two Factor Authentication
          </button>


        </div>



        <div className="settings-card">

          <h2>
            System Preferences
          </h2>


          <div className="setting-option">

            <span>
              Notifications
            </span>

            <input 
              type="checkbox"
              defaultChecked
            />

          </div>


          <div className="setting-option">

            <span>
              Dark Mode
            </span>

            <input 
              type="checkbox"
            />

          </div>


        </div>


      </div>


    </DashboardLayout>
  );
}


export default Settings;