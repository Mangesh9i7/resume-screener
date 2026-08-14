import CandidateCard from './CandidateCard';
import './ResultsGrid.css';

function ResultsGrid({ results, loading }) {
  const sorted = [...results].sort((a, b) => b.score - a.score);

  return (
    <div className="results-container">
      {loading && (
        <div className="results-overlay">
          <div className="results-spinner"></div>
          <p className="results-loading-text">Analyzing resumes...</p>
        </div>
      )}

      {!loading && sorted.length === 0 && (
        <div className="results-empty glass-card-main">
          <p>No candidates screened yet. Upload resumes above to get started.</p>
        </div>
      )}

      {sorted.length > 0 && (
        <>
          <h3 className="results-heading">Candidate Rankings</h3>
          <div className="results-list">
            {sorted.map((candidate, index) => (
              <CandidateCard
                key={candidate.id}
                candidate={candidate}
                rank={index + 1}
                delay={index * 0.1}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default ResultsGrid;
