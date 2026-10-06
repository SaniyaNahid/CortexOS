import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/Profile.css";


function Profile() {

  return (
    <DashboardLayout>

      <h1>
        Profile
      </h1>

      <p>
        Manage your personal information and account details.
      </p>


      <div className="profile-card">


        <div className="profile-avatar">
          👤
        </div>


        <h2>
          Likitha
        </h2>

        <p className="role">
          Admin
        </p>



        <div className="profile-details">


          <div>
            <strong>
              Email
            </strong>

            <p>
              likitha@example.com
            </p>
          </div>



          <div>
            <strong>
              Role
            </strong>

            <p>
              System Administrator
            </p>
          </div>



          <div>
            <strong>
              Joined
            </strong>

            <p>
              July 2026
            </p>
          </div>



          <div>
            <strong>
              Status
            </strong>

            <p className="status">
              Active ✅
            </p>
          </div>


        </div>


      </div>


    </DashboardLayout>
  );
}


export default Profile;