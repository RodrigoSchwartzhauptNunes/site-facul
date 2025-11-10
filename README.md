O projeto “blblablabla” é um jogo web simples desenvolvido em Flask (Python), onde o usuário deve escolher entre duas imagens — uma real e outra gerada por inteligência artificial (IA).

O objetivo é testar a percepção visual do jogador e mostrar, ao final, se ele conseguiu identificar corretamente as imagens criadas por IA.

O site é executado dentro de um container Docker, acessível via navegador na porta 8080, e contém uma estrutura leve com páginas HTML e imagens locais.


Topologia da INFRA

site-facul/
│
├── docker-compose.yml
└── web/
    ├── Dockerfile
    ├── app.py
    │
    ├── templates/
    │   ├── index.html              → Página inicial (HOME)
    │   ├── sobre.html              → Página “Sobre”
    │   ├── politica.html           → Página “Política de Privacidade”
    │   ├── game1.html              → Primeira rodada do jogo
    │   ├── game2.html              → Segunda rodada do jogo
    │   └── final.html              → Tela final com pontuação
    │
    └── static/
        └── img/
            ├── real1.jpg
            ├── ai1.jpg
            └── ...
