from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    host: str = "0.0.0.0"
    port: str = "8080"
    debug: bool = False
    stark_project_id: str
    enviroment: str = "sandbox"
    private_key: str
    transfer_tax_id: str
    transfer_account_name: str
    transfer_bank_code: str
    transfer_branch_code:str
    transfer_account_number: str
    transfer_account_type: str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()