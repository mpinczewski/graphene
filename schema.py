"""Basic"""


# import graphene
# import json

# from datetime import datetime


# class User(graphene.ObjectType):
#     id = graphene.ID()
#     username = graphene.String()
#     last_login = graphene.DateTime()


# class Query(graphene.ObjectType):
#     users = graphene.List(User)

#     def resolve_users(self, info):
#         return [
#             User(username='Alice', last_login=datetime.now()),
#             User(username='Bob', last_login=datetime.now()),
#             User(username='Steven', last_login=datetime.now())
            
#         ]  

# schema = graphene.Schema(query=Query)


# resault = schema.execute(
#     '''
#     {
#         users {
#             username
#             lastLogin
#         }
#     }
#     '''
# )

# items = dict(resault.data.items())
# print(json.dumps(items, indent=4))


"""Wybierz ile wyników ma śię wyświetlić"""


# import graphene
# import json

# from datetime import datetime


# class User(graphene.ObjectType):
#     id = graphene.ID()
#     username = graphene.String()
#     last_login = graphene.DateTime()


# class Query(graphene.ObjectType):
#     users = graphene.List(User, first=graphene.Int())

#     def resolve_users(self, info, first):
#         return [
#             User(username='Alice', last_login=datetime.now()),
#             User(username='Bob', last_login=datetime.now()),
#             User(username='Steven', last_login=datetime.now())
            
#         ][:first]  

# schema = graphene.Schema(query=Query)


# resault = schema.execute(
#     '''
#     {
#         users(first: 2) {
#             username
#             lastLogin
#         }
#     }
#     '''
# )

# items = dict(resault.data.items())
# print(json.dumps(items, indent=4))

"""Mutations"""


# import graphene
# import json

# from datetime import datetime


# class User(graphene.ObjectType):
#     id = graphene.ID()
#     username = graphene.String()
#     last_login = graphene.DateTime(required=False)


# class Query(graphene.ObjectType):
#     users = graphene.List(User, first=graphene.Int())

#     def resolve_users(self, info, first):
#         return [
#             User(username='Alice', last_login=datetime.now()),
#             User(username='Bob', last_login=datetime.now()),
#             User(username='Steven', last_login=datetime.now())
            
#         ][:first]  


# class CreateUser(graphene.Mutation):
    
#     class Arguments:
#         username = graphene.String()
        
#     user = graphene.Field(User)
    
#     def mutate(self, info, username):
#         user = User(username=username)
#         return CreateUser(user=user)

# class Mutations(graphene.ObjectType):
#     create_user = CreateUser.Field()


# schema = graphene.Schema(query=Query, mutation=Mutations)


# resault = schema.execute(
#     '''
# mutation createUser {
#     createUser(username: "Bob"){
#         user {
#             username
#         }
#     }
# }
#     '''
# )

# items = dict(resault.data.items())
# print(json.dumps(items, indent=4))


"""Variables"""


import graphene
import json

from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='Alice', last_login=datetime.now()),
            User(username='Bob', last_login=datetime.now()),
            User(username='Steven', last_login=datetime.now())
            
        ][:first]  


class CreateUser(graphene.Mutation):
    
    class Arguments:
        username = graphene.String()
        
    user = graphene.Field(User)
    
    def mutate(self, info, username):
        user = User(username=username)
        return CreateUser(user=user)

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)


resault = schema.execute(
    '''
    mutation createUser {
        createUser(username: "Bob"){
            user {
                username
            }
        }
    }
    ''',
    variable_values={'username': 'Bob'}
)

items = dict(resault.data.items())
print(json.dumps(items, indent=4))