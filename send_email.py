import os
import smtplib
import ssl
from email.mime.text import MIMEText
from schemes import DataForEmail

import os
import ssl
import smtplib
from io import BytesIO

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet



def generate_pdf(candidate):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = [
        Paragraph("<b>NOVO CANDIDATO CADASTRADO</b>", styles["Title"]),
        Spacer(1, 20),

        # ======================
        # DADOS PESSOAIS
        # ======================
        Paragraph("<b>DADOS PESSOAIS</b>", styles["Heading2"]),
        Spacer(1, 8),

        Paragraph(f"<b>Nome:</b> {candidate.name}", styles["BodyText"]),
        Paragraph(f"<b>WhatsApp:</b> {candidate.tel}", styles["BodyText"]),
        Paragraph(f"<b>CPF:</b> {candidate.cpf}", styles["BodyText"]),
        Paragraph(
            f"<b>Data de nascimento:</b> {candidate.birth_date}",
            styles["BodyText"]
        ),
        Paragraph(
            f"<b>Instagram/Facebook:</b> {candidate.instagram_facebook}",
            styles["BodyText"]
        ),

        Spacer(1, 15),

        # ======================
        # ENDEREÇO
        # ======================
        Paragraph("<b>ENDEREÇO</b>", styles["Heading2"]),
        Spacer(1, 8),

        Paragraph(f"<b>CEP:</b> {candidate.cep}", styles["BodyText"]),
        Paragraph(f"<b>Cidade:</b> {candidate.city}", styles["BodyText"]),
        Paragraph(f"<b>Estado:</b> {candidate.state}", styles["BodyText"]),

        Spacer(1, 15),

        # ======================
        # EXPERIÊNCIA PROFISSIONAL
        # ======================
        Paragraph("<b>EXPERIÊNCIA PROFISSIONAL</b>", styles["Heading2"]),
        Spacer(1, 8),

        Paragraph(
            f"<b>Situação profissional:</b> "
            f"{candidate.professional_situation}",
            styles["BodyText"]
        ),

        Paragraph(
            f"<b>Produtos ou segmentos que já trabalhou:</b><br/>"
            f"{candidate.product_exp}",
            styles["BodyText"]
        ),

        Paragraph(
            f"<b>Produto que vende atualmente:</b><br/>"
            f"{candidate.current_product}",
            styles["BodyText"]
        ),

        Spacer(1, 15),

        # ======================
        # PERFIL COMERCIAL
        # ======================
        Paragraph("<b>PERFIL COMERCIAL</b>", styles["Heading2"]),
        Spacer(1, 8),

        Paragraph(
            f"<b>Objetivo da revenda:</b> "
            f"{candidate.income}",
            styles["BodyText"]
        ),

        # Paragraph(
        #     f"<b>Tempo disponível para vendas:</b> "
        #     f"{candidate.available_time}",
        #     styles["BodyText"]
        # ),

        Paragraph(
            f"<b>Representante que indicou:</b> "
            f"{candidate.commercial_representative}",
            styles["BodyText"]
        ),

        Paragraph(
            f"<b>Por que acredita que seria uma boa revendedora Fantasy?</b><br/>"
            f"{candidate.motivation}",
            styles["BodyText"]
        ),

        Spacer(1, 20),

        # ======================
        # AVALIAÇÃO FINAL
        # ======================
        Paragraph("<b>AVALIAÇÃO FINAL</b>", styles["Heading2"]),
        Spacer(1, 8),

        Paragraph(
            f"<b>Pontuação final:</b> {candidate.score}",
            styles["Heading3"]
        ),
    ]

    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf





def send_to_email(candidate: DataForEmail):
    
    pdf_content = generate_pdf(candidate)
    

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
        
    

    msg = MIMEMultipart()
    msg["Subject"] = "Novo candidato"
    msg["From"] = os.getenv("EMAIL_USER") #type: ignore
    msg["To"] = 'mcfullp9mo@gmail.com'  # #type: ignore
    
    # Corpo simples do e-mail
    msg.attach(MIMEText(
        "Segue em anexo o PDF com os dados do candidato.",
        "plain"
    ))
    
     # Anexa o PDF
    attachment = MIMEApplication(pdf_content, _subtype="pdf")
    attachment.add_header(
        "Content-Disposition",
        "attachment",
        filename=f"candidato_{candidate.cpf}.pdf"
    )
    
    msg.attach(attachment)


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