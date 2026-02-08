import API from "./api";
import axios from "axios";

const token = localStorage.getItem("token");

export const fetchTasks = async () => {
  const response = await axios.get("http://127.0.0.1:8000/tasks/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};

export const createTask = async (task) => {
  const res = await API.post("/tasks/", task);
  return res.data;
};

export const updateTaskStatus = async (id, status) => {
  const res = await API.patch(`/tasks/${id}/status`, { status });
  return res.data;
};

export const deleteTask = async (taskId) => {
  await API.delete(`/tasks/${taskId}`);
};

export const updateTaskAssignment = async (id, { user_id, due_date }) => {
  const res = await API.patch(`/tasks/${id}/assignment`, {
    user_id,
    due_date: due_date || null,
  });
  return res.data;
};

