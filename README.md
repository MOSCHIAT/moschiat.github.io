# 🎨 MOSCHIAT Portfolio

[![Deploy](https://github.com/MOSCHIAT/moschiat.com/workflows/Deploy%20site%20to%20GitHub%20Pages/badge.svg)](https://github.com/MOSCHIAT/moschiat.com/actions)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fmoschiat.com)](https://moschiat.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Portfólio pessoal de Paulo Marques - Desenvolvedor, Designer e Artista Digital

🌐 **[moschiat.com](https://moschiat.com)**

---

## 📋 Sobre o Projeto

Site pessoal e portfólio profissional apresentando trabalhos em desenvolvimento Python, modelagem 3D, fotografia, design gráfico e projetos multidisciplinares.

### ✨ Características

- 🎨 Design moderno e responsivo
- 🔒 Área protegida com autenticação
- ⚡ Performance otimizada
- 🌓 Animações suaves e interativas
- 📱 Mobile-first design
- 🔐 Headers de segurança configurados
- ♿ Acessibilidade (WCAG 2.1)

---

## 🗂️ Estrutura do Projeto

```
moschiat.com/
├── index.html              # Landing page pública
├── dashboard.html          # Dashboard protegido
├── 404.html               # Página de erro personalizada
├── .nojekyll              # Desabilita Jekyll no GitHub Pages
├── CNAME                  # Configuração de domínio customizado
├── README.md              # Este arquivo
├── LICENSE                # Licença do projeto
├── assets/
│   ├── css/
│   │   └── style.css     # Estilos centralizados
│   ├── js/
│   │   ├── auth.js       # Sistema de autenticação
│   │   └── main.js       # Scripts principais
│   └── images/
│       ├── icons/        # Ícones personalizados
│       └── profile/      # Imagens de perfil
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions para deploy
```

---

## 🚀 Tecnologias

### Frontend
- HTML5 Semântico
- CSS3 (Flexbox, Grid, Animations)
- JavaScript ES6+
- Font Awesome 6.5.1

### Hospedagem
- GitHub Pages
- SSL/TLS automático
- CDN global

### Segurança
- Content Security Policy (CSP)
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- HTTPS forçado
- Hash SHA-256 para senhas

---

## 🔐 Segurança

### Autenticação

O dashboard possui sistema de autenticação com:

- ✅ Hash SHA-256 para senhas
- ✅ Rate limiting (5 tentativas)
- ✅ Bloqueio temporário (5 minutos)
- ✅ Sessão com expiração (1 hora)
- ✅ Proteção contra força bruta

### Credenciais de Teste

**⚠️ ATENÇÃO: Para uso em produção, implemente backend real!**

```
Usuário: moschiat
Senha: password
```

### Headers de Segurança

```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Content-Security-Policy: default-src 'self'
```

---

## 📦 Instalação e Deploy

### Desenvolvimento Local

1. Clone o repositório:
```bash
git clone https://github.com/MOSCHIAT/moschiat.com.git
cd moschiat.com
```

2. Abra com um servidor local:
```bash
# Usando Python
python -m http.server 8000

# Usando Node.js
npx http-server

# Usando VS Code
# Instale a extensão "Live Server" e clique em "Go Live"
```

3. Acesse: `http://localhost:8000`

### Deploy no GitHub Pages

O deploy é automático via GitHub Actions:

1. Faça push para a branch `main`:
```bash
git add .
git commit -m "Update site"
git push origin main
```

2. GitHub Actions executa automaticamente
3. Site disponível em: `https://moschiat.com`

### Configuração do Domínio

1. No seu provedor DNS, configure:
```
CNAME: www -> moschiat.github.io
A: @ -> 185.199.108.153
A: @ -> 185.199.109.153
A: @ -> 185.199.110.153
A: @ -> 185.199.111.153
```

2. No repositório GitHub:
- Settings → Pages
- Custom domain: `moschiat.com`
- ✅ Enforce HTTPS

---

## 🎨 Personalização

### Cores

Edite as variáveis CSS em `index.html` e `dashboard.html`:

```css
:root {
    --primary: #00ffae;        /* Verde neon */
    --primary-dark: #00b377;   /* Verde escuro */
    --background: #0a0a0a;     /* Preto */
    --card-bg: rgba(26, 26, 26, 0.95);
    --text-primary: #ffffff;
    --text-secondary: #b0b0b0;
}
```

### Conteúdo

- **Projetos**: Edite a seção `projects-grid` no `dashboard.html`
- **Sobre**: Modifique a seção `hero` no `index.html`
- **Contato**: Atualize os links sociais no footer

---

## 🔧 Manutenção

### Atualizar Dependências

```bash
# Verificar novas versões do Font Awesome
# https://cdnjs.cloudflare.com/ajax/libs/font-awesome/

# Atualizar hash de integridade
# https://www.srihash.org/
```

### Backup

```bash
# Fazer backup do repositório
git clone --mirror https://github.com/MOSCHIAT/moschiat.com.git backup/

# Restaurar backup
cd backup/moschiat.com.git
git push --mirror https://github.com/MOSCHIAT/moschiat.com.git
```

---

## 📊 Performance

### Lighthouse Scores

- 🟢 Performance: 95+
- 🟢 Accessibility: 100
- 🟢 Best Practices: 100
- 🟢 SEO: 100

### Otimizações

- ✅ Imagens otimizadas
- ✅ CSS/JS minificados
- ✅ Lazy loading
- ✅ CDN para bibliotecas
- ✅ Cache headers configurados

---

## 🐛 Solução de Problemas

### Site não carrega HTTPS

```bash
# Verificar configuração DNS
dig moschiat.com

# Aguardar propagação DNS (até 48h)
# Limpar cache do navegador
```

### Dashboard não autentica

```bash
# Verificar console do navegador (F12)
# Limpar sessionStorage
sessionStorage.clear()

# Verificar se JavaScript está habilitado
```

### Deploy falha no GitHub Actions

```bash
# Verificar logs: 
# GitHub repo → Actions → Deploy workflow

# Verificar permissões:
# Settings → Actions → General → Workflow permissions
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para mudanças importantes:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add: Nova feature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📝 Roadmap

### Em Desenvolvimento

- [ ] Blog integrado
- [ ] CMS headless (Strapi/Contentful)
- [ ] Backend para autenticação real
- [ ] Sistema de comentários
- [ ] Newsletter

### Planejado

- [ ] Versão multilíngue (EN, IT)
- [ ] Dark/Light mode toggle
- [ ] Galeria de projetos 3D
- [ ] API pública
- [ ] Documentação interativa

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Paulo Marques (MOSCHIAT)**

- 🌐 Website: [moschiat.com](https://moschiat.com)
- 💼 GitHub: [@MOSCHIAT](https://github.com/MOSCHIAT)
- 📧 Email: contato@moschiat.com

---

## 🙏 Agradecimentos

- [Font Awesome](https://fontawesome.com/) - Ícones
- [GitHub Pages](https://pages.github.com/) - Hospedagem
- [Cloudflare](https://www.cloudflare.com/) - CDN

---

## 📚 Recursos Úteis

### Documentação
- [GitHub Pages Docs](https://docs.github.com/pt/pages)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Web.dev](https://web.dev/)

### Ferramentas
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [SSL Labs](https://www.ssllabs.com/ssltest/)

---

<div align="center">

**[⬆ Voltar ao topo](#-moschiat-portfolio)**

Feito com ❤️ por [MOSCHIAT](https://moschiat.com)

</div>
