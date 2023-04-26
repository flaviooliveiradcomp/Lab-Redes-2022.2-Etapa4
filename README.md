# Lab-Redes-2022.2-Etapa4
Flávio Emanuel de Oliveira Santos (201900016974)<br/>
Entrega 4 - fase de implementação e treinamento<br/>
IMAGE ID: 75e18a38d069
```
$ docker images
...
entrega4  latest  75e18a38d069  38 hours ago 115MB
...
```

Obs: Parâmetros definidos pelo usuário ou ambiente estão marcados com <>

### Build:
```
$ docker build -t entrega4 .
```
### Execução do Servidor:
```
$ docker run -d -p <port>:12000 -it --rm --name entrega4 entrega4
```
### Execução do Client
1 - Chamada do interpretador por dentro do container
```
$ docker exec -i -t <id> /bin/bash
# python TCPClient.py
```

Exemplo de uso:
```
root@3bb3d36503b4:/usr/src/flavio-etapa4# python TCPClient.py
<!DOCTYPE html>
<html>
<head>
        <title>Web and File Server</title>
    <subtitle>COMP0463 - LABORATÓRIO DE REDES DE COMPUTADORES (2022.2 - T01)</subtitle>
    <br/>
    <subtitle>FLAVIO EMANUEL DE OLIVEIRA SANTOS (201900016974)</subtitle>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
        <header>
                <h1>Welcome to the Web and File Server Project</h1>
        </header>

        <main>
                <section id="about">
                        <h2>About Us</h2>
                        <p>
                We are a Web and File Server Project that offers a variety of services to our clients. 
                Our team consists of experienced developers and engineers who are passionate about del
                ivering high-quality solutions that meet the unique needs of each client.
            </p>
            <p>
                The new network will be used by users who want to host a web application or file server.
                The project supports communication in hybrid mode, that is, between the company and customers
                (retail) and within the company. Supported business functions involve hosting web and file servers.
                Within the network there are all the components and infrastructure for providing services, as well
                as the professionals of the companies that wish to maintain them. Outside the network are all 
                those who are not customers, as well as those who do not work for the service provider.
            </p>
                </section>

                <section id="services">
                        <h2>Our Services</h2>
                        <ul>
                                <li>Web Development</li>
                                <li>File Server Management</li>
                                <li>Cloud Hosting</li>
                                <li>And more...</li>
                        </ul>
                </section>
        </main>

        <footer>
                <p>&copy; 2023 Web and File Server Project. All rights reserved.</p>
        </footer>

</body>
</html>
```

2 - Chamada externa
```
$ docker exec <id> python TCPClient.py
```

Exemplo de uso:
```
flsantos0101@cedro:~/Lab-Redes-2022.2-Etapa4$ docker exec 3bb3d36503b4 python TCPClient.py
<!DOCTYPE html>
<html>
<head>
        <title>Web and File Server</title>
    <subtitle>COMP0463 - LABORATÓRIO DE REDES DE COMPUTADORES (2022.2 - T01)</subtitle>
    <br/>
    <subtitle>FLAVIO EMANUEL DE OLIVEIRA SANTOS (201900016974)</subtitle>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
        <header>
                <h1>Welcome to the Web and File Server Project</h1>
        </header>

        <main>
                <section id="about">
                        <h2>About Us</h2>
                        <p>
                We are a Web and File Server Project that offers a variety of services to our clients. 
                Our team consists of experienced developers and engineers who are passionate about del
                ivering high-quality solutions that meet the unique needs of each client.
            </p>
            <p>
                The new network will be used by users who want to host a web application or file server.
                The project supports communication in hybrid mode, that is, between the company and customers
                (retail) and within the company. Supported business functions involve hosting web and file servers.
                Within the network there are all the components and infrastructure for providing services, as well
                as the professionals of the companies that wish to maintain them. Outside the network are all 
                those who are not customers, as well as those who do not work for the service provider.
            </p>
                </section>

                <section id="services">
                        <h2>Our Services</h2>
                        <ul>
                                <li>Web Development</li>
                                <li>File Server Management</li>
                                <li>Cloud Hosting</li>
                                <li>And more...</li>
                        </ul>
                </section>
        </main>

        <footer>
                <p>&copy; 2023 Web and File Server Project. All rights reserved.</p>
        </footer>

</body>
</html>
```
