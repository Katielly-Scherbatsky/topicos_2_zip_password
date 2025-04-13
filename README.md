```markdown
# 🔐 ZIP Password Cracker

Este é um programa feito em Python que quebra senhas de arquivos `.zip` usando uma **wordlist** (lista de possíveis senhas), com uma interface gráfica amigável usando **Tkinter**.

---

## 📦 Funcionalidades

- Interface gráfica simples
- Testa senhas automaticamente a partir de um arquivo `.txt`
- Funciona no **Windows** e **Linux**
- Atualiza o status em tempo real enquanto tenta as senhas

---

## 🖥️ Requisitos

### Windows

1. Instale o Python:
   - Baixe e instale pelo site oficial: https://www.python.org/downloads/windows/
   - Marque a opção `Add Python to PATH` durante a instalação.

2. Verifique no terminal (cmd ou PowerShell):

```bash
python --version
```

3. Instale a biblioteca opcional (se desejar detectar encoding automaticamente):

```bash
pip install chardet
```

> ⚠️ A biblioteca `chardet` **não é obrigatória**, mas pode ser útil em versões futuras com detecção automática de encoding.

---

### Linux (Ubuntu/Debian)

1. Instale o Python (se ainda não tiver):

```bash
sudo apt update
sudo apt install python3 python3-pip
```

2. Verifique:

```bash
python3 --version
```

3. Instale a biblioteca opcional:

```bash
pip3 install chardet
```

---

## 🚀 Como rodar o programa

1. Clone ou baixe este repositório:

```bash
https://github.com/Katielly-Scherbatsky/topicos_2_zip_password
```

2. Execute o script:

### Windows:

```bash
python zip_cracker.py
```

### Linux:

```bash
python3 zip_cracker.py
```

---

## 🧪 Como testar o programa

### 1. Crie um arquivo ZIP com senha:

#### Linux:

```bash
zip -e teste.zip arquivo.txt
# Digite a senha desejada
```

#### Windows:

- Use o programa **7-Zip**:
  - Clique com o botão direito > 7-Zip > "Adicionar ao arquivo..."
  - Marque a opção de **criptografar** e digite a senha.

### 2. Existem dois arquivos de wordlist simples (arquivo `.txt`):

> Um contém a senha `wordlistcomasenha.txt`
> o outro não `wordlistsemasenha.txt`

### 3. No programa:

- Selecione o arquivo `arquivozipado.zip`
- Selecione a wordlist
- Clique em "Iniciar Ataque"
- O programa testará as senhas até encontrar a correta

---

## 🧑‍💻 Autor

Desenvolvido por Katielly Bordin Santos 💻

---

## 🛑 Aviso Legal

Este programa é **educacional** e deve ser usado **somente em arquivos que você tem permissão legal para acessar**. O uso inadequado é de responsabilidade exclusiva do usuário.
```
