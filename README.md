O projeto “blblablabla” é um jogo web simples desenvolvido em Flask (Python), onde o usuário deve escolher entre duas imagens — uma real e outra gerada por inteligência artificial (IA).

O objetivo é testar a percepção visual do jogador e mostrar, ao final, se ele conseguiu identificar corretamente as imagens criadas por IA.

O site é executado dentro de um container Docker, acessível via navegador na porta 8080, e contém uma estrutura leve com páginas HTML e imagens locais.


Topologia da INFRA

site-facul/
│
├── docker-compose.yml        → define o container Flask
│
└── web/
    ├── Dockerfile             → cria a imagem do app
    ├── app.py                 → backend Flask (controla as rotas)
    │
    ├── templates/             → páginas HTML do site
    │   ├── index.html         → tela inicial com as imagens
    │   └── game.html          → lógica do jogo "Qual delas é IA?"
    │
    └── static/
        └── img/               → imagens usadas nas páginas
            ├── real1.jpg
            └── ai1.jpg
