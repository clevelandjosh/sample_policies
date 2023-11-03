from azure.identity import DefaultAzureCredential
from azure.management.policyinsights import PolicyStatesClient
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.identity import DefaultAzureCredential

# Create Azure Resource Graph client
credential = DefaultAzureCredential()
resource_graph_client = ResourceGraphClient(credential)


# Define and execute your Azure Resource Graph query
query = """az graph query -q "project type, name, subscriptionId, tenantId, managementGroup, location" --output json > azure_resource_hierarchy.json"""
# query = """
# resources
# | where type in~ ('Microsoft.Management/managementGroups', 'Microsoft.Management/managementGroups/subscriptions', 'Microsoft.Resources/resourceGroups')
# | project type, name, subscriptionId, tenantId, managementGroup, location
# """
results = resource_graph_client.resources(query)

# Create a list to store the hierarchy data
azure_hierarchy = []

for result in results:
    hierarchy_info = {
        "type": result['type'],
        "name": result['name'],
        "subscriptionId": result['subscriptionId'],
        "tenantId": result['tenantId'],
        "managementGroup": result['managementGroup'],
        "location": result['location']
    }
    azure_hierarchy.append(hierarchy_info)

# Continue with your policy analysis logic
# For example, you can now compare policy assignments based on the hierarchy data

# Initialize PolicyStatesClient and perform policy analysis
policy_states_client = PolicyStatesClient(credential)

# Retrieve policy states and perform analysis based on the hierarchy data
policy_states = list(policy_states_client.policy_states.list())

# Implement your logic to analyze the hierarchy and compare policy assignments
# based on "azure-policy-assignment-id," "azure-policy-definition-id," and "scope."
# Use the 'azure_hierarchy' list for reference.

# Output your findings based on the comparison.

# Keep in mind that this is a simplified example, and real-world implementation
# will depend on the structure of your Azure hierarchy and your specific requirements.
