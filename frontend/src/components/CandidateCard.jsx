import { useState } from 'react';
import './CandidateCard.css';

function CandidateCard({ candidate, rank, delay }) {
  const [expanded, setExpanded] = useState(false);

  const score = candidate.score || 0;
  const scoreClass = score >= 70 ? 'score-high' : score >= 40 ? 'score-med' : 'score-low';

  return (
    <div
      className="candidate-card"
      style={{ animationDelay: `${delay}s` }}
    >
      <div className="candidate-content">
        <div className="candidate-info">
          <div className="candidate-rank">#{rank}</div>
          <div className="candidate-details">
            <h4 className="candidate-filename">{candidate.filename}</h4>

            <div className="skills-container">
              {candidate.matched_skills?.map((skill, i) => (
                <span key={`m-${i}`} className="skill-pill skill-match">✓ {skill}</span>
              ))}
              {candidate.missing_skills?.map((skill, i) => (
                <span key={`x-${i}`} className="skill-pill skill-miss">✗ {skill}</span>
              ))}
            </div>
          </div>
        </div>

        <div className={`score-badge ${scoreClass}`}>
          {score}
        </div>
      </div>

      <button
        className="reasoning-toggle"
        onClick={() => setExpanded(!expanded)}
      >
        {expanded ? '▲ Hide Reasoning' : '▼ View Reasoning'}
      </button>

      <div className={`reasoning-panel ${expanded ? 'reasoning-open' : ''}`}>
        <p className="reasoning-text">{candidate.reasoning}</p>
      </div>
    </div>
  );
}

export default CandidateCard;
