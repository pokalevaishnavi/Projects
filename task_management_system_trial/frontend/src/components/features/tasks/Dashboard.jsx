import React from "react";
import Sidebar from "./Sidebar";
import Topbar from "./Topbar";
import TaskBoard from "./TaskBoard";

const Dashboard = () => {
  return (
    <div className="flex h-screen bg-slate-100">
      {/* <Sidebar /> */}

      <div className="flex flex-1 flex-col overflow-hidden rounded-l-3xl bg-slate-50 shadow-inner">
        <Topbar />
        <TaskBoard />
      </div>
    </div>
  );
};

export default Dashboard;