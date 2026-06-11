import os
import smtplib
import ssl
from email.mime.text import MIMEText
from schemes import DataForEmail

def send_to_email(candidate: DataForEmail):

    corpo = f"""
        <html>
        <body>
            <p><b>Novo candidato cadastrado</b></p>

            <p><b>Nome:</b> {candidate.name}</p>
            <p><b>WhatsApp:</b> {candidate.tel}</p>
            <p><b>CPF:</b> {candidate.cpf}</p>
            <p><b>Data de nascimento:</b> {candidate.birth_date}</p>
            <p><b>Instagram/Facebook:</b> {candidate.instagram_facebook}</p>

            <p><b>Situação profissional:</b> {candidate.professional_situation}</p>
            <p><b>CEP:</b> {candidate.cep}</p>
            <p><b>Cidade:</b> {candidate.city}</p>
            <p><b>Estado:</b> {candidate.state}</p>

            <p><b>Produtos ou segmentos que já trabalhei:</b> {candidate.product_exp}</p>
            <p><b>Produto que faço venda atualmente:</b> {candidate.current_product}</p>
            <p><b>Você pretende fazer da revenda uma renda extra ou principal:</b> {candidate.income}</p>
            <p><b>Quantas horas por dia você acredita que consegue dedicar às vendas?:</b> {candidate.available_time}</p>

            <p><b>Nome do Representante comercial da Fantasy que me indicou:</b> {candidate.commercial_representative}</p>
            <p><b>Por que você acredita que seria uma boa revendedora Fantasy?:</b> {candidate.motivation}</p>

            <p><b>Pontuação final:</b> {candidate.score}</p>
        </body>
        </html>
        """

    msg = MIMEText(corpo, "html")
    msg["Subject"] = "Novo candidato"
    msg["From"] = os.getenv("EMAIL_USER") #type: ignore
    msg["To"] = 'mcfullp9mo@gmail.com'  # envia para você mesmo #type: ignore

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        context=ssl.create_default_context()
    ) as server:

        server.login(
            os.getenv("EMAIL_USER"), #type: ignore
            os.getenv("EMAIL_PASSWORD") #type: ignore
        )

        server.send_message(msg)