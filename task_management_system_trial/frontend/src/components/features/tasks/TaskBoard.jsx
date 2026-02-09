import React, { useEffect, useState } from "react";
import { fetchTasks } from "../../../services/taskService";
import TaskCard from "./TaskCard";
import TaskForm from "./TaskForm";

const TaskBoard = () => {
  const [tasks, setTasks] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const loadTasks = async () => {
    try {
      setIsLoading(true);
      const data = await fetchTasks();
      setTasks(data);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const backlog = tasks.filter((t) => t.status === "Backlog");
  const inProgress = tasks.filter((t) => t.status === "In Progress");
  const review = tasks.filter((t) => t.status === "Review");
  const done = tasks.filter((t) => t.status === "Done");

  return (
    <div className="flex h-screen flex-col overflow-hidden bg-slate-50">
      
      {/* Header */}
      <div className="px-6 pt-6 pb-4 border-b border-slate-200 bg-white/80 backdrop-blur">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <h1 className="text-2xl font-semibold text-slate-900">
              Team Tasks
            </h1>
            <p className="text-sm text-slate-500">
              Visualize and manage work across Backlog, In Progress, Review, and Done.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-xs font-medium text-slate-500 uppercase tracking-wide">
              Total Tasks
            </span>
            <span className="inline-flex items-center justify-center rounded-full bg-indigo-50 px-3 py-1 text-sm font-semibold text-indigo-700">
              {tasks.length}
            </span>
          </div>
        </div>

        <div className="mt-4">
          <TaskForm onCreated={loadTasks} />
        </div>
      </div>

      {/* Columns container */}
       <div className="flex-1 overflow-hidden">
        <div className="h-full overflow-x-auto overflow-y-hidden pb-2">
          <div className="flex w-max h-full gap-5 px-6 pt-4 pb-1">
            <Column title="Backlog" count={backlog.length} accent="border-slate-300 bg-slate-50" tasks={backlog} onRefresh={loadTasks}/>
            <Column title="In Progress" count={inProgress.length} accent="border-amber-300 bg-amber-50" tasks={inProgress} onRefresh={loadTasks}/>
            <Column title="Review" count={review.length} accent="border-sky-300 bg-sky-50" tasks={review} onRefresh={loadTasks}/>
            <Column title="Done" count={done.length} accent="border-emerald-300 bg-emerald-50" tasks={done} onRefresh={loadTasks}/>
          </div>
        </div>
      </div>

      {isLoading && (
        <div className="pointer-events-none fixed inset-x-0 bottom-4 flex justify-center">
          <div className="flex items-center gap-2 rounded-full bg-slate-900/90 px-4 py-2 text-xs font-medium text-slate-100 shadow-lg">
            <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-emerald-400" />
            Syncing board…
          </div>
        </div>
      )}
    </div>
  );
};

const Column = ({ title, count, accent, tasks, onRefresh }) => {
  return (
    <div className={`flex h-full min-w-[320px] flex-1 flex-col rounded-2xl border p-4 shadow-sm ${accent}`}>
      
      <div className="mb-3 flex items-center justify-between">
        <h2 className="text-sm font-semibold text-slate-800">{title}</h2>
        <span className="rounded-full bg-slate-100 px-2 py-0.5 text-xs font-semibold text-slate-600">
          {count}
        </span>
      </div>

      {/* Scrollable tasks */}
      <div className="flex-1 overflow-y-auto space-y-3 pr-1">
        {tasks.map((task) => (
          <TaskCard key={task.id} task={task} onUpdated={onRefresh} />
        ))}

        {tasks.length === 0 && (
          <div className="rounded-xl border border-dashed border-slate-200 bg-slate-50/70 px-3 py-4 text-center text-xs text-slate-400">
            No tasks in {title}.
          </div>
        )}
      </div>
    </div>
  );
};

export default TaskBoard;