# 🚀 Deploy LIBRAS App - Guia Completo

**Status**: Ready for Production  
**Plataformas**: Vercel (Frontend) + Railway (Backend) + Neon (Database)  
**Tempo Estimado**: 30-45 minutos

---

## 📐 Arquitetura de Deploy

```
Internet
  │
  ├─→ Vercel (Frontend React)
  │   └─→ https://libras.vercel.app
  │
  ├─→ Railway (Backend FastAPI)
  │   └─→ https://libras-backend.railway.app/api/v1
  │
  └─→ Neon (PostgreSQL Database)
      └─→ postgresql://... (connection string)
```

---

## 🎯 Sequência de Deploy

### **PASSO 1: Preparação do Repositório (5 min)**

#### 1.1 Fazer push do código para GitHub

```bash
cd ~/Libras

# Verificar status
git status

# Adicionar configurações de deploy
git add vercel.json railway.json backend/.dockerignore .env.production
git commit -m "config: Add deployment configuration files for Vercel and Railway"
git push origin main
```

#### 1.2 Criar conta no GitHub (se não tiver)

- Acesse https://github.com
- Sign up
- Configure SSH key (recomendado)

---

### **PASSO 2: Setup do Banco de Dados (10 min)**

#### 2.1 Criar conta no Neon

```bash
# 1. Acesse https://console.neon.tech
# 2. Clique "Sign up"
# 3. Conecte com GitHub (recomendado)
# 4. Clique "Create project"
```

#### 2.2 Criar novo projeto

```
Nome do Projeto: libras-app
PostgreSQL Version: 16
Region: us-east-1 (mais próximo de você)
Clique "Create project"
```

#### 2.3 Copiar Connection String

```
No painel Neon:
1. Clique em "Connection string"
2. Copie a URL (tipo: postgresql://user:pass@host/db)
3. Salve em local seguro (vamos usar em Railway)

Exemplo:
postgresql://libras_user:abc123@ep-calm-wind-123456.us-east-1.neon.tech/libras_db
```

#### 2.4 Criar tabelas (Alembic migrations)

Vamos fazer isso automaticamente no Railway (no deploy).

---

### **PASSO 3: Deploy do Backend no Railway (15 min)**

#### 3.1 Criar conta no Railway

```bash
# 1. Acesse https://railway.app
# 2. Clique "Create new project"
# 3. Conecte com GitHub
# 4. Autorize Railway
```

#### 3.2 Criar novo projeto

```
1. Clique "+ New Project"
2. Selecione "Deploy from GitHub repo"
3. Autorize Railway para acessar GitHub
4. Procure por "libras"
5. Selecione o repositório
6. Clique "Deploy Now"
```

#### 3.3 Adicionar variáveis de ambiente

```
No painel do Railway:

1. Clique na aba "Variables"
2. Adicione:

DATABASE_URL = postgresql://[sua-string-do-neon]
SECRET_KEY = [gere uma chave aleatória segura de 32 caracteres]
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DEBUG = False
ALLOWED_ORIGINS = ["https://libras.vercel.app"]
REDIS_URL = redis://localhost:6379 (opcional por enquanto)
```

#### 3.4 Esperar o deploy

```
No Railway, você verá:
✓ Building
✓ Deploying
✓ Running

Quando ficar verde, seu backend está no ar!

URL será algo como:
https://libras-backend-production.railway.app
```

#### 3.5 Verificar se backend está funcionando

```bash
# Testar health check
curl https://libras-backend-production.railway.app/api/v1/health

# Esperado:
# {"status":"ok","service":"libras-app","version":"0.1.0"}

# Ver logs
railway logs
```

---

### **PASSO 4: Deploy do Frontend no Vercel (5 min)**

#### 4.1 Criar conta no Vercel

```bash
# 1. Acesse https://vercel.com
# 2. Clique "Sign Up"
# 3. Conecte com GitHub (recomendado)
# 4. Autorize Vercel
```

#### 4.2 Importar repositório

```
1. Clique "Add New..."
2. Selecione "Project"
3. Clique "Import Git Repository"
4. Procure por "libras"
5. Clique "Import"
```

#### 4.3 Configurar projeto

```
Framework: Vite
Root Directory: ./frontend
Build Command: npm run build
Output Directory: .next (deixe padrão)
```

#### 4.4 Adicionar variáveis de ambiente

```
Settings → Environment Variables

VITE_API_URL = https://libras-backend-production.railway.app/api/v1

Clique "Save"
```

#### 4.5 Deploy automático

```
Vercel fará deploy automaticamente quando você fizer push!

Acesse:
https://libras.vercel.app (ou seu domínio customizado)
```

#### 4.6 Verificar se frontend está funcionando

```bash
# 1. Acesse https://libras.vercel.app
# 2. Veja a página inicial
# 3. Tente fazer login com:
#    Email: student@libras.app
#    Senha: student123
# 4. Verifique se os cursos carregam
```

---

## 🔄 Workflow de Deploy Contínuo

Após configuração inicial, o deploy é automático:

```bash
# 1. Desenvolver localmente
git checkout -b feature/minha-feature

# 2. Fazer mudanças
# ... edite arquivos ...

# 3. Commit e push
git add .
git commit -m "feat: minha nova feature"
git push origin feature/minha-feature

# 4. Abrir Pull Request no GitHub
# (GitHub → Create Pull Request)

# 5. Merge para main
# git checkout main
# git merge feature/minha-feature
# git push origin main

# 6. Vercel e Railway fazem deploy automaticamente!
```

---

## 📊 Verificar Status dos Deploys

### Vercel
```bash
# Dashboard: https://vercel.com/dashboard
# Seu projeto: https://vercel.com/dashboard/libras
# Deployments: veja histórico de deploys
```

### Railway
```bash
# Dashboard: https://railway.app/dashboard
# Seu projeto: clique no projeto
# Deployments: veja histórico
# Logs: veja logs em tempo real
```

### Neon
```bash
# Dashboard: https://console.neon.tech
# Seu projeto: clique no projeto
# Query Editor: teste queries SQL
```

---

## 🔐 Segurança em Produção

### ✅ Checklist de Segurança

- [ ] `SECRET_KEY` é uma chave aleatória de 32+ caracteres
- [ ] `DEBUG=False` em todas as variáveis de produção
- [ ] `ALLOWED_ORIGINS` contém apenas seus domínios
- [ ] Não há `.env` ou secrets no repositório
- [ ] HTTPS está habilitado (automático em Vercel/Railway)
- [ ] Senha do banco de dados é forte
- [ ] Senha root do Neon foi alterada

### 🔑 Gerar SECRET_KEY Segura

```bash
# Linux/Mac
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# Windows PowerShell
[System.Convert]::ToBase64String([System.Security.Cryptography.RandomNumberGenerator]::GetBytes(32))
```

---

## 🧪 Teste o Deploy

### 1️⃣ Teste o Backend

```bash
# Health check
curl https://libras-backend-production.railway.app/api/v1/health

# API docs
https://libras-backend-production.railway.app/docs

# Fazer login
curl -X POST https://libras-backend-production.railway.app/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"student@libras.app","password":"student123"}'
```

### 2️⃣ Teste o Frontend

```bash
# Abra no navegador
https://libras.vercel.app

# Faça login
Email: student@libras.app
Senha: student123

# Verifique se:
- Header carrega
- Página inicial aparece
- Pode clicar em "Cursos"
- Cursos carregam da API
```

### 3️⃣ Teste o Database

```bash
# No Neon console
SELECT * FROM users;
SELECT * FROM courses;

# Deve retornar dados
```

---

## 🆘 Troubleshooting

### Erro: "Connection refused" no frontend

```
Problema: Frontend não consegue conectar ao backend

Solução:
1. Verifique se variável VITE_API_URL está correta em Vercel
2. Verifique se backend está rodando em Railway
3. Verifique ALLOWED_ORIGINS no backend (inclua seu domínio Vercel)
4. Limpe cache do navegador (Ctrl+Shift+Del)
5. Verifique na aba Network do DevTools as requisições
```

### Erro: "Database connection error" no backend

```
Problema: Backend não consegue conectar ao banco

Solução:
1. Verifique se DATABASE_URL está correta em Railway
2. Verifique string de conexão do Neon
3. Verifique se IP do Railway está permitido no Neon firewall
4. Teste conexão: psql "postgresql://..."
5. Verifique logs: railway logs
```

### Erro: "Migration failed"

```
Problema: Migrations do Alembic falharam no deploy

Solução:
1. Teste localmente: alembic upgrade head
2. Verifique se migrations estão no git
3. Verifique sintaxe SQL nas migrations
4. Rollback: alembic downgrade -1
5. Crie nova migration: alembic revision --autogenerate
```

### Vercel mostra 404

```
Problema: Frontend não renderiza (404 em todas as rotas)

Solução:
1. Verifique se output directory está correto (.next ou dist)
2. Verifique build command em Settings → Build
3. Verifique se package.json tem scripts corretos
4. Teste build localmente: npm run build
5. Limpe cache: vercel env pull → npm run build
```

---

## 📈 Monitoramento e Logs

### Ver logs do Backend (Railway)

```bash
# Tempo real
railway logs -f

# Últimas 100 linhas
railway logs

# Com filtro
railway logs | grep "ERROR"
```

### Ver logs do Frontend (Vercel)

```
Dashboard Vercel:
1. Clique no projeto
2. Deployments
3. Clique no deploy mais recente
4. Clique em "Logs"
```

### Monitorar Banco de Dados (Neon)

```
Console Neon:
1. Clique no projeto
2. Query Editor
3. Execute: SELECT * FROM pg_stat_statements;
```

---

## 🌍 Domínio Customizado

### Adicionar domínio customizado no Vercel

```
1. Vercel Dashboard → Seu projeto
2. Settings → Domains
3. Clique "+ Add"
4. Digite seu domínio (libras.com.br)
5. Siga instruções para apontar DNS
6. Aguarde propagação (até 24h)
```

### Adicionar domínio customizado no Railway

```
1. Railway Dashboard → Seu projeto
2. Settings → Domains
3. Clique "+ Add Domain"
4. Digite seu domínio (api.libras.com.br)
5. Siga instruções DNS
```

---

## 💰 Custos Estimados (Mensal)

| Serviço | Plano | Custo |
|---------|-------|-------|
| **Vercel** | Hobby | $0 |
| **Railway** | Pay-as-you-go | ~$5-10 |
| **Neon** | Starter | $0-15 |
| **Total** | - | **~$0-25/mês** |

*Preços podem variar. Verifique documentação oficial.*

---

## ✅ Checklist de Deploy Final

- [ ] Repository no GitHub com todos arquivos
- [ ] Neon criado e connection string copiada
- [ ] Railway criado e variáveis configuradas
- [ ] Backend deployado e rodando
- [ ] Vercel criado e variáveis configuradas
- [ ] Frontend deployado e rodando
- [ ] Testes de conectividade passaram
- [ ] Logs foram verificados
- [ ] Banco de dados foi criado com migrations
- [ ] Dados de teste foram seedados
- [ ] Documentação atualizada
- [ ] URLs são conhecidas e funcionando

---

## 🎉 Pronto!

Sua LIBRAS App está no ar! 🚀

```
Frontend: https://libras.vercel.app
Backend:  https://libras-backend-production.railway.app/api/v1
Database: Neon PostgreSQL (gerenciado)

Próximos passos:
1. Compartilhe o link com stakeholders
2. Colete feedback
3. Implemente Phase 2 (exercícios)
4. Configure CI/CD com GitHub Actions
5. Implemente monitoramento com Sentry/DataDog
```

---

## 📞 Links Úteis

| Recurso | Link |
|---------|------|
| **Vercel Docs** | https://vercel.com/docs |
| **Railway Docs** | https://docs.railway.app |
| **Neon Docs** | https://neon.tech/docs/introduction |
| **FastAPI Deploy** | https://fastapi.tiangolo.com/deployment |
| **React Deploy** | https://vitejs.dev/guide/static-deploy.html |

---

**Última atualização**: 2024-07-05  
**Versão**: 0.1.0 MVP

Feito com ❤️ para a comunidade LIBRAS
