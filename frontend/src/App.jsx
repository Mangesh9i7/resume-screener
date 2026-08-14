import { useState, useEffect } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import JobDetail from './components/JobDetail';
import FileUploader from './components/FileUploader';
import ResultsGrid from './components/ResultsGrid';
import './App.css';

function App() {
  const [jobs, setJobs] = useState([]);
  const [selectedJobId, setSelectedJobId] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    try {
      const response = await fetch('/api/jobs');
      if (!response.ok) throw new Error('Failed to fetch jobs');
      const data = await response.json();
      setJobs(data);
    } catch (err) {
      console.error(err);
      setError('Could not load jobs');
    }
  };

  const createJob = async (title, description) => {
    try {
      const response = await fetch('/api/jobs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description }),
      });
      if (!response.ok) throw new Error('Failed to create job');
      const newJob = await response.json();
      setJobs([...jobs, newJob]);
      selectJob(newJob.id);
    } catch (err) {
      console.error(err);
      alert('Error creating job');
    }
  };

  const selectJob = async (id) => {
    setSelectedJobId(id);
    setResults([]);
    fetchResults(id);
  };

  const fetchResults = async (jobId) => {
    setLoading(true);
    try {
      const response = await fetch(`/api/jobs/${jobId}/results`);
      if (response.ok) {
        const data = await response.json();
        setResults(data.candidates || []);
      }
    } catch (err) {
      console.error('Failed to fetch results', err);
    } finally {
      setLoading(false);
    }
  };

  const uploadResumes = async (files) => {
    if (!selectedJobId) return;
    setLoading(true);
    
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append('files', files[i]);
    }

    try {
      const response = await fetch(`/api/jobs/${selectedJobId}/resumes`, {
        method: 'POST',
        body: formData,
      });
      if (!response.ok) throw new Error('Upload failed');
      const data = await response.json();
      
      const successfulResults = data.results.filter(r => !r.error);
      const newResults = [...successfulResults, ...results].sort((a, b) => b.score - a.score);
      setResults(newResults);
    } catch (err) {
      console.error(err);
      alert('Error uploading files');
    } finally {
      setLoading(false);
    }
  };

  const selectedJob = jobs.find(j => j.id === selectedJobId);

  return (
    <div className="app-container">
      <Sidebar 
        jobs={jobs} 
        selectedJobId={selectedJobId} 
        onCreateJob={createJob} 
        onSelectJob={selectJob} 
      />
      <div className="main-content">
        <Header />
        {selectedJobId ? (
          <>
            <JobDetail job={selectedJob} />
            <FileUploader onUpload={uploadResumes} loading={loading} jobId={selectedJobId} />
            <ResultsGrid results={results} loading={loading} />
          </>
        ) : (
          <div className="empty-state">
            <h1>Welcome to Resume Screener</h1>
            <p>Select a job from the sidebar or create a new one to get started.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
