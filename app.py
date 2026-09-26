def carregar_base():
    with open("base_conhecimento.txt", "r", encoding="utf-8") as arquivo:
        return arquivo.read()


def responder(pergunta, base):
    pergunta = pergunta.lower()

    palavras = {
        "python": "Python é uma linguagem de programação de alto nível conhecida por sua sintaxe simples e legível.",
        "variável": "Uma variável é utilizada para armazenar um valor que pode ser utilizado durante a execução de um programa.",
        "lista": "Uma lista permite armazenar vários valores em uma única variável.",
        "função": "Uma função é um bloco de código criado para executar uma determinada tarefa.",
        "git": "Git é um sistema de controle de versão utilizado para acompanhar alterações em projetos.",
        "github": "GitHub é uma plataforma utilizada para hospedar repositórios Git e colaborar em projetos.",
        "commit": "Um commit registra alterações realizadas em um projeto utilizando Git.",
        "banco de dados": "Um banco de dados permite armazenar, organizar e consultar informações.",
        "sql": "SQL é uma linguagem utilizada para realizar operações em bancos de dados relacionais.",
        "inteligência artificial": "Inteligência Artificial é uma área da tecnologia que busca desenvolver sistemas capazes de realizar tarefas associadas à inteligência humana.",
        "prompt": "Um prompt é uma instrução fornecida a um modelo de inteligência artificial para orientar sua resposta."
    }

    for palavra, resposta in palavras.items():
        if palavra in pergunta:
            return resposta

    return "Não encontrei informações suficientes na minha base de conhecimento para responder com segurança."


base = carregar_base()

print("===================================")
print("       TECHGUIDE IA")
print(" Assistente de Estudos em Tecnologia")
print("===================================")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("TechGuide IA: Até mais! Bons estudos!")
        break

    print("TechGuide IA:", responder(pergunta, base))
