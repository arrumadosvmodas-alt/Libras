# ⚡ Deploy LIBRAS App - Guia Rápido (5 Passos)

**Tempo Total**: ~45 minutos  
**Dificuldade**: Fácil  

---

## 📌 O que você vai fazer

```
GitHub         Vercel          Railway         Neon
   ↓             ↓               ↓              ↓
 Repositório  Frontend        Backend      Database
   (código)    (React)       (FastAPI)   (PostgreSQL)
```

---

## ✅ PASSO 1: Preparar o GitHub (5 min)

### 1.1 Você precisa de:
- [ ] Conta GitHub (https://github.com)
- [ ] Seu repositório `libras` no GitHub

### 1.2 Se o repositório não está no GitHub:

```bash
cd ~/Libras

# Criar repositório no GitHub:
# 1. Acesse https://github.com/new
# 2. Nome: "libras"
# 3. Clique "Create repository"

# Adicionar origin remota
git remote add origin https://github.com/SEU_USERNAME/libras.git
git branch -M main
git push -u origin main
```

### 1.3 Fazer push dos arquivos de deploy

```bash
git push origin main
```

✅ **PRONTO!** Código está no GitHub

---

## ✅ PASSO 2: Setup do Banco (Neon) - 10 min

### 2.1 Criar conta Neon

```
1. Acesse: https://console.neon.tech
2. Clique "Sign Up"
3. Escolha "Sign up with GitHub"
4. Autorize
```

### 2.2 Criar projeto

```
1. Clique "Create project"
2. Nome: "libras-app"
3. PostgreSQL: 16
4. Region: us-east-1 (ou a mais próxima)
5. Clique "Create project"
```

### 2.3 Copiar string de conexão

```
1. No painel Neon, procure por "Connection string"
2. Copie algo assim:
   postgresql://libras_user:***@ep-cool-wind-12345.us-east-1.neon.tech/libras_db
3. Cole em um arquivo de texto (vamos usar no Railway)
```

✅ **PRONTO!** Banco de dados está criado

---

## ✅ PASSO 3: Deploy Backend (Railway) - 15 min

### 3.1 Criar conta Railway

```
1. Acesse: https://railway.app
2. Clique "Create new project"
3. Escolha "Deploy from GitHub repo"
4. Autorize Railway a acessar seu GitHub
```

### 3.2 Selecionar repositório

```
1. Procure por "libras"
2. Selecione seu repositório
3. Clique "Deploy Now"
```

### 3.3 Adicionar variáveis de ambiente

```
No painel Railway, vá para "Variables"

Adicione estas variáveis:

DATABASE_URL = [Cole a string do Neon aqui]
SECRET_KEY = [Gere uma chave aleatória]
DEBUG = False
ALLOWED_ORIGINS = ["https://libras.vercel.app"]

Clique "Save"
```

#### Gerar SECRET_KEY (Python):
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copie o resultado e adicione como SECRET_KEY.

### 3.4 Esperar deploy

```
Railway vai:
1. ✓ Build a imagem Docker
2. ✓ Fazer deploy do backend
3. ✓ Rodar migrations do Alembic
4. ✓ Ficar pronto!

Quando aparecer "Running" em verde, está pronto!
```

### 3.5 Copiar URL do Backend

```
No painel Railway, procure por "Deployments"
Copie a URL (será algo como):
https://libras-backend-production.railway.app

Cole em um arquivo (vamos usar no Vercel)
```

✅ **PRONTO!** Backend está deployado

---

## ✅ PASSO 4: Deploy Frontend (Vercel) - 5 min

### 4.1 Criar conta Vercel

```
1. Acesse: https://vercel.com
2. Clique "Sign Up"
3. Escolha "Continue with GitHub"
4. Autorize
```

### 4.2 Importar repositório

```
1. Clique "Add New..." → "Project"
2. Clique "Import Git Repository"
3. Procure "libras"
4. Clique "Import"
```

### 4.3 Configurar projeto

```
Framework: Vite (detecta automaticamente)
Root Directory: ./
Build Command: cd frontend && npm install && npm run build
Output Directory: frontend/dist
```

Deixe os outros padrões.

### 4.4 Adicionar variável de ambiente

```
Vá para "Environment Variables"

Adicione:
VITE_API_URL = [Cole a URL do Railway aqui]

Exemplo:
VITE_API_URL = https://libras-backend-production.railway.app/api/v1

Clique "Save"
```

### 4.5 Deploy automático

```
Vercel vai fazer deploy automaticamente!
Espere as luzes ficarem verdes.

Sua URL será:
https://libras.vercel.app
```

✅ **PRONTO!** Frontend está deployado

---

## ✅ PASSO 5: Testar Deploy - 5 min

### 5.1 Testar Frontend

```
1. Abra: https://libras.vercel.app
2. Veja a página inicial
3. Clique em "Cursos"
4. Você deve ver os cursos carregados
```

### 5.2 Testar Login

```
1. Clique em "Login" ou "Registrar"
2. Teste com conta:
   Email: student@libras.app
   Senha: student123
3. Você deve estar logado
4. Clique em "Cursos" novamente
```

### 5.3 Testar API Backend

```bash
# Abra o terminal e execute:
curl https://libras-backend-production.railway.app/api/v1/health

# Você deve ver:
# {"status":"ok","service":"libras-app","version":"0.1.0"}
```

### 5.4 Verificar Logs

```
Se algo der errado, verifique logs:

Railway:
- Clique no seu projeto
- Deployments
- Clique no deploy
- Veja "Build Logs" ou "Deploy Logs"

Vercel:
- Clique no seu projeto
- Deployments
- Clique no deploy mais recente
- Veja os logs
```

✅ **PRONTO!** Seu app está no ar! 🚀

---

## 📊 Resumo do que foi deployado

| Componente | Plataforma | URL |
|-----------|-----------|-----|
| **Frontend** | Vercel | https://libras.vercel.app |
| **Backend** | Railway | https://libras-backend-*.railway.app |
| **Database** | Neon | postgresql://... |

---

## 🔄 Próximas Deploys (automáticas!)

```bash
# Depois de configurar, é só fazer:
git add .
git commit -m "feat: sua mudança"
git push origin main

# Vercel e Railway fazem deploy automaticamente!
```

---

## 🆘 Problemas Comuns?

### Frontend mostra 404 em todas as páginas
```
Solução:
1. Vai para Vercel Dashboard
2. Seu projeto → Settings → Build & Development
3. Build Command: cd frontend && npm install && npm run build
4. Output Directory: frontend/dist
5. Clique "Deploy" novamente
```

### Frontend não conecta ao backend
```
Solução:
1. Vercel Dashboard → Environment Variables
2. Verifique se VITE_API_URL está correto
3. Deve ser: https://libras-backend-*.railway.app/api/v1
4. Redeploy o frontend
```

### Backend da erro de banco de dados
```
Solução:
1. Railway Dashboard → Variables
2. Copie a string de conexão do Neon novamente
3. Cole em DATABASE_URL
4. Clique "Save"
5. Railway redeploy automaticamente
```

---

## 📞 Links Úteis

- **Vercel**: https://vercel.com/dashboard
- **Railway**: https://railway.app/dashboard
- **Neon**: https://console.neon.tech
- **GitHub**: https://github.com

---

## ✨ Pronto!

Sua LIBRAS App está no ar! 🎉

Compartilhe as URLs:
```
Frontend: https://libras.vercel.app
API Docs: https://libras-backend-*.railway.app/docs
```

Próximo passo: **Implementar Phase 2** (exercícios, progresso, etc)

---

**Tempo total: ~45 minutos**  
**Dificuldade: Fácil**  
**Resultado: App em produção! 🚀**
