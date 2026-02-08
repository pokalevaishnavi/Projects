import API from "./api";

export const loginUser = async (data) => {
  const res = await API.post("/auth/login", data);
  localStorage.setItem("token", res.data.access_token);
  return res.data;
};

