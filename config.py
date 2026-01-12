
from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):

    

    zoho_client_id :str
    zoho_client_secret : str
    zoho_refresh_token : str

    model_config =SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings= Settings()
