import { Link, useNavigate } from "react-router-dom";

import {
  MdDashboard,
  MdDescription,
  MdAnalytics,
  MdGroups,
  MdSettings,
} from "react-icons/md";

import {
  FiUpload,
  FiLogOut,
  FiUser,
} from "react-icons/fi";

import { BsRobot } from "react-icons/bs";


function Sidebar({ isOpen }) {

  const navigate = useNavigate();


  const handleLogout = () => {

    // remove login data (frontend)
    localStorage.removeItem("isLoggedIn");

    // redirect to login page
    navigate("/login");

  };


  return (
    <aside className={`sidebar ${isOpen ? "" : "collapsed"}`}>


      <div className="logo">

        <h2>CortexOS</h2>

        <p>
          AI Intelligence Platform
        </p>

      </div>


      <nav>

        <Link to="/dashboard">
          <MdDashboard />
          <span>Dashboard</span>
        </Link>


        <Link to="/documents">
          <MdDescription />
          <span>Knowledge Base</span>
        </Link>


        <Link to="/upload">
          <FiUpload />
          <span>Upload Documents</span>
        </Link>


        <Link to="/chat">
          <BsRobot />
          <span>AI Assistant</span>
        </Link>


        <Link to="/analytics">
          <MdAnalytics />
          <span>Analytics</span>
        </Link>


        <Link to="/users">
          <MdGroups />
          <span>User Management</span>
        </Link>


        <Link to="/settings">
          <MdSettings />
          <span>Settings</span>
        </Link>


        <Link to="/profile">
          <FiUser />
          <span>Profile</span>
        </Link>


      </nav>



      <div className="logout">

        <button 
          onClick={handleLogout}
          className="logout-btn"
        >

          <FiLogOut />

          <span>
            Logout
          </span>

        </button>

      </div>


    </aside>
  );
}


export default Sidebar;