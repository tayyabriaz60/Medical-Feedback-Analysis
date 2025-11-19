-- Database Index Creation Script
-- Run this manually if Alembic migrations are not available
-- These indexes improve query performance

-- Feedback table indexes
CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_feedback_department_status 
    ON feedback(department, status);

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_feedback_created_status 
    ON feedback(created_at, status);

-- Analysis table indexes
CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_analysis_urgency_sentiment 
    ON analysis(urgency, sentiment);

CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_analysis_category_urgency 
    ON analysis(primary_category, urgency);

-- User table indexes (already created by models, but verify)
CREATE INDEX CONCURRENTLY IF NOT EXISTS ix_users_email 
    ON users(email);

-- Verify indexes were created
SELECT tablename, indexname 
FROM pg_indexes 
WHERE tablename IN ('users', 'feedback', 'analysis', 'actions')
ORDER BY tablename, indexname;

