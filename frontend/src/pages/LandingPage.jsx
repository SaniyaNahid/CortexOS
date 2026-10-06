import "./../styles/LandingPage.css";

import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import FeaturesSection from "../components/FeaturesSection";
import StatsSection from "../components/StatsSection";
import Footer from "../components/Footer";

function LandingPage() {
  return (
    <div className="landing-page">
      <Navbar />
      <HeroSection />
      <FeaturesSection />
      <StatsSection />
      <Footer />
    </div>
  );
}

export default LandingPage;