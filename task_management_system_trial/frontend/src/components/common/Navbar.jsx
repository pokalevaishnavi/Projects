import React from "react";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <header className="flex items-center justify-between border-b border-slate-200 bg-white/80 px-6 py-3 backdrop-blur">
      <div className="flex items-center gap-2">
        <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-600 text-xs font-semibold text-white">
          TF
        </div>
        <div>
          <p className="text-sm font-semibold text-slate-900">TaskFlow</p>
          <p className="text-xs text-slate-500">Team Task Management</p>
        </div>
      </div>

      <div className="flex items-center gap-3">
        <button
          type="button"
          onClick={() => navigate("/dashboard")}
          className="hidden sm:inline-flex items-center rounded-full px-3 py-1 text-xs font-medium text-slate-600 hover:bg-slate-100"
        >
          Board
        </button>
        <button
          type="button"
          onClick={handleLogout}
          className="inline-flex items-center rounded-full bg-slate-900 px-3 py-1.5 text-xs font-medium text-slate-50 hover:bg-slate-800"
        >
          Logout
        </button>
      </div>
    </header>
  );
};

export default Navbar;

