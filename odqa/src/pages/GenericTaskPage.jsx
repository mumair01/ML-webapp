import React from "react";

const GenericTaskPage = ({ task, model, page }) => (
  <section
    className="colorlib-about text-center"
    data-section="data"
    id="about"
  >
    <div className="colorlib-narrow-content col-md-12">
      <h2 className="colorlib-heading">{task + " using " + model}</h2>
    </div>
    {page}
  </section>
);

export default GenericTaskPage;
