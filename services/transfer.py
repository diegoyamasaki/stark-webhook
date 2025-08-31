import starkbank

from common.logger import logging
from common.provider import init_starkbank
from common.settings import settings


def send_transfer_from_invoice(data, headers):
    init_starkbank()
    event = starkbank.event.parse(
            content=data.decode("utf-8"),
            signature=headers.get("Digital-Signature")
            )
    if event.log.invoice.status != "paid":
        logging.info(
            f"ignore invoice status {event.log.invoice.status}",
        )
        return
    transfers = starkbank.transfer.create(
        [
            starkbank.Transfer(
                amount=(event.log.invoice.amount - event.log.invoice.fee),
                tax_id=settings.transfer_tax_id,
                name=settings.transfer_account_name,
                bank_code=settings.transfer_bank_code,
                branch_code=settings.transfer_branch_code,
                account_number=settings.transfer_account_number,
                account_type=settings.transfer_account_type
            )
        ]
    )
    for transfer in transfers:
        logging.info(transfer)
    
    