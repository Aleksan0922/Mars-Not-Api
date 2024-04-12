import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    creator_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer,
                                  default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.Date)
    end_date = sqlalchemy.Column(sqlalchemy.Date)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)