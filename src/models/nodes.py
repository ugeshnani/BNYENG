from sqlalchemy.orm import relationship, remote, foreign
from sqlalchemy import func
from sqlalchemy import Sequence, create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import LtreeType, Ltree

engine = create_engine('postgresql://postgres:Ugesh@1995@localhost:5432/BNY')

Base = declarative_base()

id_seq = Sequence('nodes_id_seq')


class Node(Base):
    __tablename__ = 'nodes'
    node_id = Column(String, primary_key=True)
    node = Column(String, nullable=False)
    parent_id = Column(String, nullable=False)
    path = Column(LtreeType, nullable=True)
    source = Column(String, nullable=False)
    # parent = relationship(
    #     'Node',
    #     primaryjoin=remote(path) == foreign(func.subpath(path, 0, -1)),
    #     backref='children',
    #     viewonly=True,
    # )

    def __init__(self, node_id, node, parent_id, path, source):

        self.node_id = node_id
        self.node = node
        self.parent_id = parent_id
        self.path = path
        self.source = source


    __table_args__ = (
        Index('ix_nodes_path', path, postgresql_using="gist"),
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Node({})'.format(self.name)

Base.metadata.create_all(engine)

