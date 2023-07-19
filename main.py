from qbClient import AuthClient
import constants as cfg
import requests
from future.moves.urllib.parse import urlencode

auth_client = AuthClient(**cfg.client_secrets)

def getCustomerData(accessToken):
    #making Request
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    url = '{0}/v3/company/{1}/companyinfo/{1}'.format(base_url, cfg.qBData["realm_id"])
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    print("Response = ",response)
    print("Response Data = ",response.text)

    print("Success")


# Production Base URL:https://quickbooks.api.intuit.com
# Sandbox Base URL:https://sandbox-quickbooks.api.intuit.com
def getInvoiceData(accessToken):
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    # query = "select * from Invoice"
    query = "select * from Invoice where TxnDate = '2023-06-20'"
    url = '{0}/v3/company/{1}/query?query={2}&minorversion=65'.format(base_url, cfg.qBData["realm_id"], query)
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print("Response:", response)
    if response.status_code == 200:
        invoice_data = response.json()
        # Process and use the invoice_data as needed
        print("Invoice Data:", invoice_data)
    else:
        print("Error occurred:", response.text)

    print("Success")


def getCreditMemoData(accessToken):
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    query = "Select * from CreditMemo where TxnDate > '2014-04-15'"
    url = '{0}/v3/company/{1}/query?query={2}&minorversion=65'.format(base_url, cfg.qBData["realm_id"], query)
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print("Response:", response)
    if response.status_code == 200:
        invoice_data = response.json()
        # Process and use the invoice_data as needed
        print("Invoice Data:", invoice_data)
    else:
        print("Error occurred:", response.text)

    print("Success")
def refresh_token():
    response = auth_client.refresh(refresh_token=cfg.refreshToken)
    return response

def getPaymentData(accessToken):
    #making Request
    base_url = f'https://sandbox.api.intuit.com/quickbooks/v4/payments/charges/'
    auth_header = 'Bearer {0}'.format(accessToken)
    data = {
        'Authorization': auth_header
    }
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json;charset=UTF-8',
        'Content-type': '*/*'
    }

    response = requests.get(base_url, headers=headers)

    print("Response 2 = ",response)
    print("Response Data 2 = ",response.text)

    print("Success")


if __name__ == "__main__":
    # fetchData()
    response = refresh_token()
    # getCustomerData(accessToken = response["access_token"])
    getInvoiceData(accessToken = response["access_token"])
    # getCreditMemoData(accessToken = response["access_token"])
    response2 = auth_client.get_user_info(access_token=response["access_token"])
    print(response2.text)
    print("\n\n\n")
    # getPaymentData(accessToken = response["access_token"])

