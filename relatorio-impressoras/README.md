
O **Gerador de Relatório de Impressoras** é um script Python desenvolvido para automatizar a coleta e geração de relatórios de status e suprimentos de impressoras das marcas OKI e HP. Este sistema foi projetado para empresas e organizações que possuem diversas impressoras em rede e precisam monitorar regularmente os níveis de suprimentos e o desempenho dos equipamentos, facilitando o gerenciamento e manutenção preventiva.

### Funcionamento do Sistema

1.  **Acesso ao PrintSuperVision (OKI)**  
    Para impressoras OKI, o script acessa o **PrintSuperVision**, um aplicativo de monitoramento específico para esta marca, que deve estar previamente instalado no computador. O script abre o PrintSuperVision no navegador, realiza o login de forma automática e acessa a interface de gerenciamento de impressoras.
    
2.  **Acesso ao Site de Impressoras HP**  
    Para impressoras HP, o script se conecta individualmente ao site de cada impressora em rede, acessando as informações de status e suprimentos. Esse processo envolve o login na interface web de cada impressora, se necessário, e a coleta de dados relevantes, como níveis de toner, contadores de páginas e alertas de manutenção.
    
3.  **Atualização do Status de Suprimentos**  
    O script realiza uma atualização dos suprimentos para todas as impressoras registradas, garantindo que os dados sejam os mais recentes antes da geração do relatório. Essa atualização é essencial para que as informações sobre toner, papel e outros consumíveis estejam corretas e prontas para análise.
    
4.  **Geração do Relatório**  
    Após a coleta e atualização dos dados, o script gera um relatório detalhado com informações de todas as impressoras OKI e HP monitoradas. O relatório inclui dados como modelo da impressora, níveis de suprimento, contadores de páginas e quaisquer alertas de manutenção. Esses dados são organizados de maneira clara para facilitar a leitura e análise.
    
5.  **Criação de PDF e Armazenamento em Rede**  
    O relatório é convertido em um arquivo PDF para garantir compatibilidade e facilidade de compartilhamento. O script salva automaticamente o PDF em uma pasta de rede designada, permitindo que os responsáveis tenham acesso rápido e centralizado às informações de manutenção e suprimentos. O armazenamento em rede é ideal para que equipes de TI ou de administração possam acessar o relatório facilmente, mesmo remotamente.
    

### Requisitos e Tecnologias Utilizadas

-   **PrintSuperVision**: Aplicativo necessário para monitoramento de impressoras OKI.
-   **Python**: Linguagem principal para automação e manipulação de dados.
-   **Bibliotecas de Automação Web**: Selenium, para login e navegação automática nos sites das impressoras.
-   **Biblioteca de PDF**: ReportLab, para geração de arquivos PDF.

### Benefícios do Sistema

O Gerador de Relatório de Impressoras automatiza uma tarefa que seria manual e demorada, assegurando uma atualização constante e precisa dos dados de suprimentos e status das impressoras. A centralização dos relatórios em PDF na rede torna o gerenciamento mais eficiente e fornece uma visão completa do desempenho e necessidade de manutenção dos equipamentos, facilitando a gestão de TI e a reposição de suprimentos.
