import React, { useState, useEffect } from "react";
import {
  updateTaskStatus,
  updateTaskAssignment,
  deleteTask,
} from "../../../services/taskService";
import { fetchUsers } from "../../../services/userService";

const STATUSES = ["Backlog", "In Progress", "Review", "Done"];

const TaskCard = ({ task, onUpdated }) => {
  const [isUpdatingStatus, setIsUpdatingStatus] = useState(false);
  const [isUpdatingAssignment, setIsUpdatingAssignment] = useState(false);
  const [isEditingAssignment, setIsEditingAssignment] = useState(false);
  const [assigneeId, setAssigneeId] = useState(task.user_id ?? "");
  const [dueDate, setDueDate] = useState(
    task.due_date ? String(task.due_date).slice(0, 10) : ""
  );
  const [isDeleting, setIsDeleting] = useState(false);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const loadUsers = async () => {
      const data = await fetchUsers();
      setUsers(data);
    };
    loadUsers();
  }, []);


  const changeStatus = async (status) => {
    if (isUpdatingStatus || status === task.status) return;
    try {
      setIsUpdatingStatus(true);
      await updateTaskStatus(task.id, status);
      if (onUpdated) await onUpdated();
    } finally {
      setIsUpdatingStatus(false);
    }
  };

  const saveAssignment = async () => {
    if (isUpdatingAssignment) return;

    let payload = {
      user_id: null,
      due_date: dueDate || null,
    };

    if (assigneeId !== "") {
      const numericId = Number(assigneeId);

      if (!users.some((u) => u.id === numericId)) {
        alert("Invalid user id");
        return;
      }

      payload.user_id = numericId;
    }

    try {
      setIsUpdatingAssignment(true);
      await updateTaskAssignment(task.id, payload);
      if (onUpdated) await onUpdated();
      setIsEditingAssignment(false);
    } finally {
      setIsUpdatingAssignment(false);
    }
  };


  const removeTask = async () => {
    if (isDeleting) return;

    try {
      setIsDeleting(true);
      await deleteTask(task.id);
      if (onUpdated) await onUpdated();
    } finally {
      setIsDeleting(false);
    }
  };

  const formattedDue =
    task.due_date || dueDate
      ? new Date(task.due_date || dueDate).toLocaleDateString()
      : null;



  return (
    <div className="group rounded-2xl border border-slate-200 bg-white/90 p-3 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md">

      {/* Title + delete */}
      <div className="mb-2 flex items-start justify-between gap-2">
        <h3 className="line-clamp-2 text-sm font-semibold text-slate-900">
          {task.title}
        </h3>

        <button
          onClick={removeTask}
          disabled={isDeleting}
          className="text-xs font-medium text-red-500 opacity-0 transition group-hover:opacity-100 hover:text-red-600"
        >
          Delete
        </button>
      </div>

      {task.description && (
        <p className="mb-2 line-clamp-2 text-xs text-slate-500">
          {task.description}
        </p>
      )}

      <div className="mb-1 flex items-center justify-between text-[11px] text-slate-500">
        <span>
          Assigned:{" "}
          <span className="font-medium">
            {task.user_id ? task.user_id : "NA"}
          </span>
        </span>
        <span>
          Due:{" "}
          <span className="font-medium">
            {formattedDue || "No due date"}
          </span>
        </span>
      </div>

      <div className="mb-2 flex items-center justify-between">
        <span className="inline-flex items-center rounded-full bg-slate-100 px-2 py-0.5 text-[10px] font-medium uppercase tracking-wide text-slate-500">
          {task.status || "Backlog"}
        </span>
        {(isUpdatingStatus || isUpdatingAssignment || isDeleting) && (
          <span className="text-[10px] font-medium text-indigo-500">
            Updating…
          </span>
        )}
      </div>

      {isEditingAssignment ? (
        <div className="mb-2 flex items-center gap-2">

          {/* dropdown */}
          <select
            className="w-24 rounded-lg border border-slate-200 px-2 py-1 text-[11px]"
            value={assigneeId}
            onChange={(e) => setAssigneeId(e.target.value)}
          >
            <option value="">NA</option>
            {users.map((u) => (
              <option key={u.id} value={u.id}>
                User {u.id}
              </option>
            ))}
          </select>

        
          <button
            type="button"
            onClick={saveAssignment}
            className="rounded-lg bg-slate-900 px-2 py-1 text-[10px] text-white"
          >
            Save
          </button>
        </div>
      ) : (
        <button
          type="button"
          onClick={() => setIsEditingAssignment(true)}
          className="mb-2 text-[11px] font-medium text-indigo-600"
        >
          Assign / Edit
        </button>
      )}

      <div className="mt-1 flex flex-wrap gap-1.5">
        {STATUSES.map((status) => {
          const isActive = task.status === status;

          const base =
            "inline-flex items-center rounded-full px-2.5 py-0.5 text-[10px] font-medium border transition";
          const paletteByStatus = {
            Backlog:
              "border-slate-300 text-slate-600 bg-slate-50 hover:bg-slate-100",
            "In Progress":
              "border-amber-300 text-amber-700 bg-amber-50 hover:bg-amber-100",
            Review:
              "border-sky-300 text-sky-700 bg-sky-50 hover:bg-sky-100",
            Done:
              "border-emerald-300 text-emerald-700 bg-emerald-50 hover:bg-emerald-100",
          };

          const activeRing = isActive
            ? "ring-1 ring-offset-1 ring-indigo-500"
            : "";

          return (
            <button
              key={status}
              disabled={isUpdatingStatus}
              onClick={() => changeStatus(status)}
              className={`${base} ${paletteByStatus[status]} ${activeRing}`}
            >
              {status}
            </button>
          );
        })}
      </div>
    </div>
  );
};

export default TaskCard;