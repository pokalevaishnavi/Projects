import React, { useState } from "react";
import { createTask } from "../../../services/taskService";

const TaskForm = ({ onCreated }) => {
  const [title, setTitle] = useState("");
  const [assigneeId, setAssigneeId] = useState("");
  const [dueDate, setDueDate] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const submit = async (e) => {
    e?.preventDefault();
    if (!title.trim() || isSubmitting) return;

    const userIdToUse =
      assigneeId.trim() !== "" ? Number(assigneeId.trim()) : 0;
    try {
      setIsSubmitting(true);
      await createTask({
        title: title.trim(),
        description: "",
        user_id: userIdToUse,
        due_date: dueDate || null,
      });

      setTitle("");
      setAssigneeId("");
      setDueDate("");
      if (onCreated) {
        await onCreated();
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form
      onSubmit={submit}
      className="flex flex-wrap items-center gap-2 rounded-2xl bg-slate-50 px-3 py-2 shadow-inner"
    >
      <input
        className="min-w-[220px] flex-1 rounded-xl border border-slate-200 bg-white px-3 py-2 text-sm text-slate-900 placeholder:text-slate-400 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-100"
        placeholder="Add a task to Backlog…"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <input
        className="w-24 rounded-xl border border-slate-200 bg-white px-2 py-2 text-xs text-slate-900 placeholder:text-slate-400 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-100"
        placeholder="User ID"
        value={assigneeId}
        onChange={(e) => setAssigneeId(e.target.value)}
      />

      <input
        type="date"
        className="w-36 rounded-xl border border-slate-200 bg-white px-2 py-2 text-xs text-slate-900 focus:border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-100"
        value={dueDate}
        onChange={(e) => setDueDate(e.target.value)}
      />

      <button
        type="submit"
        disabled={isSubmitting}
        className="inline-flex items-center rounded-xl bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:ring-offset-1 disabled:cursor-not-allowed disabled:opacity-70"
      >
        {isSubmitting ? "Adding…" : "Add task"}
      </button>
    </form>
  );
};

export default TaskForm;

