from http import HTTPStatus

from flask import Flask, Response, request
from starkcore.error import InvalidSignatureError, StarkError

from common.logger import logging
from common.settings import settings
from services.transfer import send_transfer_from_invoice

app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def handle_webhook():
    try:
        send_transfer_from_invoice(data=request.data, headers=request.headers)
    except InvalidSignatureError as e:
        logging.info("Invalid Signarture", exc_info=e)
        return Response(status=HTTPStatus.BAD_REQUEST)
    except StarkError as e:
        logging.error(f"Integration Stark Error {e.message}", exc_info=e)
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
    except Exception as e:
        logging.error(f"Webhook Internal Error {e}", exc_info=e)
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
    return Response(status=HTTPStatus.OK)


if __name__ == '__main__':
    app.run(host=settings.host, port=settings.port, debug=settings.debug)