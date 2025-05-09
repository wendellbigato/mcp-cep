from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("cep")

@mcp.tool()
async def echo(texto: str) -> str:
    """Repete o texto enviado."""
    return f"Você disse: {texto}"

@mcp.tool()
async def buscar_cep(cep: str) -> dict:
    """Consulta informações de um CEP brasileiro usando a API ViaCEP.

    Args:
        cep: Código de Endereçamento Postal no formato 01001000 ou 01001-000.

    Returns:
        Um dicionário com informações de endereço como rua, bairro, cidade e estado.
    """
    url = f"https://viacep.com.br/ws/{cep.replace('-', '')}/json/"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            if "erro" in data:
                return {"erro": "CEP não encontrado."}
            return data
    except Exception as e:
        return {"erro": f"Falha ao consultar o CEP: {str(e)}"}

@mcp.tool()
async def buscar_ceps_por_logradouro(uf: str, cidade: str, logradouro: str) -> list:
    """Busca todos os CEPs associados a um logradouro em uma cidade e estado.

    Args:
        uf: Sigla do estado (ex: SP, RJ)
        cidade: Nome da cidade (ex: São Paulo)
        logradouro: Nome da rua, avenida, praça etc (ex: Praça da Sé)

    Returns:
        Lista de dicionários com endereços que correspondem à busca.
    """
    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, dict) and "erro" in data:
                return [{"erro": "Endereço não encontrado."}]
            return data
    except Exception as e:
        return [{"erro": f"Erro ao buscar logradouro: {str(e)}"}]
