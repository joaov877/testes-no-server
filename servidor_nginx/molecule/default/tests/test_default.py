def test_nginx_instalado_e_rodando(host):

    # Verificar se o Nginx está instalado
    pacote = host.package("nginx")
    assert pacote.is_installed

    # Verificar se o serviço está rodando e habilitado
    servico = host.service("nginx")
    assert servico.is_running
    assert servico.is_enabled

    # Verificar se a porta 80 está escutando
    porta = host.socket("tcp://0.0.0.0:80")
    assert porta.is_listening