import express, { response } from "express";
import bodyParser from "body-parser";

const app = express();
const axios = require("axios");
const flaskURL = "http://127.0.0.1:5000/";

app.use(bodyParser.json());

//--- Adding routes

app.post("/api/execute", async (req, res) => {
  const { modelName, task, executeKwargs } = req.body;
  const data = {
    "model_name": modelName,
    "task": task,
    "execute_kwargs": executeKwargs,
  };

  if (!modelName || !task || !executeKwargs) {
    return res.status(404).json({ message: "Bad request" });
  }
  axios
    .post(flaskURL + "/execute", data)
    .then((response) => {
      res.status(200).json(response.data);
    })
    .catch((error) => res.status(500).json({ message: error.message }));
});

app.get("/api/get_model_tasks", async (req, res) => {
  if (!req.body["model_name"]) {
    return res.status(404).json({ message: "model name required" });
  }
  axios
    .get(flaskURL + "/get_model_tasks?model_name=" + req.body["model_name"])
    .then((response) => {
      res.status(200).json(response.data);
    })
    .catch((error) => res.status(500).json({ message: error.message }));
});

app.get("/api/get_models_for_task", async (req, res) => {
  if (!req.body.task) {
    return res.status(404).json({ message: "task required" });
  }
  axios
    .get(flaskURL + "/get_models_for_task?task=" + req.body.task)
    .then((response) => {
      res.status(200).json(response.data);
    })
    .catch((error) => res.status(500).json({ message: error.message }));
});

app.get("/api/get_models_by_task", async (req, res) => {
  axios
    .get(flaskURL + "/get_models_by_task")
    .then((response) => {
      res.status(200).json(response.data);
    })
    .catch((error) => {
      res.status(500).json({ message: error.message });
    });
});

app.listen(8000, () => console.log("Listening on port 8000"));
