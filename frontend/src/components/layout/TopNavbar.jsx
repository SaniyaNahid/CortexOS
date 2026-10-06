import { FiBell, FiUser, FiMenu } from "react-icons/fi";

function TopNavbar({ toggleSidebar }) {
  return (
    <header className="top-navbar">

      <div className="navbar-left">

        <button
          className="menu-btn"
          onClick={toggleSidebar}
        >
          <FiMenu />
        </button>


        <div className="navbar-title">

          <h2>
            CortexOS Dashboard
          </h2>

          <p>
            AI-Powered Enterprise Intelligence Platform
          </p>

        </div>

      </div>



      <div className="navbar-actions">


        <button className="icon-button">
          <FiBell />
        </button>



       <div className="user-profile">

  <FiUser />

  <div>
    <span>
      Likitha
    </span>

    <small>
      (Admin)
    </small>
  </div>

</div>


      </div>


    </header>
  );
}

export default TopNavbar;