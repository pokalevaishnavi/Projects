import React from "react";

const Sidebar = () => {
  return (
    <aside className="flex w-64 flex-col border-r border-slate-200 bg-slate-950 text-slate-50">
      <div className="px-6 py-5">
        <h1 className="text-xl font-semibold tracking-tight">TaskFlow</h1>
        <p className="mt-1 text-xs text-slate-400">
          Planner-style work management
        </p>
      </div>

      <nav className="flex-1 space-y-1 px-2 py-2 text-sm">
        <span className="block rounded-lg bg-slate-800 px-3 py-2 font-medium text-slate-50">
          Board
        </span>
        <span className="block rounded-lg px-3 py-2 text-slate-400">
          My tasks
        </span>
        <span className="block rounded-lg px-3 py-2 text-slate-400">
          Analytics
        </span>
        <span className="block rounded-lg px-3 py-2 text-slate-400">
          Settings
        </span>
      </nav>

      <div className="px-6 pb-4 pt-2 text-xs text-slate-500">
        © 2026 TaskFlow
      </div>
    </aside>
  );
};

export default Sidebar;

