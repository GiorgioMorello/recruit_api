import os
import smtplib
import ssl
from email.mime.text import MIMEText
from schemes import DataForEmail

def send_to_email(candidate: DataForEmail):

    corpo = f"""
    Novo candidato cadastrado

    Nome: {candidate.name}
    WhatsApp: {candidate.tel}
    CPF: {candidate.cpf}
    Data de nascimento: {candidate.birth_date}
    Instagram/Facebook: {candidate.instagram_facebook}

    Situação profissional: {candidate.professional_situation}
    CEP: {candidate.cep}
    Cidade: {candidate.city}
    Estado: {candidate.state}

    Produtos ou segmentos que já trabalhei: {candidate.product_exp}
    Produto que faço venda atualmente: {candidate.current_product}
    Você pretende fazer da revenda uma renda extra ou principal: {candidate.income}
    Quantas horas por dia você acredita que consegue dedicar às vendas?: {candidate.available_time}

    Nome do Representante comercial da Fantasy que me indicou: {candidate.commercial_representative}
    Por que você acredita que seria uma boa revendedora Fantasy?: {candidate.motivation}

    Pontuação final: {candidate.score}
    """

    msg = MIMEText(corpo)
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