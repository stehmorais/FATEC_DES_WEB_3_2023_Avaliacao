from django.test import TestCase
from .models import RegistroModel
from django.shortcuts import resolve_url as r
from .forms import RegistroForm, RegistroModelForm

# Teste para verificar se a resposta HTTP é 200 (OK)
class RegistrarTestCase(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    
    def test_200_response(self):
        # Verifica se a resposta HTTP é 200
        self.assertEqual(200, self.resp.status_code)

    def test_template_registrar(self):
        # Verifica se o template 'registrar.html' é usado
        self.assertTemplateUsed(self.resp, 'registrar.html')
    
    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('<header>', 1),
            ('<nav>', 1),
            ('</nav>', 1),
            ('<br>', 2),
            ('</header>', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                # Verifica se as tags HTML estão presentes na resposta
                self.assertContains(self.resp, text, count)

# Teste para verificar se a resposta HTTP é 200 (OK)
class ListarTestCase(TestCase):
    def setUp(self):
        self.resp = self.client.get('/listar')

    def test_200_response(self):
        # Verifica se a resposta HTTP é 200
        self.assertEqual(200, self.resp.status_code)

    def test_template_listar(self):
        # Verifica se o template 'listar.html' é usado
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_html(self):
        tags = (
            ('<html lang="pt-br">', 1),
            ('<body>', 1),
            ('<header>', 1),
            ('<nav>', 1),
            ('</nav>', 1),
            ('<br>', 3),
            ('</header>', 1),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                # Verifica se as tags HTML estão presentes na resposta
                self.assertContains(self.resp, text, count)

# Teste para verificar a criação do objeto RegistroModel
class RegistarModelTest(TestCase):
    def setUp(self):
        self.registro = RegistroModel(
            nome='Maria Neves',
            professor='Junior Santos'
        )
        self.registro.save()
        self.resp = self.client.post(r('core:registrar'))
    
    def test_200_response(self):
        # Verifica se a resposta HTTP é 200
        self.assertEqual(200, self.resp.status_code)

    def test_created(self):
        # Verifica se o objeto RegistroModel foi criado
        self.assertTrue(RegistroModel.objects.exists())

    def test_nome(self):
        nome = self.registro.__dict__.get('nome', '')
        # Verifica se o atributo 'nome' do objeto RegistroModel é consistente
        self.assertEqual(nome, self.registro.nome)
    
    def test_professor(self):
        professor = self.registro.__dict__.get('professor', '')
        # Verifica se o atributo 'professor' do objeto RegistroModel é consistente
        self.assertAlmostEqual(professor, self.registro.professor)

# Teste para verificar a criação do objeto RegistroModel
class ListarModelTest(TestCase):
    def setUp(self):
        self.registro = RegistroModel(
            nome='Maria Neves',
            professor='Junior Santos'
        )
        self.registro.save()
        self.resp = self.client.post(r('core:listar'))
    
    def test_200_response(self):
        # Verifica se a resposta HTTP é 200
        self.assertEqual(200, self.resp.status_code)

    def test_created(self):
        # Verifica se o objeto RegistroModel foi criado
        self.assertTrue(RegistroModel.objects.exists())

    def test_nome(self):
        nome = self.registro.__dict__.get('nome', '')
        # Verifica se o atributo 'nome' do objeto RegistroModel é consistente
        self.assertEqual(nome, self.registro.nome)
    
    def test_professor(self):
        professor = self.registro.__dict__.get('professor', '')
        # Verifica se o atributo 'professor' do objeto RegistroModel é consistente
        self.assertAlmostEqual(professor, self.registro.professor)

# Teste para verificar os campos do formulário RegistroForm
class RegistroFormTest(TestCase):
    def test_forms_has_fields(self):
        form = RegistroForm()
        expected = ['nome', 'professor']
        # Verifica se o formulário RegistroForm possui os campos esperados
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='Maria Neves')
        # Verifica se o campo 'nome' é capitalizado corretamente
        self.assertEqual('MARIA NEVES', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
            nome='Maria Neves',
            professor='Junior Santos'
        )
        data = dict(valid, **kwargs)
        form = RegistroForm(data)
        form.is_valid()
        return form

# Teste para verificar os campos do formulário RegistroModelForm
class RegistroModelFormTest(TestCase):
    def test_forms_has_fields(self):
        form = RegistroModelForm()
        expected = ['nome', 'professor']
        # Verifica se o formulário RegistroModelForm possui os campos esperados
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='Maria Neves')
        # Verifica se o campo 'nome' é capitalizado corretamente
        self.assertEqual('MARIA NEVES', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
            nome='Maria Neves',
            professor='Junior Santos'
        )
        data = dict(valid, **kwargs)
        form = RegistroModelForm(data)
        form.is_valid()
        return form
