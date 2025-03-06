from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Repository(db.Model):
    __tablename__ = 'repositories'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), unique=True, nullable=False)

    def __repr__(self):
        return f'<Repository {self.url}>'


class AnalysisResult(db.Model):
    __tablename__ = 'analysis_results'
    id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, db.ForeignKey(
        'repositories.id'), nullable=False)
    file_name = db.Column(db.String(128), nullable=False)
    unsafe_code_type = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<AnalysisResult {self.repo_id} - {self.file_name}>'
