import { Link } from "react-router-dom";

function QuickActions() {
  return (
    <div className="quick-actions">

      <h2>Quick Actions</h2>

      <div className="action-buttons">

        <Link to="/upload">
          <button>Upload Document</button>
        </Link>

        <Link to="/chat">
          <button>AI Chat</button>
        </Link>

        <Link to="/documents">
          <button>View Documents</button>
        </Link>

        <Link to="/analytics">
          <button>Analytics</button>
        </Link>

      </div>

    </div>
  );
}

export default QuickActions;