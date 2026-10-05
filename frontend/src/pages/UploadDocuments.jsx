import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/UploadDocuments.css";

function UploadDocuments() {

  return (
    <DashboardLayout>

      <h1>
        Upload Documents
      </h1>

      <p>
        Upload files to build your enterprise knowledge base.
      </p>


      <div className="upload-container">

        <h2>
          Select Document
        </h2>

        <input 
          type="file"
        />


        <button>
          Upload Document
        </button>


      </div>


    </DashboardLayout>
  );
}


export default UploadDocuments;