import { useState } from 'react';
import './Sidebar.css';

function Sidebar({ jobs, selectedJobId, onCreateJob, onSelectJob }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim() || !description.trim()) return;
    onCreateJob(title.trim(), description.trim());
    setTitle('');
    setDescription('');
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-section glass-card">
        <h2 className="sidebar-heading">Create New Job</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            className="input-field"
            placeholder="Job Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <textarea
            className="input-field textarea-field"
            placeholder="Paste the full job description here..."
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows={6}
          />
          <button type="submit" className="btn-primary">
            + Create Job
          </button>
        </form>
      </div>

      <div className="sidebar-section glass-card">
        <h2 className="sidebar-heading">Your Jobs</h2>
        {jobs.length === 0 ? (
          <p className="sidebar-empty">No jobs yet. Create one above.</p>
        ) : (
          <div className="job-list">
            {jobs.map((job) => (
              <div
                key={job.id}
                className={`job-item ${selectedJobId === job.id ? 'job-item-active' : ''}`}
                onClick={() => onSelectJob(job.id)}
              >
                <span className="job-item-title">{job.title}</span>
                <span className="job-item-desc">
                  {job.description.length > 80
                    ? job.description.substring(0, 80) + '...'
                    : job.description}
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </aside>
  );
}

export default Sidebar;
