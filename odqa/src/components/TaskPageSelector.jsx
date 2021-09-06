import React from "react";
import tasksPages from "./tasks-content";
import GenericTaskPage from "../pages/GenericTaskPage";
import NotFoundPage from "../pages/NotFoundPage";

const TasksPageSelector = ({ match }) => {
  const task = match.params.task;
  const model = match.params.model;

  for (const taskPage of tasksPages) {
    if (taskPage.task === task && taskPage.model === model) {
      return <GenericTaskPage task={task} model={model} page={taskPage.page} />;
    }
  }

  return NotFoundPage;
};

export default TasksPageSelector;
