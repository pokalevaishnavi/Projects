import API from "./api";

export const fetchTasks = async () => {
  const token = localStorage.getItem("token");

  const response = await API.get("/tasks/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
};
