import DashboardLayout from "../components/layout/DashboardLayout";
import DashboardCard from "../components/DashboardCard";
import "../styles/Dashboard.css";

import {
  MdDescription,
  MdPeople,
  MdSearch,
  MdStorage
} from "react-icons/md";


function Dashboard() {

  return (
    <DashboardLayout>

      <h1>
        Welcome back, Likitha 👋
      </h1>

      <p>
        AI-Powered Enterprise Intelligence and Decision Support System
      </p>


      <div className="dashboard-cards">

        <DashboardCard
          title="Documents"
          value="120"
          icon={<MdDescription />}
        />


        <DashboardCard
          title="AI Queries"
          value="540"
          icon={<MdSearch />}
        />


        <DashboardCard
          title="Active Users"
          value="25"
          icon={<MdPeople />}
        />


        <DashboardCard
          title="Storage Used"
          value="68%"
          icon={<MdStorage />}
        />

      </div>


    </DashboardLayout>
  );
}

export default Dashboard;