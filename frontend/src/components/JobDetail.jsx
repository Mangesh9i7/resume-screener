import './JobDetail.css';

function JobDetail({ job }) {
  if (!job) return null;

  return (
    <div className="job-detail glass-card-main">
      <h2 className="job-detail-title">{job.title}</h2>
      <p className="job-detail-desc">{job.description}</p>
    </div>
  );
}

export default JobDetail;
