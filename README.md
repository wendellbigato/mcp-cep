# MCP-CEP

Servidor MCP para consulta de CEPs usando a API pública do [ViaCEP](https://viacep.com.br).  
Compatível com [Goose](https://block.github.io/goose/) como extensão de linha de comando (Command-line Extension).

---

### 👤 Autor

**Wendell Barreto**  
[https://github.com/wendellbigato](https://github.com/wendellbigato)  


---

## 🚀 Instalação

### 1. Clone este repositório

```bash
git clone https://github.com/wendellbigato/mcp-cep.git
cd mcp-cep
````

> Altere a URL acima para a real quando publicar.

---

### 2. Crie e ative o ambiente virtual

```bash
python3.11 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate.bat  # Windows
```

---

### 3. Instale as dependências com `uv` ou `pip`

Usando [uv](https://github.com/astral-sh/uv):

```bash
uv pip install -e ".[cli]"
```

Ou com pip normal:

```bash
pip install -e ".[cli]"
```

---

## 🧩 Configurando como extensão no Goose

1. Execute:

```bash
goose configure
```

2. Selecione `Add Extension`

3. Escolha `Command-line Extension`

4. Preencha os campos:

| Campo              | Valor                                                                     |
| ------------------ | ------------------------------------------------------------------------- |
| **Extension name** | `mcp-cep`                                                                 |
| **Command to run** | `/caminho/completo/para/uv --directory /caminho/para/mcp-cep run main.py` |
| **Timeout**        | `300`                                                                     |
| **Environment**    | *(em branco, ou personalize se necessário)*                               |

Use `which uv` e `pwd` para encontrar os caminhos corretos.

---

## ✅ Como testar no Goose

Após configurar, inicie:

```bash
goose session --with-extension mcp-cep
```

E envie comandos como:

```
Repita: Olá!
Qual o endereço do CEP 01001000?
```

---

## 🧰 Ferramentas disponíveis

* `echo(texto: str)`: repete o texto enviado.
* `buscar_cep(cep: str)`: consulta informações de endereço via ViaCEP.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
