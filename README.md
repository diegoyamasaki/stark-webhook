You will receive an invitation to join a Sandbox account in your email as an Admin. Create a Project and Webhook endpoint for that account and develop a simple app integration using whichever language you prefer that:

    1. Issues 8 to 12 Invoices every 3 hours to random people for 24 hours (our Sandbox emulation environment will make sure some of those are automatically paid);
    2. Receives the webhook callback of the Invoice credit and sends the received amount (minus eventual fees) to the following account using a Transfer: 
        a. bank code: 20018183
        b. branch: 0001
        c. account: 6341320293482496
        d. name: Stark Bank S.A.
        e. tax ID: 20.018.183/0001-80
        f. account type: payment


To deploy:
gcloud run deploy --source .