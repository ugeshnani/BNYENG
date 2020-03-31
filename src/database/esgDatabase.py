from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import expression
from sqlalchemy_utils.types.ltree import LQUERY

# from src.models import nodes
from src.models import nodes
from src.models.nodes import Node

engine = create_engine('postgresql://postgres:Ugesh@1995@localhost:5432/BNY')
Session = sessionmaker(bind=engine)
session = Session()


class esgDatabase:

    def add_data(self, node_list):
        # To create a tree like the example shown
        # at the top of this post:
        # Session.configure
        # con = engine.connect()
        # for value in node_list:
        #     ins = 'INSERT INTO "nodes" ''(node_id, node,parent_id,path,source) ''VALUES (1,"raw1")'
        #     result = con.excute(ins)
        print("inside add data")
        for node in node_list:
            # print(node.source)
            session.add(node)

        session.commit()

        # node_id = Column(String, nullable=False)
        # node = Column(String, nullable=False)
        # parent_id = Column(String, nullable=True)
        # path = Column(LtreeType, nullable=True)
        # source = Column(String, nullable=False)


