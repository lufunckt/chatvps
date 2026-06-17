# Guia de Instalação e Acesso - ChatbotX

Este arquivo contém as instruções necessárias para instalar e acessar o ChatbotX na sua VPS.

## 🛠️ Passo 1: Acesso e Preparação do Servidor
Acesse seu servidor via SSH e execute os comandos abaixo para garantir que o Docker esteja funcionando corretamente:

```bash
# Remove configurações antigas que podem causar erro e reinicia o Docker
rm -f /etc/docker/daemon.json && systemctl restart docker

# Verifica se o Docker está ativo (deve mostrar o cabeçalho de uma tabela vazia)
docker ps
```

## 🚀 Passo 2: Instalação Automática
Copie e cole todo este bloco de comandos no seu terminal SSH para instalar o ChatbotX:

```bash
# Cria a pasta de instalação e baixa as configurações
mkdir -p ~/chatbotx-install && cd ~/chatbotx-install
git clone https://github.com/chatbotxio/chatbotx-docker-compose.git .

# Configura as chaves de segurança e o IP da sua VPS
echo "BETTER_AUTH_SECRET=$(openssl rand -base64 32)" > .env
echo "ENCRYPTION_KEY=$(openssl rand -hex 32)" >> .env
echo "PUBLIC_IP=162.141.109.148" >> .env

# Inicia o sistema
docker compose up -d
```

## 🔑 Passo 3: Credenciais de Acesso
Após rodar os comandos acima, aguarde cerca de **2 minutos** para o sistema inicializar o banco de dados.

*   **🌐 URL de Acesso:** [http://162.141.109.148:3123](http://162.141.109.148:3123)
*   **📧 Login (E-mail):** `demo@example.com`
*   **🔒 Senha:** `Demo@1234`

---

### ⚠️ Observações de Segurança e Firewall
1.  **Firewall:** Se o link acima não abrir, você deve liberar a **porta 3123** no painel de controle da sua VPS (Hosteg).
2.  **SSH Host Key:** Se receber um erro de "Remote Host Identification Has Changed" ao tentar entrar no SSH, execute o comando `ssh-keygen -R 162.141.109.148` no seu computador.
