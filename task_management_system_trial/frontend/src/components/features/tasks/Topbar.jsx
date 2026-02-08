import React from "react";

const Topbar = () => {
  return (
    <div className="flex items-center justify-between border-b border-slate-200 bg-white px-6 py-3">
      <h2 className="text-lg font-semibold text-slate-900">Dashboard</h2>

      <div className="flex items-center gap-3">
        <span className="text-sm text-slate-500">Admin</span>
        <div className="flex h-8 w-8 items-center justify-center rounded-full bg-indigo-600 text-sm font-semibold text-white">
          A
        </div>
      </div>
    </div>
  );
};

export default Topbar;

