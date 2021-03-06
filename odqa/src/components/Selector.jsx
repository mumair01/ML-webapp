import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Select from "react-select";

const Selector = () => {
  const [modelsByTask, setModelsByTask] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      const result = await fetch("/api/get_models_by_task");
      const body = await result.json();
      const res = [];
      for (const [task, models] of Object.entries(body)) {
        for (const model of models) {
          res.push({ "task": task, "model": model });
        }
      }
      setModelsByTask(res);
    };
    fetchData();
  }, []);

  return (
    <>
      <Select
        options={modelsByTask.map((item) => ({
          value: (
            <Link to={"tasks/" + item.task + "/model/" + item.model}>
              {item.task + "/" + item.model}
            </Link>
          ),
          label: (
            <Link to={"tasks/" + item.task + "/model/" + item.model}>
              {item.task + "/" + item.model}
            </Link>
          ),
        }))}
      />
    </>
  );
};

export default Selector;
