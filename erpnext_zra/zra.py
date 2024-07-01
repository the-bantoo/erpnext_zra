import requests, frappe
import json

class ZRAAPI:
    BASE_URL = 

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
    def get_device_status(self):
        url = f"{self.BASE_URL}/device/status"
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

    def get_invoice_status(self, invoice_no):
        url = f"{self.BASE_URL}/invoice/status"
        payload = {
            "invoiceNo": invoice_no
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response.json()

    def get_sales_summary(self, start_date, end_date):
        url = f"{self.BASE_URL}/sales/summary"
        payload = {
            "startDate": start_date,
            "endDate": end_date
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)
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
        "exchangeRate": self.conversion_rate,
        "remarks": self.remarks
    }
    return invoice_data
