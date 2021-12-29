import React from "react";
import Selector from "../components/Selector";
const HomePage = () => (
  <section
    className="colorlib-about text-center"
    data-section="data"
    id="about"
  >
    <div className="colorlib-narrow-content col-md-12">
      <h2
        className="colorlib-heading"
        style={{ fontSize: "200%", textDecoration: "underline" }}
      >
        ODQA web app
      </h2>
      <p>Accomplish specific tasks with state of the art Machine Learning</p>
      <Selector />
    </div>
  </section>
);

export default HomePage;
