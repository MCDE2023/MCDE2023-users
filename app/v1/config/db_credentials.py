from dataclasses import dataclass, field
import os


def get_env_variable(var_name: str, default=None) -> str:
    """Esegui il parsing di una variabile d'ambiente.

    Args:
        var_name (str): Nome della variabile d'ambiente.
        default (str, optional): Valore di default.

    Raises:
        EnvironmentError: Se non trova la variabile d'ambiente e il default non è definito.

    Returns:
        str: Il valore della variabile d'ambiente.

    """
    return os.getenv(var_name)
    # try:
    #     # Restituisce il valore della variabile d'ambiente

    #     return os.environ[var_name]
    # # Se non esiste
    # except KeyError as e:
    #     # Se è definito un valore di default lo restituisce
    #     if default is not None:
    #         return default
    #     raise EnvironmentError(
    #         f"La variabile {var_name} non è stata impostata correttamente."
    #     )


@dataclass(frozen=True, slots=True)
class DynamoCredentials:
    """Definisce il modello delle credenziali per la connessione a DynamoDB."""

    awsAccessKeyId: str = field(default=get_env_variable("AWS_ACCESS_KEY_ID"))
    awsSecretAccessKey: str = field(default=get_env_variable("AWS_SECRET_ACCESS_KEY"))
    endpointUrl: str = field(default=get_env_variable("AWS_ENDPOINT_URL"))
    regionName: str = field(default=get_env_variable("DYNAMODB_REGION"))
    tableName: str = field(default=get_env_variable("DYNAMODB_TABLE"))


if __name__ == "__main__":
    credentials = DynamoCredentials()
    print(credentials)
