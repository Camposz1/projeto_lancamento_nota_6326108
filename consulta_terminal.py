import pandas as pd

def calcular_media(row):
    try:
        nota1 = float(row['Nota 1'])
        nota2 = float(row['Nota 2'])
        tf01 = float(row['TF01'])
        tf02 = float(row['TF02'])

        media_provas = ((nota1 + nota2) / 2.0) * 0.8  # Vale até 8.0
        media_tf = (tf01 + tf02) / 2.0                # Vale até 2.0
        return media_provas + media_tf
    except Exception:
        return 0.0

def exibir_estatisticas(df):
    df['Media_Final'] = df.apply(calcular_media, axis=1)
    
    total_alunos = len(df)
    media_geral = df['Media_Final'].mean()
    aprovados = len(df[df['Media_Final'] >= 6.0])
    reprovados = total_alunos - aprovados
    taxa_aprovacao = (aprovados / total_alunos) * 100 if total_alunos > 0 else 0

    print("\n" + "="*45)
    print("         📊 ESTATÍSTICAS DA TURMA         ")
    print("="*45)
    print(f"Total de Alunos Processados : {total_alunos}")
    print(f"Média Geral da Turma       : {media_geral:.2f} / 10.0")
    print(f"Aprovados                  : {aprovados} ({taxa_aprovacao:.1f}%)")
    print(f"Reprovados                 : {reprovados}")
    print(f"Maior Nota                 : {df['Media_Final'].max():.2f}")
    print(f"Menor Nota                 : {df['Media_Final'].min():.2f}")
    print("="*45)

def consultar_aluno():
    try:
        df = pd.read_csv("notas.csv")
    except Exception:
        print("❌ Erro ao carregar a planilha ou arquivo 'notas.csv'.")
        return

    # Garante que os nomes das colunas e valores estejam em formato string simples
    df['RA'] = df['RA'].astype(str)
    df['Nome'] = df['Nome'].astype(str)

    # Exibe estatísticas gerais ao iniciar
    exibir_estatisticas(df)

    # Permite busca por RA ou Nome
    busca = input("\nDigite o RA ou o NOME do aluno para pesquisar: ").strip()

    # Filtra por RA exato ou por Nome contendo o termo digitado (ignorando maiúsculas/minúsculas)
    aluno = df[(df['RA'] == busca) | (df['Nome'].str.contains(busca, case=False, na=False))]

    if aluno.empty:
        print(f"❌ Nenhum aluno encontrado com a busca '{busca}'.")
    else:
        dados = aluno.iloc[0]
        
        nota1 = float(dados['Nota 1'])
        nota2 = float(dados['Nota 2'])
        tf01 = float(dados['TF01'])
        tf02 = float(dados['TF02'])

        media_provas = ((nota1 + nota2) / 2.0) * 0.8
        media_tf = (tf01 + tf02) / 2.0
        nota_final = media_provas + media_tf

        status = "APROVADO" if nota_final >= 6.0 else "REPROVADO"

        print("\n" + "="*45)
        print("          RELATÓRIO DO ALUNO          ")
        print("="*45)
        print(f"RA                         : {dados['RA']}")
        print(f"Nome                       : {dados['Nome']}")
        print(f"Nota 1                     : {nota1:.2f}")
        print(f"Nota 2                     : {nota2:.2f}")
        print(f"TF01                       : {tf01:.2f}")
        print(f"TF02                       : {tf02:.2f}")
        print("-" * 45)
        print(f"Pontuação Provas (peso 8)  : {media_provas:.2f}")
        print(f"Pontuação TF (peso 2)      : {media_tf:.2f}")
        print(f"MÉDIA FINAL                : {nota_final:.2f} / 10.0")
        print(f"SITUAÇÃO                   : {status}")
        print("="*45)

if __name__ == "__main__":
    while True:
        consultar_aluno()
        opcao = input("\nDeseja pesquisar outro aluno? (s/n): ").strip().lower()
        if opcao != 's':
            print("Encerrando consulta.")
            break