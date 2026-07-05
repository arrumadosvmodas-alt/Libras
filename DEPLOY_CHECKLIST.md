# ✅ Deploy LIBRAS App - Checklist Interativo

Siga esta lista para fazer deploy completo em produção!

---

## 📋 PRÉ-REQUISITOS

- [ ] Conta GitHub (https://github.com)
- [ ] Conta Vercel (https://vercel.com) - conectada com GitHub
- [ ] Conta Railway (https://railway.app) - conectada com GitHub
- [ ] Conta Neon (https://neon.tech) - para banco de dados
- [ ] Repositório `libras` no GitHub

---

## 🔧 FASE 1: Preparação (5 min)

### GitHub Setup
```bash
cd ~/Libras
```

- [ ] Repositório criado no GitHub: `github.com/SEU_USER/libras`
- [ ] Arquivo `vercel.json` criado ✓
- [ ] Arquivo `railway.json` criado ✓
- [ ] Arquivo `.env.production` criado ✓
- [ ] Arquivo `DEPLOY.md` criado ✓
- [ ] Arquivo `backend/.dockerignore` criado ✓

### Push para GitHub
```bash
git add -A
git commit -m "config: Add deployment files"
git push origin main
```

- [ ] Todos os arquivos estão no GitHub
- [ ] Verifique em https://github.com/SEU_USER/libras

---

## 🗄️ FASE 2: Database (Neon) - 10 min

### Criar Conta
- [ ] Acesse https://console.neon.tech
- [ ] Sign up com GitHub
- [ ] Autorize permissões

### Criar Projeto
- [ ] Clique "Create project"
- [ ] Nome: `libras-app`
- [ ] Versão: PostgreSQL 16
- [ ] Região: us-east-1 (ou mais próxima)
- [ ] Clique "Create project"

### Copiar Connection String
- [ ] Vá para "Connection String"
- [ ] Copie a URL completa
- [ ] Salve em um arquivo seguro (você vai precisar no Railway)

```
Exemplo:
postgresql://libras_user:***@ep-cool-wind-123.us-east-1.neon.tech/libras_db
```

- [ ] String copiada ✓

---

## 🚀 FASE 3: Backend (Railway) - 15 min

### Criar Conta
- [ ] Acesse https://railway.app
- [ ] Clique "Create new project"
- [ ] Autorize Railway para acessar seu GitHub

### Deploy do Repositório
- [ ] Clique "Deploy from GitHub repo"
- [ ] Procure por "libras"
- [ ] Selecione seu repositório
- [ ] Clique "Deploy Now"
- [ ] Espere a build completar (pode levar 3-5 min)

**Status**: Procure por ✓ "Running" em verde

### Configurar Variáveis de Ambiente
- [ ] Clique na aba "Variables"
- [ ] Adicione `DATABASE_URL`: [cole a string do Neon]
- [ ] Gere SECRET_KEY: `python3 -c "import secrets; print(secrets.token_urlsafe(32))"`
- [ ] Adicione `SECRET_KEY`: [cola a chave gerada]
- [ ] Adicione `DEBUG`: `False`
- [ ] Adicione `ALLOWED_ORIGINS`: `["https://libras.vercel.app"]`
- [ ] Clique "Save"

### Aguardar Deployment
- [ ] Status mostra "Running" em verde ✓
- [ ] Clique em "Deployments"
- [ ] Copie a URL do deployment
- [ ] Salve a URL (você vai precisar no Vercel)

```
Exemplo:
https://libras-backend-production.railway.app
```

### Testar Backend
```bash
# Execute no terminal:
curl https://libras-backend-production.railway.app/api/v1/health
```

- [ ] Recebe resposta: `{"status":"ok","service":"libras-app"}`

---

## 🌐 FASE 4: Frontend (Vercel) - 5 min

### Criar Conta
- [ ] Acesse https://vercel.com
- [ ] Clique "Sign Up"
- [ ] Escolha "Continue with GitHub"
- [ ] Autorize Vercel

### Importar Repositório
- [ ] Clique "Add New..." → "Project"
- [ ] Clique "Import Git Repository"
- [ ] Procure por "libras"
- [ ] Clique "Import"

### Configurar Build
- [ ] Framework: Vite (automático)
- [ ] Root Directory: (deixe em branco)
- [ ] Build Command: `cd frontend && npm install && npm run build`
- [ ] Output Directory: `frontend/dist`
- [ ] Clique "Deploy"

**Status**: Procure por ✓ "Ready" em azul

### Configurar Variáveis de Ambiente
- [ ] Clique "Settings" → "Environment Variables"
- [ ] Adicione `VITE_API_URL`
- [ ] Valor: `https://libras-backend-production.railway.app/api/v1`
- [ ] Clique "Save"

### Redeploy
- [ ] Volte para "Deployments"
- [ ] Clique "Redeploy Latest"
- [ ] Aguarde ficar verde

### Copiar URL do Frontend
- [ ] URL estará em: `https://libras.vercel.app` ou seu domínio customizado
- [ ] Salve a URL

---

## 🧪 FASE 5: Testes - 5 min

### Testar Frontend
```
1. Acesse: https://libras.vercel.app
```

- [ ] Página inicial carrega
- [ ] Vê o logo "LIBRAS App"
- [ ] Vê as features na home
- [ ] Botão "Começar Agora" é clicável

### Testar Navegação
```
1. Clique em "Cursos" (no header ou no botão)
```

- [ ] Página de cursos carrega
- [ ] Vê pelo menos 1 curso listado
- [ ] Curso tem imagem placeholder

### Testar Login
```
1. Clique em "Login"
2. Email: student@libras.app
3. Senha: student123
4. Clique "Login"
```

- [ ] Login é bem-sucedido
- [ ] Redireciona para página de cursos
- [ ] Vê mensagem de boas-vindas ou user icon no header
- [ ] Pode clicar em um curso

### Testar API Diretamente
```bash
# Health check
curl https://libras-backend-production.railway.app/api/v1/health
```

- [ ] Retorna: `{"status":"ok","service":"libras-app","version":"0.1.0"}`

```bash
# API Docs
curl https://libras-backend-production.railway.app/docs
```

- [ ] Acessa a documentação Swagger

---

## 📊 FASE 6: Verificação Final

### Status dos Serviços
- [ ] **Frontend**: https://libras.vercel.app ✓ Funcionando
- [ ] **Backend**: https://libras-backend-production.railway.app/api/v1/health ✓ Funcionando
- [ ] **Database**: Neon criado e conectado ✓ Funcionando

### URLs Salvas
- [ ] Frontend URL: `_________________________`
- [ ] Backend URL: `_________________________`
- [ ] Database URL: `_________________________`

### Variáveis de Ambiente
- [ ] SECRET_KEY: Salvo e seguro ✓
- [ ] DATABASE_URL: Salvo e seguro ✓
- [ ] VITE_API_URL: Configurado em Vercel ✓
- [ ] ALLOWED_ORIGINS: Configurado em Railway ✓

---

## 🔐 Segurança Final

- [ ] SECRET_KEY é uma chave aleatória segura (não compartilhado)
- [ ] DEBUG=False em Railway
- [ ] Senha do Neon é forte e segura
- [ ] Não há `.env` ou secrets no repositório Git
- [ ] ALLOWED_ORIGINS contém apenas domínio vercel.app

---

## 📱 Teste em Dispositivos

- [ ] Teste no desktop (Chrome, Firefox)
- [ ] Teste no mobile (iPhone, Android)
- [ ] Responsivo funciona bem
- [ ] Buttons são clicáveis no mobile

---

## 🎉 SUCESSO!

- [ ] App está deployada em produção ✓
- [ ] Todos os testes passaram ✓
- [ ] URLs funcionando ✓
- [ ] Pronto para compartilhar! ✓

---

## 📝 Próximos Passos

Após deployment bem-sucedido:

1. **Fase 2**: Implementar exercícios interativos
2. **Fase 3**: Adicionar streak e gamificação
3. **Fase 4**: Implementar pagamento com Stripe
4. **Conteúdo**: Gravar aulas com professores surdos
5. **Comunidade**: Validar com comunidade surda brasileira

---

## 🆘 Precisa de Ajuda?

### Problemas Comuns
- [ ] Frontend não carrega → Verifique VITE_API_URL em Vercel
- [ ] Backend não responde → Verifique DATABASE_URL em Railway
- [ ] Login não funciona → Verifique ALLOWED_ORIGINS em Railway
- [ ] Migrations falharam → Verifique DATABASE_URL e permissões no Neon

### Recursos
- 📖 [DEPLOY.md](./DEPLOY.md) - Guia completo
- 📖 [DEPLOY_STEPS.md](./DEPLOY_STEPS.md) - Guia rápido
- 🏗️ [ARCHITECTURE.md](./ARCHITECTURE.md) - Entender a arquitetura
- 📚 [README.md](./README.md) - Documentação geral

---

## 🎯 Status Geral

```
GitHub:     ✓ Repositório
Vercel:     ✓ Frontend
Railway:    ✓ Backend  
Neon:       ✓ Database

Status Global: ✅ DEPLOYADA COM SUCESSO!
```

---

**Última atualização**: 2024-07-05  
**Versão**: 0.1.0 MVP  
**Status**: Ready for Production 🚀

Parabéns! Sua LIBRAS App está no ar! 🎉
