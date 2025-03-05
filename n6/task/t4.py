"""
API para validação e processamento de objetos Item.

Este módulo define um endpoint utilizando FastAPI para validar e
processar objetos do tipo Item, com geração automática de UUID.
"""
from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()


class Item(BaseModel):
    """
    Modelo Pydantic para o objeto Item.

    Atributos:
        nome (str): Nome do item com no máximo 25 caracteres.
        valor (float): Valor do item.
        data (str): Data no formato YYYY-MM-DD, não superior à data atual.
        uuid (str): UUID gerado automaticamente (adicionado dinamicamente).
    """
    nome: str = Field(..., max_length=25,
                      description="Nome do item (máx. 25 caracteres)")
    valor: float = Field(..., description="Valor numérico do item")
    data: str = Field(..., description="Data no formato YYYY-MM-DD")

    @field_validator("data")
    @classmethod
    def validar_data(cls, v: str) -> str:
        """Valida se a data fornecida está no formato correto e não é superior à data atual."""
        try:
            data_formatada = datetime.strptime(v, "%Y-%m-%d").date()
            if data_formatada > datetime.now().date():
                raise ValueError("A data não pode ser superior à data atual.")
            return v
        except ValueError as e:
            raise ValueError(
                "Formato de data inválido. Use YYYY-MM-DD.") from e


@app.post("/processar_item/", response_model=Item)
def processar_item(item: Item) -> Item:
    """
    Endpoint para processar e validar o objeto Item.

    Args:
        item (Item): Objeto Item recebido na requisição.

    Returns:
        Item: Objeto Item validado com o campo uuid adicionado.
    """
    item_dict = item.model_dump()
    item_dict["uuid"] = str(uuid4())
    return Item(**item_dict)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("n6.task.t4:app", host="127.0.0.1", port=8000, reload=True)

# executar: python -m uvicorn n6.task.t4:app --reload
# acesso ao FastAPI - Swagger UI <http://127.0.0.1:8000/docs>
