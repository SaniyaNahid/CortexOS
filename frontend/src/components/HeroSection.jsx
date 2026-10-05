import { Link } from "react-router-dom";

function HeroSection() {
  return (
    <section className="hero">

      <div className="hero-text">

        <h1>
          CortexOS
        </h1>

        <p>
          AI-Powered Enterprise Intelligence and Decision Support System
        </p>

        <p>
          Transform organizational knowledge into intelligent insights
          through AI-driven search, document understanding, and
          decision support.
        </p>


        <div className="buttons">

          <Link to="/login" className="primary-btn">
            Get Started
          </Link>

          <Link to="/" className="secondary-btn">
            Learn More
          </Link>

        </div>

      </div>

    </section>
  );
}

export default HeroSection;