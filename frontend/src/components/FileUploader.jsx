import { useState, useRef } from 'react';
import './FileUploader.css';

function FileUploader({ onUpload, loading, jobId }) {
  const [files, setFiles] = useState([]);
  const [dragOver, setDragOver] = useState(false);
  const inputRef = useRef(null);

  const validExtensions = ['.pdf', '.docx', '.txt'];

  const isValidFile = (file) => {
    const ext = '.' + file.name.split('.').pop().toLowerCase();
    return validExtensions.includes(ext);
  };

  const addFiles = (newFiles) => {
    const valid = Array.from(newFiles).filter(isValidFile);
    setFiles((prev) => {
      const existingNames = new Set(prev.map(f => f.name));
      const unique = valid.filter(f => !existingNames.has(f.name));
      return [...prev, ...unique];
    });
  };

  const removeFile = (index) => {
    setFiles((prev) => prev.filter((_, i) => i !== index));
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragOver(false);
    addFiles(e.dataTransfer.files);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setDragOver(true);
  };

  const handleDragLeave = () => setDragOver(false);

  const handleClick = () => inputRef.current?.click();

  const handleInputChange = (e) => {
    addFiles(e.target.files);
    e.target.value = '';
  };

  const handleUpload = () => {
    if (files.length === 0) return;
    onUpload(files);
    setFiles([]);
  };

  return (
    <div className="uploader-container glass-card-main" style={{ animationDelay: '0.1s' }}>
      <h3 className="uploader-heading">Upload Resumes</h3>

      <div
        className={`drop-zone ${dragOver ? 'drop-zone-active' : ''}`}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onClick={handleClick}
      >
        <input
          ref={inputRef}
          type="file"
          accept=".pdf,.docx,.txt"
          multiple
          onChange={handleInputChange}
          style={{ display: 'none' }}
        />
        <div className="drop-icon">📁</div>
        <p className="drop-text">Drag & drop resumes here, or click to browse</p>
        <p className="drop-hint">Supports PDF, DOCX, TXT</p>
      </div>

      {files.length > 0 && (
        <div className="file-list">
          {files.map((file, i) => (
            <span key={i} className="file-pill">
              {file.name}
              <button className="file-remove" onClick={() => removeFile(i)}>×</button>
            </span>
          ))}
        </div>
      )}

      <button
        className="btn-screen"
        onClick={handleUpload}
        disabled={loading || files.length === 0}
      >
        {loading ? (
          <span className="btn-loading">
            <span className="spinner"></span>
            Analyzing...
          </span>
        ) : (
          `Screen ${files.length || ''} Resume${files.length !== 1 ? 's' : ''} 🚀`
        )}
      </button>
    </div>
  );
}

export default FileUploader;
