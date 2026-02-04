import React, { useEffect, useState } from "react";
import { fetchTasks } from "../../../services/taskService";

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadTasks = async () => {
      try {
        const data = await fetchTasks();
        setTasks(data);
      } catch (err) {
        setError("Failed to load tasks");
      }
    };

    loadTasks();
  }, []);

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  return (
    <div>
      <h2>Tasks</h2>

      {tasks.length === 0 ? (
        <p>No tasks available</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong> — {task.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TaskList;
