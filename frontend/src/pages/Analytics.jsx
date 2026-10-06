import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/Analytics.css";


function Analytics() {

  return (
    <DashboardLayout>

      <h1>
        Analytics
      </h1>

      <p>
        Monitor CortexOS performance and usage insights.
      </p>


      <div className="analytics-cards">


        <div className="analytics-card">

          <h2>
            120
          </h2>

          <p>
            Documents Processed
          </p>

        </div>


        <div className="analytics-card">

          <h2>
            540
          </h2>

          <p>
            AI Queries
          </p>

        </div>


        <div className="analytics-card">

          <h2>
            25
          </h2>

          <p>
            Active Users
          </p>

        </div>


        <div className="analytics-card">

          <h2>
            68%
          </h2>

          <p>
            Storage Used
          </p>

        </div>


      </div>



      <div className="activity-box">

        <h2>
          Recent Activity
        </h2>


        <p>
          ✔ Employee Policy.pdf processed
        </p>


        <p>
          ✔ AI Assistant answered query
        </p>


        <p>
          ✔ New document uploaded
        </p>


      </div>


    </DashboardLayout>
  );
}


export default Analytics;