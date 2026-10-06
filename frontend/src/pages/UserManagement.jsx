import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/UserManagement.css";


function UserManagement() {

  const users = [
    {
      name: "Likitha",
      role: "Admin",
      status: "Active"
    },
    {
      name: "Rahul",
      role: "Project Manager",
      status: "Active"
    },
    {
      name: "Anjali",
      role: "Employee",
      status: "Active"
    }
  ];


  return (
    <DashboardLayout>

      <h1>
        User Management
      </h1>

      <p>
        Manage users, roles and permissions.
      </p>


      <div className="users-table">


        <div className="table-header">

          <span>Name</span>
          <span>Role</span>
          <span>Status</span>

        </div>



        {
          users.map((user,index)=>(

            <div 
              className="user-row"
              key={index}
            >

              <span>
                {user.name}
              </span>


              <span>
                {user.role}
              </span>


              <span className="active">

                {user.status}

              </span>


            </div>

          ))
        }


      </div>


    </DashboardLayout>
  );
}


export default UserManagement;