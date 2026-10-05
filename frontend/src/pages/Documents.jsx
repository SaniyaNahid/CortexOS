import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/Documents.css";

function Documents() {

  return (
    <DashboardLayout>

      <h1>
        Knowledge Base
      </h1>

      <p>
        Manage and explore your enterprise documents.
      </p>


      <div className="documents-list">

        <h2>
          Available Documents
        </h2>


        <div className="document-item">

          📄 Employee Policy.pdf

          <span>
            Processed ✅
          </span>

        </div>


        <div className="document-item">

          📄 Project Report.docx

          <span>
            Processing ⏳
          </span>

        </div>


        <div className="document-item">

          📄 AI Research.pdf

          <span>
            Processed ✅
          </span>

        </div>


      </div>


    </DashboardLayout>
  );
}

export default Documents;