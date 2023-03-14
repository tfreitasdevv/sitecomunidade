# from comunidadeimpressionadora import app, database
# from comunidadeimpressionadora.models import Usuario

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Lira', email='lira@email.com', senha='123456')
#     usuario2 = Usuario(username='João', email='joao@email.com', senha='123456')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = meus_usuarios[2]
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.username)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.senha)
#     print(primeiro_usuario.posts)


# with app.app_context():
#     usuario = Usuario.query.filter_by(email='thiagocasa@email.com').first()
#     print(usuario.cursos)
#     print(usuario.posts[0].data_criacao)

# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(email='lira@email.com').first()
#     print(usuario_teste)
#     print(usuario_teste.email)

# with app.app_context():
#     meu_post = Post(titulo='Primeiro post', id_usuario='1', corpo='Lira voando')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.username)

# with app.app_context():
#     database.drop_all()
#     database.create_all()
