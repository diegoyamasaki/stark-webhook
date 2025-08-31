from unittest import mock

import pytest

from main import app as service_app


@pytest.fixture
def client():
    service_app.config['TESTING'] = True # Enable testing mode
    with service_app.test_client() as client:
        yield client # Yield the client for use in tests

@pytest.fixture
def request_body():
    return  {
            "event": {
                "created": "2024-01-31T21:15:17.463956+00:00",
                "id": "6046987522670592",
                "log": {
                "created": "2024-01-31T21:15:16.852263+00:00",
                "errors": [],
                "id": "5244688441278464",
                "invoice": {
                    "amount": 10000,
                    "brcode": "00020101021226890014br.gov.bcb.pix2567brcode-h.sandbox.starkbank.com/v2/ee87e7ce19544b11be5a6de65b97091a5204000053039865802BR5925Stark Bank S.A. - Institu6009Sao Paulo62070503***630442BE",
                    "created": "2024-01-31T21:15:16.701209+00:00",
                    "descriptions": [
                        {
                        "key": "Product A",
                        "value": "R$10,00"
                        },
                        {
                        "key": "Taxes",
                        "value": "R$100,00"
                        }
                    ],
                    "discountAmount": 0,
                    "discounts": [
                        {
                        "due": "2024-11-25T17:59:26+00:00",
                        "percentage": 10.5
                        },
                        {
                        "due": "2024-11-29T17:59:26+00:00",
                        "percentage": 5
                        }
                    ],
                    "due": "2024-11-30T02:06:26.249976+00:00",
                    "expiration": 1,
                    "fee": 0,
                    "fine": 2.5,
                    "fineAmount": 0,
                    "id": "5807638394699776",
                    "interest": 1.3,
                    "interestAmount": 0,
                    "link": "https://starkv2.sandbox.starkbank.com/invoicelink/ee87e7ce19544b11be5a6de65b97091a",
                    "name": "Iron Bank S.A.",
                    "nominalAmount": 10000,
                    "pdf": "https://sandbox.api.starkbank.com/v2/invoice/ee87e7ce19544b11be5a6de65b97091a.pdf",
                    "rules": [],
                    "splits": [],
                    "status": "paid",
                    "tags": [
                    "war supply",
                    "invoice #1234"
                    ],
                    "taxId": "20.018.183/0001-80",
                    "transactionIds": [],
                    "updated": "2024-01-31T21:15:16.852309+00:00"
                },
                "type": "credited"
                },
                "subscription": "invoice",
                "workspaceId": "6341320293482496"
            }
        }

def test_request_invoice(client, request_body):
    with mock.patch('main.send_transfer_from_invoice') as mock_send_transfer_from_invoice:
        client.post('/webhook', json=request_body, headers={"teste": "teste"})
        assert mock_send_transfer_from_invoice.called
        
