import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Member as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_members = SQLAlchemyConnectionField(User)
    user = graphene.Field(User)


schema = graphene.Schema(query=Query, types=[User])
