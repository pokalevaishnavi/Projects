import API from "./api";

export const loginUser = async (email, password) => {
  const response = await API.post("/auth/login", {
    email,
    password,
  });

  localStorage.setItem("token", response.data.access_token);

  return response.data;
};
