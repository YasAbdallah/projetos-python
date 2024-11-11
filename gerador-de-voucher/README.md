O **Gerador de Senha Wi-Fi** é um script desenvolvido em Python para automatizar a criação e distribuição de vouchers de uma rede Wi-Fi, com o objetivo de aumentar a segurança e facilitar o acesso autorizado. Este sistema foi projetado para organizações ou empresas que desejam alterar suas senhas de Wi-Fi periodicamente, evitando acesso não autorizado e garantindo que apenas usuários aprovados recebam as credenciais de rede.

### Funcionamento do Sistema

1.  **Acesso ao Unifi Controller**  
    O script conecta-se automaticamente ao **Unifi Controller**, um software de gerenciamento de redes que permite configurar e monitorar redes Wi-Fi. A conexão com o Unifi Controller é realizada de forma segura, autenticando o script para acessar as configurações da rede.
    
2.  **Navegação até a Aba de Wi-Fi**  
    Uma vez conectado, o script navega até a seção de configurações de Wi-Fi no Unifi Controller. Esta etapa garante que o script acessa diretamente o local correto para atualizar as configurações de senha.
    
3.  **Geração da Nova Senha**  
    O script gera uma senha aleatória, utilizando uma combinação de letras, números e caracteres especiais, conforme definido nas configurações de segurança. A nova senha é criada com o objetivo de ser complexa o suficiente para oferecer segurança, mas ao mesmo tempo prática para os usuários.
    
4.  **Criação de PDF com QR Code**  
    Após a geração da senha, o script cria um PDF contendo o QR Code correspondente. O QR Code facilita o acesso dos usuários à rede, permitindo que simplesmente escaneiem o código para se conectar, sem precisar digitar a senha manualmente. A biblioteca utilizada para a criação do QR Code converte a senha em uma imagem QR, que é então inserida em um PDF gerado automaticamente.
    
5.  **Envio de E-mail com Senha e PDF**  
    O sistema envia um e-mail para uma lista de usuários autorizados, contendo a nova senha e o PDF com o QR Code. O e-mail é configurado para ser enviado com uma mensagem padrão e os anexos necessários, garantindo que os usuários recebam as informações de acesso de maneira conveniente e segura.
    
6.  **Execução Mensal Automática**  
    Esse processo é repetido automaticamente no primeiro dia de cada mês, de acordo com uma rotina agendada (utilizando bibliotecas como `schedule` ou `cron` para automação). A rotina mensal garante que a senha é atualizada de forma consistente, sem a necessidade de intervenção manual.
    

### Tecnologias e Bibliotecas Utilizadas

-   **Python**: Linguagem principal do script.
-   **Unifi API**: Para acesso e controle das configurações de rede.
-   **wifi_qrcode_generatore e reportlab**: Bibliotecas para criação do QR Code e geração do PDF.
-   **smtplib** ou **email**: Bibliotecas do Python para envio de e-mails.

### Benefícios do Sistema

O Gerador de Senha Wi-Fi automatiza o gerenciamento de credenciais, economizando tempo e aumentando a segurança da rede. A atualização mensal das senhas e o envio direto aos usuários permitem um controle efetivo do acesso, ideal para empresas que buscam otimizar a segurança de sua rede sem processos manuais complexos.
