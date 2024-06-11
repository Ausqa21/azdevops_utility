from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

# Fill in with your personal access token and org URL
personal_access_token = 'fdteif5bzvyknmogv7pylw24r4uw6pmedqssps32sf4oa27zeh5a'
organization_url = 'https://dev.azure.com/ausqa21'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()

# Get the first page of projects
get_projects_response = core_client.get_projects()

if get_projects_response is None:
    print("There are no projects")
    exit(1)
else:
    for x in range(len(get_projects_response)):
        pprint.pprint("[" + str(x) + "] " + get_projects_response[x].name)


# index = 0
# while get_projects_response is not None:
#     for project in get_projects_response:
#         pprint.pprint("[" + str(index) + "] " + project.name)
#         index += 1
#     if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
#         # Get the next page of projects
#         get_projects_response = core_client.get_projects(
#             continuation_token=get_projects_response.continuation_token)
#     else:
#         # All projects have been retrieved
#         get_projects_response = None
