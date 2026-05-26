import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


# ==========================================
# 1. MOTOR DE SEGURANÇA (Agora aceita extensões personalizadas)
# ==========================================
def derivar_chave(senha: str, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=2 ** 14, r=8, p=1)
    return kdf.derive(senha.encode())


def aplicar_cadeado(caminho_alvo: str, senha: str, extensao_final: str) -> str:
    with open(caminho_alvo, "rb") as f:
        dados = f.read()

    salt = os.urandom(16)
    nonce = os.urandom(12)
    chave = derivar_chave(senha, salt)
    aesgcm = AESGCM(chave)

    dados_cifrados = aesgcm.encrypt(nonce, dados, None)

    # Agora a gente escolhe a extensão na hora de salvar
    caminho_final = caminho_alvo + extensao_final
    with open(caminho_final, "wb") as f:
        f.write(salt + nonce + dados_cifrados)

    return caminho_final


def remover_cadeado(caminho_protegido: str, senha: str, extensao_alvo: str) -> str:
    with open(caminho_protegido, "rb") as f:
        pacote = f.read()

    salt = pacote[:16]
    nonce = pacote[16:28]
    dados_cifrados = pacote[28:]

    chave = derivar_chave(senha, salt)
    aesgcm = AESGCM(chave)

    dados_originais = aesgcm.decrypt(nonce, dados_cifrados, None)

    # Remove a etiqueta específica
    caminho_recuperado = caminho_protegido.replace(extensao_alvo, "")
    with open(caminho_recuperado, "wb") as f:
        f.write(dados_originais)

    return caminho_recuperado


# ==========================================
# 2. LÓGICA DO PACOTE (Com a inteligência corrigida)
# ==========================================
def forcar_exclusao(funcao, caminho, informacao_erro):
    import os
    import stat
    os.chmod(caminho, stat.S_IWRITE)
    funcao(caminho)


def processar_trancamento(caminho: str, senha: str):
    if os.path.isdir(caminho):
        # 1. Compacta a pasta
        caminho_zip = shutil.make_archive(caminho, 'zip', caminho)

        # 2. Blinda o zip usando a etiqueta de pasta
        resultado = aplicar_cadeado(caminho_zip, senha, ".pasta_protegida")

        # 3. Limpa as evidências
        os.remove(caminho_zip)
        shutil.rmtree(caminho, onerror=forcar_exclusao)
        return resultado
    else:
        # Blinda o arquivo direto usando a etiqueta de arquivo
        resultado = aplicar_cadeado(caminho, senha, ".arquivo_protegido")
        os.remove(caminho)
        return resultado


def processar_destrancamento(caminho: str, senha: str):
    # A mágica da decisão: o próprio nome do arquivo diz o que fazer
    if caminho.endswith(".pasta_protegida"):
        caminho_base = remover_cadeado(caminho, senha, ".pasta_protegida")
        os.remove(caminho)

        # Como sabemos que era uma pasta, temos certeza absoluta de extrair
        pasta_destino = caminho_base.replace('.zip', '')
        shutil.unpack_archive(caminho_base, pasta_destino)
        os.remove(caminho_base)  # Deleta o zip limpo temporário
        return pasta_destino

    elif caminho.endswith(".arquivo_protegido"):
        caminho_base = remover_cadeado(caminho, senha, ".arquivo_protegido")
        os.remove(caminho)
        return caminho_base

    else:
        raise ValueError("O formato do arquivo é desconhecido.")
# ==========================================
# 3. INTERFACE GRÁFICA
# ==========================================
class AppCofre:
    def __init__(self, root):
        self.root = root
        self.root.title("Cofre Mágico - v3.0 (Suporte a Pastas)")
        self.root.geometry("480x420")
        self.root.resizable(False, False)
        self.alvo = None

        style = ttk.Style()
        style.theme_use('clam')

        # --- Seção de Seleção ---
        frame_alvo = ttk.LabelFrame(root, text=" 1. O que deseja proteger? ", padding=15)
        frame_alvo.pack(fill="x", padx=20, pady=10)

        # Agora temos dois botões distintos
        btn_frame = ttk.Frame(frame_alvo)
        btn_frame.pack(fill="x")

        ttk.Button(btn_frame, text="Procurar Arquivo...", command=self.escolher_arquivo).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Procurar Pasta...", command=self.escolher_pasta).pack(side="left", padx=5)

        self.lbl_alvo = ttk.Label(frame_alvo, text="Nenhum item selecionado", foreground="gray")
        self.lbl_alvo.pack(pady=10)

        # --- Seção de Senha ---
        frame_senha = ttk.LabelFrame(root, text=" 2. Código de Acesso ", padding=15)
        frame_senha.pack(fill="x", padx=20, pady=10)

        self.entry_senha = ttk.Entry(frame_senha, show="*", width=30)
        self.entry_senha.pack(side="left", padx=5)

        self.btn_olho = ttk.Button(frame_senha, text="👁️ Mostrar", width=10, command=self.alternar_visao)
        self.btn_olho.pack(side="left", padx=5)

        # --- Seção de Ações ---
        frame_acoes = ttk.Frame(root, padding=10)
        frame_acoes.pack(fill="x", padx=20, pady=10)

        ttk.Button(frame_acoes, text="🔒 Ocultar (Trancar)", command=self.acao_trancar).pack(fill="x", pady=5)
        ttk.Button(frame_acoes, text="🔓 Revelar (Destrancar)", command=self.acao_destrancar).pack(fill="x", pady=5)

    def alternar_visao(self):
        if self.entry_senha.cget('show') == '*':
            self.entry_senha.config(show='')
            self.btn_olho.config(text="🙈 Ocultar")
        else:
            self.entry_senha.config(show='*')
            self.btn_olho.config(text="👁️ Mostrar")

    def atualizar_label(self, caminho):
        if caminho:
            self.alvo = caminho
            nome_curto = os.path.basename(caminho)
            if os.path.isdir(caminho):
                self.lbl_alvo.config(text=f"📁 Pasta: {nome_curto}", foreground="#0052cc")
            else:
                self.lbl_alvo.config(text=f"📄 Arquivo: {nome_curto}", foreground="#0052cc")

    def escolher_arquivo(self):
        caminho = filedialog.askopenfilename(title="Selecione um documento solto")
        self.atualizar_label(caminho)

    def escolher_pasta(self):
        caminho = filedialog.askdirectory(title="Selecione um diretório inteiro")
        self.atualizar_label(caminho)

    def acao_trancar(self):
        if not self.alvo:
            messagebox.showwarning("Aviso", "Selecione algo primeiro!")
            return

        senha = self.entry_senha.get()
        if not senha:
            messagebox.showwarning("Aviso", "A chave não pode estar vazia!")
            return

        try:
            resultado = processar_trancamento(self.alvo, senha)
            self.resetar_ui()
            messagebox.showinfo("Sucesso!", f"Operação concluída!\nSalvo como: {os.path.basename(resultado)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha: {str(e)}")

    def acao_destrancar(self):
        if not self.alvo:
            messagebox.showwarning("Aviso", "Selecione algo primeiro!")
            return

        # === A CORREÇÃO ESTÁ AQUI ===
        # Agora a interface aceita as duas novas etiquetas inteligentes
        if not (self.alvo.endswith(".pasta_protegida") or self.alvo.endswith(".arquivo_protegido")):
            messagebox.showerror("Erro",
                                 "Formato inválido. O alvo precisa terminar em '.pasta_protegida' ou '.arquivo_protegido'.")
            return

        senha = self.entry_senha.get()
        if not senha:
            messagebox.showwarning("Aviso", "Digite a credencial de acesso!")
            return

        try:
            resultado = processar_destrancamento(self.alvo, senha)
            self.resetar_ui()
            messagebox.showinfo("Sucesso!",
                                f"Conteúdo extraído perfeitamente!\nDisponível em: {os.path.basename(resultado)}")
        except Exception:
            messagebox.showerror("Acesso Negado", "Senha incorreta ou pacote adulterado!")
    def resetar_ui(self):
        """Limpa a tela após o sucesso para não deixar vestígios visuais"""
        self.alvo = None
        self.lbl_alvo.config(text="Nenhum item selecionado", foreground="gray")
        self.entry_senha.delete(0, tk.END)


if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = AppCofre(janela_principal)
    janela_principal.mainloop()