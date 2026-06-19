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

def create_pdf(elements):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf

def generate_pdf(candidate: DataForEmail):
    #buffer = BytesIO()

    #doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    
    # Cria a imagem
    logo = Image(
        "fantasy_logo.png",
        width=90,
        height=90
    )
    
    # Centraliza a logo
    logo.hAlign = "CENTER"

    elements_for_representative = [
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
        Paragraph(f"<b>Rua:</b> {candidate.street}", styles["BodyText"]),
        Paragraph(f"<b>Número:</b> {candidate.residence_number}", styles["BodyText"]),

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
    
    
    
    
    elements_for_attendant = [
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
        Paragraph(f"<b>Rua:</b> {candidate.street}", styles["BodyText"]),
        Paragraph(f"<b>Número:</b> {candidate.residence_number}", styles["BodyText"]),

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
            f"<b>Você possui carteira assinada atualmente:</b>"
            f"{candidate.signed_card}",
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
            f"<b>Gosta de trabalhar com atendimento:</b> "
            f"{candidate.enjoy_servicing}",
            styles["BodyText"]
        ),

        Paragraph(
            f"<b>Objetivo da revenda:</b> "
            f"{candidate.income}",
            styles["BodyText"]
        ),



        Paragraph(
            f"<b>Representante que indicou:</b> "
            f"{candidate.commercial_representative}",
            styles["BodyText"]
        ),

        Paragraph(
            f"<b>Por que acredita que seria uma boa revendedora Fantasy:</b><br/>"
            f"{candidate.motivation}",
            styles["BodyText"]
        ),
        
        Spacer(1, 8),
        
        # ======================
        # Informações Financeiras
        # ======================
        
        Paragraph("<b>INFORMAÇÕES FINANCEIRAS</b>", styles["Heading2"]),
        Spacer(1, 8),
        
        Paragraph(
            f"<b>Possui restrições financeiras:</b> "
            f"{candidate.restriction}",
            styles["BodyText"]
        ),
        
        Paragraph(
            f"<b>Possui conta bancária em seu nome: </b> "
            f"{candidate.bank_account}",
            styles["BodyText"]
        ),
        

        Spacer(1, 20),
        
        
        
        # ======================
        # Informações Adicionais
        # ======================
        Paragraph("<b>INFORMAÇÕES ADICIONAIS</b>", styles["Heading2"]),
        
        Spacer(1, 8),
        
        Paragraph(
            f"<b>Possui veículo:</b> "
            f"{candidate.has_vehicle}",
            styles["BodyText"]
        ),
        
        Paragraph(
            f"<b>Tipo de veículo:</b> "
            f"{candidate.vehicle_type}",
            styles["BodyText"]
        ),
        
        Paragraph(
            f"<b>Tipo de residência:</b> "
            f"{candidate.residence_type}",
            styles["BodyText"]
        ),
        
        
        Spacer(1, 8),

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


    pdf_representative = create_pdf(elements_for_representative)
    pdf_attendant = create_pdf(elements_for_attendant)
    
    # doc.build(elements_for_representative)

    # pdf = buffer.getvalue()
    # buffer.close()

    return [pdf_attendant, pdf_representative]





def send_to_email(candidate: DataForEmail):
    
    pdf_attendant, pdf_representative = generate_pdf(candidate)
        
    

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
    attachment = MIMEApplication(pdf_representative, _subtype="pdf")
    attachment.add_header(
        "Content-Disposition",
        "attachment",
        filename=f"documento_para_representante.pdf"
    )
    
    msg.attach(attachment)
    
    
    attachment2 = MIMEApplication(
        pdf_attendant,
        _subtype="pdf"
    )
    
    attachment2.add_header(
        "Content-Disposition",
        "attachment",
        filename=f"documento_para_atendente.pdf"
    )
    
    msg.attach(attachment2)


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