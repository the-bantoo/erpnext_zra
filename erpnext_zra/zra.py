import requests #, frappe
import json


def initialize_device(base_url, tpin, bhf_id, dvc_srl_no):
    url = f"{base_url}/initializer/selectInitInfo"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "tpin": tpin,
        "bhfId": bhf_id,
        "dvcSrlNo": dvc_srl_no
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None

if __name__ == "__main__":
    # Replace these values with your actual values
    base_url = "http://localhost:8080/zrasandboxvsdc"
    tpin = "2295829289"
    bhf_id = "000"
    dvc_srl_no = "2295829289_VSDC"
    
    result = initialize_device(base_url, tpin, bhf_id, dvc_srl_no)
    
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("Initialization failed")


class ZRAAPI:
    BASE_URL = "https://localhost:8080/zrasandboxvsdc"

    def __init__(self, api_key, device_serial_no, branch_id, tpin):
        self.api_key = api_key
        self.device_serial_no = device_serial_no
        self.branch_id = branch_id
        self.tpin = tpin

    def initialize_device(self):
        url = f"{self.BASE_URL}/initializer/selectInitInfo"
        payload = {
            "tpin": self.tpin,
            "bhfId": self.branch_id,
            "dvcSrlNo": self.device_serial_no
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response.json()

    def submit_sales_invoice(self, invoice_data):
        url = f"{self.BASE_URL}/sales/newInvoice"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(url, data=json.dumps(invoice_data), headers=headers)
        return response.json()

    def get_standard_codes(self):
        url = f"{self.BASE_URL}/standardCodes"
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def get_tax_types(self):
        url = f"{self.BASE_URL}/taxTypes"
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)
        return response.json()

    # We Can Add other methods as required by the VSDC API
def submit_invoice():
    settings = frappe.get_doc("ZRA Settings")
    zra_api = ZRAAPI(
        api_key=settings.api_key,
        device_serial_no=settings.device_serial_no,
        branch_id=settings.branch_id,
        tpin=settings.tpin
    )
    
    invoice_data = get_invoice_data()
    response = zra_api.submit_sales_invoice(invoice_data)
    
    if response.get('error'):
        frappe.throw(response['error'])

def get_invoice_data(self):
    items = []
    for item in self.items:
        items.append({
            "itemCode": item.item_code,
            "itemName": item.item_name,
            "qty": item.qty,
            "unitPrice": item.rate,
            "totalAmount": item.amount,
            "taxAmount": item.tax_amount,
            "discountAmount": item.discount_amount
        })

    invoice_data = {
        "invoiceNo": self.name,
        "issueDate": self.posting_date,
        "tpin": self.tpin,
        "bhfId": self.branch_id,
        "customerName": self.customer_name,
        "items": items,
        "totalAmount": self.total,
        "taxAmount": self.total_taxes_and_charges,
        "totalDiscount": self.total_discount,
        "paymentType": self.payment_type,
        "currency": self.currency,
        "exchangeRate": self.conversion_rate
    }
    return invoice_data
