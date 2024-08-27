from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        ))

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ))

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        ))

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joao.silva@xpto.com"
            }
        ))

    senha1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ))

    senha2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ))

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo usuário")
            else:
                return nome

    def clean_senha2(self):
        senha_1 = self.cleaned_data.get('senha1')
        senha_2 = self.cleaned_data.get('senha2')
        if senha_1 and senha_2:
            if senha_2 != senha_1:
                raise forms.ValidationError('Senhas não conferem!')
            else:
                return senha_2
