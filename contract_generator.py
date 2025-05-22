
from pandadoc import PandaDocClient

def generate_contract(template_id, data, api_key):
    client = PandaDocClient(api_key)
    return client.create_document_from_template(template_id, data)
