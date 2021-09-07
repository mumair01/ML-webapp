import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TasksPageSelector from "./components/TaskPageSelector";
import NotFoundPage from "./pages/NotFoundPage";

import "./App.css";

function App() {
  return (
    <Router>
      <div
        id="colorlib-page"
        style={{ height: "100vh", background: "#FFE8E3" }}
      >
        <div id="colorlib-wrap">
          <Switch>
            <Route path="/" component={HomePage} exact />
            <Route
              path="/tasks/:task/model/:model"
              component={TasksPageSelector}
            />
            <Route path="*" component={NotFoundPage} />
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
