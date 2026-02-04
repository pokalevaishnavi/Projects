import React from "react";
import Login from "./components/features/auth/Login";
import TaskList from "./components/features/tasks/TaskList";

function App() {
  return (
    <div>
      <Login />
      <hr />
      <TaskList />
    </div>
  );
}

export default App;
