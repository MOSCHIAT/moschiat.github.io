# 📚 Personal Quote Generator

> Gerador de Citações Pessoal - Uma aplicação terminal para explorar, pesquisar e gerenciar suas citações favoritas.

## ✨ Descrição

O **Personal Quote Generator** é uma aplicação em Python que oferece uma experiência interativa para navegar por uma base de dados curada de 100+ citações distribuídas em 10 categorias temáticas. Com suporte completo a pesquisa, favoritos persistentes e uma interface amigável no terminal, é a ferramenta perfeita para encontrar inspiração diária.

## 🎯 Recursos

- ✅ **Citações Aleatórias** - Receba uma citação aleatória para inspiração instantânea
- 🔍 **Busca por Categoria** - Explore citações organizadas em 10 categorias distintas
- 🔎 **Pesquisa por Palavra-Chave** - Encontre citações que contenham um termo específico
- ⭐ **Sistema de Favoritos** - Marque suas citações preferidas e acesse-as facilmente
- 💾 **Persistência de Dados** - Seus favoritos são salvos automaticamente em JSON
- 🎨 **Interface Amigável** - Menu intuitivo com emojis e formatação visual
- 🛡️ **Tratamento de Erros** - Aplicação robusta que nunca quebra
- 📖 **Type Hints e Documentação** - Código bem documentado e fácil de manter

## 📦 Como Instalar

### Pré-requisitos
- Python 3.8 ou superior
- Terminal/Console

### Passos de Instalação

1. **Clone ou baixe o projeto:**
   ```bash
   git clone https://github.com/MOSCHIAT/moschiat.github.io.git
   cd moschiat.github.io/quote_generator
   ```

2. **Instale as dependências (opcional):**
   ```bash
   pip install -r requirements.txt
   ```
   > Nota: O arquivo `requirements.txt` está vazio pois o projeto usa apenas Python padrão.

## 🚀 Como Executar

**Execute o aplicativo:**
```bash
python app.py
```

Ou no Windows:
```cmd
python app.py
```

## 💡 Exemplos de Uso

### Exemplo 1: Obter uma Citação Aleatória
```
Escolha uma opção (1-6): 1

--------------------------------------------------
📌 Criatividade

"Criatividade sem execução é apenas imaginação."

— MOSCHIAT (ID: 1)
--------------------------------------------------

Deseja favoritar? (s/n): s
✅ Citação adicionada aos favoritos!
```

### Exemplo 2: Buscar por Categoria
```
Escolha uma opção (1-6): 2

📂 Categorias disponíveis:
 1 - Aprendizado
 2 - Criatividade
 3 - Disciplina
 4 - Empreendedorismo
 5 - IA
 6 - Liberdade
 7 - Produtividade
 8 - Programação
 9 - Python
10 - Vida

Escolha uma categoria (número ou nome): 3

📚 Total de citações: 10

[ID:  64] Disciplina           | Disciplina é fazer o difícil quando é fácil...
[ID:  61] Disciplina           | Somos o que repetidamente fazemos. Excelência...
...
```

### Exemplo 3: Pesquisar por Palavra-Chave
```
Escolha uma opção (1-6): 3

🔍 Digite a palavra para pesquisar: tempo

📚 Total de citações: 3

[ID:  30] Python               | Agora é melhor que nunca. (ID: 30)
[ID:  90] Produtividade        | Não deixe para amanhã o que você pode fazer hoje.
[ID:  71] Vida                 | A vida é o que acontece enquanto você está ocupado...
```

### Exemplo 4: Gerenciar Favoritos
```
Escolha uma opção (1-6): 4

⭐ SEUS FAVORITOS

📚 Total de citações: 3

[ID:   1] Criatividade        | Criatividade sem execução é apenas imaginação.
[ID:  15] Programação         | Código sem testes é código legado por definição.
[ID:  21] Python              | Beautiful is better than ugly.

Opções: (v)er citação, (r)emover, (v)oltar: r
Digite o ID da citação para remover: 15
✅ Citação removida dos favoritos!
```

## 📁 Estrutura do Projeto

```
quote_generator/
├── app.py                 # Interface terminal principal
├── quotes.py              # Base de dados de 100+ citações
├── utils.py               # Funções utilitárias
├── requirements.txt       # Dependências (vazio - só stdlib)
├── README.md              # Este arquivo
└── favorites.json         # Arquivo de favoritos (criado automaticamente)
```

### Descrição dos Arquivos

**app.py** (≈400 linhas)
- Menu interativo com 6 opções
- Gerenciamento de fluxo de usuário
- Tratamento completo de exceções
- Interface visual com emojis e formatação

**quotes.py** (≈150 linhas)
- Base de dados com 100 citações em lista de dicionários
- 10 categorias temáticas distribuídas igualmente
- Autores reais e fictícios
- Estrutura padronizada com id, author, category, quote

**utils.py** (≈150 linhas)
- `get_random_quote()` - Retorna citação aleatória
- `get_quote_by_category(category)` - Filtra por categoria
- `search_quote(keyword)` - Busca por palavra-chave
- `get_all_categories()` - Lista todas as categorias
- `favorite_quote(id)` - Adiciona aos favoritos
- `remove_favorite(id)` - Remove dos favoritos
- `list_favorites()` - Retorna citações favoritas
- `save_favorites()` - Persiste favoritos em JSON
- `load_favorites()` - Carrega favoritos do arquivo

**favorites.json** (criado automaticamente)
- Arquivo JSON que armazena IDs de citações favoritas
- Formato simples e legível
- Criado automaticamente na primeira vez

## 🏆 Categorias de Citações

1. **Criatividade** - Inspiração artística e inovação
2. **Programação** - Conceitos e filosofia de código
3. **Python** - Citações específicas sobre a linguagem Python
4. **IA** - Futuro, machine learning e tecnologia
5. **Aprendizado** - Educação e desenvolvimento pessoal
6. **Empreendedorismo** - Negócios e liderança
7. **Disciplina** - Hábitos e força de vontade
8. **Vida** - Filosofia e reflexão existencial
9. **Produtividade** - Eficiência e organização
10. **Liberdade** - Autonomia e libertação

## 🏗️ Padrões de Código

Este projeto segue rigorosamente os melhores práticas Python:

- ✅ **Type Hints** - Todas as funções possuem type hints completos
- ✅ **Docstrings** - Documentação em docstring para cada função
- ✅ **PEP 8** - Código formatado de acordo com PEP 8
- ✅ **Funções Pequenas** - Cada função tem responsabilidade única
- ✅ **Nomes Descritivos** - Variáveis e funções com nomes claros
- ✅ **Tratamento de Erros** - Try/except estratégico sem quebras
- ✅ **Reutilização** - Código modular e reutilizável
- ✅ **Comentários** - Apenas comentários úteis e necessários

## 📝 Exemplo de Código

```python
def get_quote_by_category(category: str) -> list[dict]:
    """Get all quotes from a specific category.
    
    Args:
        category: The category name to filter quotes.
    
    Returns:
        list[dict]: All quotes matching the given category.
                   Returns empty list if category not found.
    """
    return [quote for quote in QUOTES if quote["category"].lower() == category.lower()]
```

## 🐛 Tratamento de Erros

A aplicação implementa tratamento robusto de erros:

- Validação de entrada do usuário
- Tratamento de `KeyboardInterrupt` para Ctrl+C
- Exceções genéricas para operações de arquivo
- Mensagens de erro amigáveis em português
- A aplicação nunca quebra durante execução

## 📊 Dados de Exemplo

Cada citação segue a estrutura:

```json
{
  "id": 1,
  "author": "MOSCHIAT",
  "category": "Criatividade",
  "quote": "Criatividade sem execução é apenas imaginação."
}
```

## 🤝 Contribuições

Se você deseja adicionar mais citações ou melhorar o projeto:

1. Adicione as citações em `quotes.py`
2. Mantenha o formato padrão
3. Distribua entre as categorias existentes
4. Faça commit com mensagem descritiva

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.

```
MIT License

Permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e dos arquivos de documentação associados (o "Software"), para lidar
no Software sem restrição, incluindo sem limitação os direitos de usar, copiar,
modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software.

Ver LICENSE para detalhes completos.
```

## 🌟 Recursos Futuros

Potenciais melhorias:

- [ ] Interface gráfica com tkinter
- [ ] API REST para acessar citações
- [ ] Exportar favoritos para PDF
- [ ] Suporte a múltiplos idiomas
- [ ] Integração com redes sociais
- [ ] Citações por data
- [ ] Sistema de avaliação de citações

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique os exemplos acima
2. Revise a estrutura do projeto
3. Consulte as docstrings do código
4. Abra uma issue no repositório

---

**Desenvolvido com ❤️ e Python**

*Criatividade sem execução é apenas imaginação. Execute seu código!*
