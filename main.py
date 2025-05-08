from cep import mcp

if __name__ == "__main__":
    # Inicia o servidor no modo stdin/stdout
    mcp.run(transport="stdio")


#import uvicorn

#if __name__ == "__main__":
#    uvicorn.run("cep:app", host="127.0.0.1", port=8000, reload=True)

#Comando: uvicorn cep:app --host 127.0.0.1 --port 8000