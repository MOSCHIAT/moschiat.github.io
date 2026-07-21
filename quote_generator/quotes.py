"""Database of quotes stored as dictionaries.

This module contains a collection of quotes in Portuguese,
categorized across 10 different themes.
"""

QUOTES: list[dict] = [
    # Criatividade
    {"id": 1, "author": "MOSCHIAT", "category": "Criatividade", "quote": "Criatividade sem execução é apenas imaginação."},
    {"id": 2, "author": "Pablo Picasso", "category": "Criatividade", "quote": "Toda criança é um artista. O problema é permanecer um artista depois de crescer."},
    {"id": 3, "author": "Steve Jobs", "category": "Criatividade", "quote": "Criatividade é conectar coisas."},
    {"id": 4, "author": "Maya Angelou", "category": "Criatividade", "quote": "As ideias mais criativas vêm de quem ousa questionar tudo."},
    {"id": 5, "author": "Vincent van Gogh", "category": "Criatividade", "quote": "Eu sonho meu quadro e então pinto meu sonho."},
    {"id": 6, "author": "Walt Disney", "category": "Criatividade", "quote": "É divertido fazer o impossível."},
    {"id": 7, "author": "Frida Kahlo", "category": "Criatividade", "quote": "Pinto a minha própria realidade."},
    {"id": 8, "author": "David Bowie", "category": "Criatividade", "quote": "A musa não tem medo de trabalhar."},
    {"id": 9, "author": "Banksy", "category": "Criatividade", "quote": "Arte deve confortar o perturbado e perturbar o confortável."},
    {"id": 10, "author": "Dali", "category": "Criatividade", "quote": "Eu sou meu próprio muse. Eu sou o assunto que conheço melhor."},
    
    # Programação
    {"id": 11, "author": "Donald Knuth", "category": "Programação", "quote": "Otimização prematura é a raiz de todo mal."},
    {"id": 12, "author": "Linus Torvalds", "category": "Programação", "quote": "Eu gosto de ofender as pessoas quando elas estão erradas."},
    {"id": 13, "author": "Bill Gates", "category": "Programação", "quote": "A Internet será como a televisão, não será."},
    {"id": 14, "author": "Steve Ballmer", "category": "Programação", "quote": "Software é um grande jogo de xadrez tridimensional."},
    {"id": 15, "author": "Robert C. Martin", "category": "Programação", "quote": "Código sem testes é código legado por definição."},
    {"id": 16, "author": "Alan Turing", "category": "Programação", "quote": "Máquinas podem imitar o comportamento humano?"},
    {"id": 17, "author": "John Carmack", "category": "Programação", "quote": "A otimização é a raiz de toda diversão."},
    {"id": 18, "author": "Grace Hopper", "category": "Programação", "quote": "É mais fácil pedir desculpas do que permissão."},
    {"id": 19, "author": "Jeff Atwood", "category": "Programação", "quote": "Nunca duplique código. Nunca."},
    {"id": 20, "author": "Erich Gamma", "category": "Programação", "quote": "Padrões facilitam a comunicação entre desenvolvedores."},
    
    # Python
    {"id": 21, "author": "Guido van Rossum", "category": "Python", "quote": "Beautiful is better than ugly."},
    {"id": 22, "author": "Guido van Rossum", "category": "Python", "quote": "Explícito é melhor que implícito."},
    {"id": 23, "author": "Raymond Hettinger", "category": "Python", "quote": "Python é um passeio no parque comparado a C++."},
    {"id": 24, "author": "Pythonista", "category": "Python", "quote": "Em Python, há geralmente uma maneira óbvia de fazer isso."},
    {"id": 25, "author": "David Beazley", "category": "Python", "quote": "Python é uma linguagem para adultos."},
    {"id": 26, "author": "Tim Peters", "category": "Python", "quote": "Simples é melhor que complexo."},
    {"id": 27, "author": "Guido van Rossum", "category": "Python", "quote": "A legibilidade é importante."},
    {"id": 28, "author": "Real Python", "category": "Python", "quote": "Python não é uma bala de prata, é um canivete suíço."},
    {"id": 29, "author": "Programmer", "category": "Python", "quote": "Se você conhece Python, conhece o futuro."},
    {"id": 30, "author": "Barry Warsaw", "category": "Python", "quote": "Agora é melhor que nunca."},
    
    # IA
    {"id": 31, "author": "Alan Turing", "category": "IA", "quote": "Máquinas inteligentes irão inevitavelmente desempenhar tarefas humanas."},
    {"id": 32, "author": "Andrew Ng", "category": "IA", "quote": "IA é a nova eletricidade."},
    {"id": 33, "author": "Demis Hassabis", "category": "IA", "quote": "IA pode ser tão poderosa quanto aprender a ver."},
    {"id": 34, "author": "Sam Altman", "category": "IA", "quote": "O futuro vai ser muito bom se nós nos importarmos com ele."},
    {"id": 35, "author": "Yann LeCun", "category": "IA", "quote": "Deep Learning é apenas uma camada de bolo da IA."},
    {"id": 36, "author": "Fei-Fei Li", "category": "IA", "quote": "IA humanista é o futuro."},
    {"id": 37, "author": "Sundar Pichai", "category": "IA", "quote": "IA é a transformação mais profunda de nossa era."},
    {"id": 38, "author": "Elon Musk", "category": "IA", "quote": "IA é o maior risco que enfrentamos como civilização."},
    {"id": 39, "author": "Stuart Russell", "category": "IA", "quote": "O objetivo real é criar IA que seja benéfica."},
    {"id": 40, "author": "Yoshua Bengio", "category": "IA", "quote": "Deep Learning mudou tudo na IA."},
    
    # Aprendizado
    {"id": 41, "author": "Albert Einstein", "category": "Aprendizado", "quote": "Não pare nunca de questionar. A curiosidade existe por uma razão."},
    {"id": 42, "author": "Confúcio", "category": "Aprendizado", "quote": "Quando você sabe uma coisa, é melhor que não sabe."},
    {"id": 43, "author": "Malala Yousafzai", "category": "Aprendizado", "quote": "Nós não pedimos muito. Nós apenas pedimos pelo direito de aprender."},
    {"id": 44, "author": "Nelson Mandela", "category": "Aprendizado", "quote": "A educação é a mais poderosa arma para mudar o mundo."},
    {"id": 45, "author": "Benjamin Franklin", "category": "Aprendizado", "quote": "Diga-me e eu esquecerei, ensine-me e eu poderei lembrar."},
    {"id": 46, "author": "Carol S. Dweck", "category": "Aprendizado", "quote": "Mentalidade de crescimento leva ao sucesso."},
    {"id": 47, "author": "Paulo Freire", "category": "Aprendizado", "quote": "Ninguém educa ninguém, ninguém se educa a si mesmo, os homens se educam entre si."},
    {"id": 48, "author": "Malcolm X", "category": "Aprendizado", "quote": "O programa educacional deve ser estudado como um processo."},
    {"id": 49, "author": "Confúcio", "category": "Aprendizado", "quote": "O aprendizado sem pensamento é trabalho perdido."},
    {"id": 50, "author": "Stephen Covey", "category": "Aprendizado", "quote": "O aprendizado é a mudança contínua em comportamento."},
    
    # Empreendedorismo
    {"id": 51, "author": "Steve Jobs", "category": "Empreendedorismo", "quote": "O empreendedorismo é sobre fé."},
    {"id": 52, "author": "Richard Branson", "category": "Empreendedorismo", "quote": "Negócios são apenas um jogo que oferece satisfação pessoal."},
    {"id": 53, "author": "Elon Musk", "category": "Empreendedorismo", "quote": "Está sempre faltando mais que sobra."},
    {"id": 54, "author": "Jack Ma", "category": "Empreendedorismo", "quote": "Se você não fizer hoje, você nunca fará amanhã."},
    {"id": 55, "author": "Sara Blakely", "category": "Empreendedorismo", "quote": "O fracasso não deve ser visto como uma vergonha."},
    {"id": 56, "author": "Mark Zuckerberg", "category": "Empreendedorismo", "quote": "Ideias não são mágicas. Você tem que trabalhar para torná-las realidade."},
    {"id": 57, "author": "Oprah Winfrey", "category": "Empreendedorismo", "quote": "Sucesso é estar pronto para oportunidades."},
    {"id": 58, "author": "Jeff Bezos", "category": "Empreendedorismo", "quote": "Eu pedi a todos que fossem donos da companhia como se fosse sua."},
    {"id": 59, "author": "Sheryl Sandberg", "category": "Empreendedorismo", "quote": "Você não pode ser o que não pode ver."},
    {"id": 60, "author": "Tim Cook", "category": "Empreendedorismo", "quote": "O povo quer te dizer o que fazer, mas você sabe melhor."},
    
    # Disciplina
    {"id": 61, "author": "Aristóteles", "category": "Disciplina", "quote": "Somos o que repetidamente fazemos. Excelência, portanto, não é um ato mas um hábito."},
    {"id": 62, "author": "Bruce Lee", "category": "Disciplina", "quote": "A disciplina é fazer o que você odeia fazer, mas mesmo assim fazendo."},
    {"id": 63, "author": "James Clear", "category": "Disciplina", "quote": "Você não sobe para o seu melhor. Você cai para o seu sistema."},
    {"id": 64, "author": "David Goggins", "category": "Disciplina", "quote": "Disciplina é fazer o difícil quando é fácil decidir."},
    {"id": 65, "author": "Jocko Willink", "category": "Disciplina", "quote": "Disciplina é liberdade."},
    {"id": 66, "author": "Marcus Aurelius", "category": "Disciplina", "quote": "Você tem poder sobre sua mente, não fora dela."},
    {"id": 67, "author": "Naval Ravikant", "category": "Disciplina", "quote": "A disciplina é escolher entre o que você quer agora e o que você quer mais."},
    {"id": 68, "author": "Epicteto", "category": "Disciplina", "quote": "Ninguém pode ferir você sem sua permissão."},
    {"id": 69, "author": "Jim Ryun", "category": "Disciplina", "quote": "Motivação é o que te começa. Hábito é o que te mantém."},
    {"id": 70, "author": "Tony Robbins", "category": "Disciplina", "quote": "A disciplina é escolher o que você quer mais ao invés do que você quer agora."},
    
    # Vida
    {"id": 71, "author": "Oscar Wilde", "category": "Vida", "quote": "A vida é o que acontece enquanto você está ocupado fazendo outros planos."},
    {"id": 72, "author": "Maya Angelou", "category": "Vida", "quote": "Não há nada que você possa fazer de forma maior que dar de si mesmo."},
    {"id": 73, "author": "Steve Jobs", "category": "Vida", "quote": "A vida é breve e você precisa aproveitá-la."},
    {"id": 74, "author": "Paulo Coelho", "category": "Vida", "quote": "É a possibilidade de realizar um sonho que torna a vida interessante."},
    {"id": 75, "author": "Deepak Chopra", "category": "Vida", "quote": "O significado da vida é aquele que você lhe atribui."},
    {"id": 76, "author": "Socrates", "category": "Vida", "quote": "A vida que não é examinada não vale ser vivida."},
    {"id": 77, "author": "Rumi", "category": "Vida", "quote": "Você não é uma gota na água. Você é um oceano em uma gota."},
    {"id": 78, "author": "Eleanor Roosevelt", "category": "Vida", "quote": "Faça tudo que teme e o medo seguramente morrerá."},
    {"id": 79, "author": "Buddha", "category": "Vida", "quote": "A vida é sofrimento causado pela ganância."},
    {"id": 80, "author": "Marilyn Monroe", "category": "Vida", "quote": "Viva como se fosse morrer amanhã. Aprenda como se fosse viver para sempre."},
    
    # Produtividade
    {"id": 81, "author": "David Allen", "category": "Produtividade", "quote": "A produtividade vem de sistemas, não da motivação."},
    {"id": 82, "author": "Cal Newport", "category": "Produtividade", "quote": "O trabalho profundo é cada vez mais valioso e cada vez mais raro."},
    {"id": 83, "author": "Tim Ferriss", "category": "Produtividade", "quote": "Ocupado não é produtivo."},
    {"id": 84, "author": "Brian Tracy", "category": "Produtividade", "quote": "Coma aquele sapo primeiro coisa pela manhã."},
    {"id": 85, "author": "Stephen R. Covey", "category": "Produtividade", "quote": "O que importa não é o tempo que você tem, mas o que você faz com ele."},
    {"id": 86, "author": "Parkinson", "category": "Produtividade", "quote": "Trabalho expande para preencher o tempo disponível."},
    {"id": 87, "author": "BJ Fogg", "category": "Produtividade", "quote": "Pequenos hábitos levam a grandes mudanças."},
    {"id": 88, "author": "Peter Drucker", "category": "Produtividade", "quote": "O que é medido é gerenciado."},
    {"id": 89, "author": "Lao Tzu", "category": "Produtividade", "quote": "Aquele que nunca se afasta de seu ofício será perfeito nele."},
    {"id": 90, "author": "Thomas Jefferson", "category": "Produtividade", "quote": "Não deixe para amanhã o que você pode fazer hoje."},
    
    # Liberdade
    {"id": 91, "author": "Nelson Mandela", "category": "Liberdade", "quote": "A liberdade é apenas uma chance de ser melhor."},
    {"id": 92, "author": "Martin Luther King Jr.", "category": "Liberdade", "quote": "Liberdade nunca é oferecida voluntariamente pelo opressor."},
    {"id": 93, "author": "Maya Angelou", "category": "Liberdade", "quote": "Ninguém pode te ferir sem sua permissão."},
    {"id": 94, "author": "Simone de Beauvoir", "category": "Liberdade", "quote": "Ser livre não é apenas sair da prisão."},
    {"id": 95, "author": "Paulo Freire", "category": "Liberdade", "quote": "Ninguém é livre enquanto houver escravos."},
    {"id": 96, "author": "Jean-Paul Sartre", "category": "Liberdade", "quote": "O homem é condenado a ser livre."},
    {"id": 97, "author": "Voltaire", "category": "Liberdade", "quote": "Posso discordar do que você diz, mas defenderei seu direito de dizê-lo."},
    {"id": 98, "author": "Benjamin Franklin", "category": "Liberdade", "quote": "Aqueles que abrem mão de liberdade essencial para segurança temporária não merecem nenhuma."},
    {"id": 99, "author": "Rosa Parks", "category": "Liberdade", "quote": "Eu havia sido pisada meu tempo todo. Eu não seria pisada mais."},
    {"id": 100, "author": "Che Guevara", "category": "Liberdade", "quote": "A verdadeira revolução é interior. Liberte-se primeiro."},
]
