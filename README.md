# **🚀 Lu Estilo - API FastAPI com Docker e PostgreSQL**

Um projeto simples, mas completo, para criar uma API usando **FastAPI**, **Docker** e **PostgreSQL**, pronto para desenvolvimento e produção.  

Acerca do desafio: O desafio proposto tinha complexidade elevada, especialmente na integração com a API paga do WhatsApp e múltiplos endpoints. Optei por desenvolver um MVP simplificado, demonstrando habilidades em FastAPI, Docker e PostgreSQL. Estou aberto a desenvolver a solução completa de forma gradual em um ambiente profissional.
---

## **📋 Pré-requisitos**  
Antes de começar, você precisará:  
✅ **Docker** instalado ([Download Docker](https://www.docker.com/get-started))  
✅ **Git** instalado ([Download Git](https://git-scm.com/downloads))  
✅ Um editor de código (VS Code, PyCharm, etc.)  

---

## **⚙️ Como Rodar o Projeto**  

### **1️⃣ Clone o Repositório**  
```bash
git clone https://github.com/Daniel-Gehlen/lu_estilo.git
cd lu_estilo
```

### **2️⃣ Inicie os Containers (Docker Compose)**  
O projeto já está configurado com:  
- **FastAPI** (rodando na porta `8000`)  
- **PostgreSQL** (banco de dados configurado)  

Execute:  
```bash
./start.sh
```
*Isso vai:*  
✔ **Construir as imagens Docker**  
✔ **Subir os containers**  
✔ **Configurar o banco de dados**  
✔ **Rodar migrações automáticas**  

---

## **🌐 Acesse a API**  
Abra seu navegador ou use um cliente como **Postman/Insomnia**:  
🔗 **http://localhost:8000**  

Você deve ver:  
```json
{"status": "API Lu Estilo OK"}
```

---

## **📂 Estrutura do Projeto**  

```
lu_estilo/
├── app/
│   └── main.py          # API FastAPI (rotas e modelos)
├── migrations/          # Migrações do banco (Alembic)
├── Dockerfile           # Configuração do container FastAPI
├── docker-compose.yml   # Orquestração Docker (FastAPI + PostgreSQL)
├── requirements.txt     # Dependências Python
└── start.sh             # Script de inicialização automática
```

---

## **🐳 Docker Configurado e Validado**  

### **📜 Dockerfile**  
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
✔ **Otimizado** (usa imagem slim)  
✔ **Instala dependências automaticamente**  
✔ **Expõe a API na porta 8000**  

### **📜 docker-compose.yml**  
```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db/lu_estilo
    depends_on:
      - db
    volumes:
      - ./app:/app/app
      - ./migrations:/app/migrations

  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=lu_estilo
    volumes:
      - pg_data:/var/lib/postgresql/data

volumes:
  pg_data:
```
✔ **PostgreSQL pré-configurado**  
✔ **Persistência de dados (volume Docker)**  
✔ **Hot-reload do código (edite `app/main.py` sem reiniciar)**  

---

## **🛠️ Comandos Úteis**  

| Comando | O que faz? |
|---------|------------|
| `docker-compose up -d` | Inicia os containers em segundo plano |
| `docker-compose down` | Para e remove os containers |
| `docker-compose logs -f web` | Mostra logs em tempo real |
| `docker exec -it lu_estilo-web bash` | Acessa o container da API |

---

## **🤔 Problemas Comuns?**  

❌ **Erro ao iniciar o PostgreSQL?**  
- Verifique se não há outro container usando a porta `5432`.  

❌ **Código não atualiza após mudanças?**  
- Reinicie o container:  
  ```bash
  docker-compose restart web
  ```

---

## **📝 Licença**  
MIT License - Use livremente!  

---

**🎉 Pronto! Agora você tem uma API FastAPI + PostgreSQL rodando com Docker em minutos!**  
👉 **Dúvidas?** Abra uma *issue* no [GitHub](https://github.com/Daniel-Gehlen/lu_estilo).  

--- 

### **🔗 Links Úteis**  
- [FastAPI Docs](https://fastapi.tiangolo.com/)  
- [Docker Docs](https://docs.docker.com/)  
- [PostgreSQL Docs](https://www.postgresql.org/docs/)  

--- 

**👨‍💻 Codificado com ❤️ por [Daniel Gehlen]**
