import { BrowserRouter, Routes, Route } from "react-router-dom";

import LandingPage from "./pages/LandingPage";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Documents from "./pages/Documents";
import AIChat from "./pages/AIChat";
import UploadDocuments from "./pages/UploadDocuments";
import Analytics from "./pages/Analytics";
import UserManagement from "./pages/UserManagement";
import Settings from "./pages/Settings";
import Profile from "./pages/Profile";

import ProtectedRoute from "./components/ProtectedRoute";


function App() {
  return (
    <BrowserRouter>

      <Routes>


        {/* Public Pages */}

        <Route 
          path="/" 
          element={<LandingPage />} 
        />


        <Route 
          path="/login" 
          element={<Login />} 
        />



        {/* Protected Pages */}


        <Route 
          path="/dashboard" 
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/documents" 
          element={
            <ProtectedRoute>
              <Documents />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/upload" 
          element={
            <ProtectedRoute>
              <UploadDocuments />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/chat" 
          element={
            <ProtectedRoute>
              <AIChat />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/analytics" 
          element={
            <ProtectedRoute>
              <Analytics />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/users" 
          element={
            <ProtectedRoute>
              <UserManagement />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/settings" 
          element={
            <ProtectedRoute>
              <Settings />
            </ProtectedRoute>
          } 
        />


        <Route 
          path="/profile" 
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          } 
        />


      </Routes>

    </BrowserRouter>
  );
}


export default App;