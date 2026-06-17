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

# Add an image to the PDF
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)



def generate_pdf(candidate):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    
    # Cria a imagem
    logo = Image(
        "fantasy_logo.png",
        width=90,
        height=90
    )
    
    # Centraliza a logo
    logo.hAlign = "CENTER"

    elements = [
        logo,
        
        Spacer(1, 15),
        
        Paragraph("<b>NOVO CANDIDATO DA FANTASY FOLHEADOS</b>", styles["Title"]),
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